"""
frbr_uri/parsers/page_fetcher.py
tags: akn, fetcher, fedlex, zh-lex

Fetches the actual HTML page for a legal document URL and extracts
structured metadata that is not present in the URL alone:
  - Official title
  - Short title / abbreviation (e.g. OR, DSG, ZGB)
  - SR / LS citation number
  - Enactment date (Erlassdatum)
  - Entry into force date (Inkraftsetzungsdatum)
  - Repeal date (Aufhebungsdatum)
  - Publication date
  - Status (current / repealed / not-yet-in-force)

This enriches ParsedDocumentUrl with the data needed to:
  1. Populate AKN <FRBRWork> metadata
  2. Resolve the DocumentPointer (short title > SR > AS number)
  3. Build human-readable citations

Usage:
    from frbr_uri.parsers.page_fetcher import fetch_metadata
    from frbr_uri.parsers.url_parser import parse_legal_url

    parsed = parse_legal_url("https://www.fedlex.admin.ch/eli/cc/1999/404/de")
    meta = fetch_metadata(parsed.source_uri)
    print(meta.short_title)   # "BV"
    print(meta.sr_number)     # "101"
    print(meta.title_de)      # "Bundesverfassung der Schweizerischen Eidgenossenschaft"
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Optional
from urllib.parse import urlparse

try:
    import requests
    from bs4 import BeautifulSoup
    _DEPS_AVAILABLE = True
except ImportError:
    _DEPS_AVAILABLE = False


TIMEOUT = 10  # seconds

HEADERS = {
    "User-Agent": "akn-pipeline/0.1 (Swiss legal document AKN converter; contact@example.ch)",
    "Accept-Language": "de-CH,de;q=0.9,fr-CH;q=0.8,en;q=0.5",
}


# ── Result dataclass ──────────────────────────────────────────────────────────

@dataclass
class FetchedMetadata:
    """Metadata extracted from a fetched legal document page."""

    source_url: str
    platform: str                        # "fedlex", "zh-lex"

    # Titles
    title_de: Optional[str] = None
    title_fr: Optional[str] = None
    title_it: Optional[str] = None
    short_title: Optional[str] = None    # Official abbreviation: OR, DSG, ZGB

    # Citation identifiers
    sr_number: Optional[str] = None      # SR / LS Ordnungsnummer
    as_number: Optional[str] = None      # AS / OS publication number

    # Dates (ISO 8601, YYYY-MM-DD)
    enactment_date: Optional[str] = None
    entry_into_force: Optional[str] = None
    repeal_date: Optional[str] = None
    publication_date: Optional[str] = None
    consolidation_date: Optional[str] = None   # "Stand am" / "En vigueur depuis"

    # Status
    status: str = "unknown"              # "current", "repealed", "future", "unknown"

    # Errors / warnings
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    raw_html_snippet: Optional[str] = None   # first 2000 chars for debugging

    def preferred_short_id(self) -> str:
        """Return the best available short identifier (F8 priority)."""
        if self.short_title:
            return self.short_title
        if self.sr_number:
            return f"SR {self.sr_number}"
        if self.as_number:
            return f"AS {self.as_number}"
        return ""

    def to_dict(self) -> dict:
        return {
            "source_url": self.source_url,
            "platform": self.platform,
            "title_de": self.title_de,
            "title_fr": self.title_fr,
            "title_it": self.title_it,
            "short_title": self.short_title,
            "sr_number": self.sr_number,
            "as_number": self.as_number,
            "enactment_date": self.enactment_date,
            "entry_into_force": self.entry_into_force,
            "repeal_date": self.repeal_date,
            "publication_date": self.publication_date,
            "consolidation_date": self.consolidation_date,
            "status": self.status,
            "errors": self.errors,
            "warnings": self.warnings,
        }


# ── Main entry point ──────────────────────────────────────────────────────────

def fetch_metadata(url: str, timeout: int = TIMEOUT) -> FetchedMetadata:
    """
    Fetch a Swiss legal document URL and extract structured metadata.

    Works with:
      - https://www.fedlex.admin.ch/eli/cc/…
      - https://fedlex.data.admin.ch/eli/cc/…  (redirects to www)
      - http://www.zhlex.zh.ch/Erlass.html?…
      - https://www.zh.ch/de/politik-staat/…/zhlex-ls/erlass-….html

    Returns FetchedMetadata. Never raises — errors are stored in .errors.
    """
    if not _DEPS_AVAILABLE:
        return FetchedMetadata(
            source_url=url, platform="unknown",
            errors=["requests and beautifulsoup4 not installed. "
                    "Run: pip install requests beautifulsoup4"]
        )

    host = urlparse(url).netloc.lower()
    try:
        resp = requests.get(url, headers=HEADERS, timeout=timeout,
                            allow_redirects=True)
        resp.raise_for_status()
    except Exception as exc:
        return FetchedMetadata(source_url=url, platform="unknown",
                               errors=[f"HTTP error: {exc}"])

    html = resp.text
    soup = BeautifulSoup(html, "html.parser")

    if host in ("www.fedlex.admin.ch", "fedlex.data.admin.ch"):
        return _extract_fedlex(url, soup, html)
    elif host in ("www.zhlex.zh.ch", "zhlex.zh.ch"):
        return _extract_zhlex(url, soup, html)
    elif host in ("www.zh.ch", "zh.ch"):
        return _extract_zhch_portal(url, soup, html)
    else:
        return FetchedMetadata(
            source_url=url, platform="unknown",
            errors=[f"No extractor for host: {host}"]
        )


# ── Fedlex extractor ──────────────────────────────────────────────────────────

def _extract_fedlex(url: str, soup: BeautifulSoup, html: str) -> FetchedMetadata:
    """
    Extract metadata from a Fedlex HTML page.

    Fedlex is a JS-heavy SPA (Vue.js). The server renders a minimal shell;
    most content loads via XHR. We try two strategies:
      A. Parse the server-rendered <meta> og: tags and title (always present)
      B. Parse inline JSON-LD if available
      C. Hit the Fedlex data API for the RDF/JSON metadata

    For maximum reliability without a headless browser, we also try the
    fedlex.data.admin.ch JSON endpoint.
    """
    meta = FetchedMetadata(source_url=url, platform="fedlex")
    meta.raw_html_snippet = html[:2000]

    # Strategy A: OG / meta tags
    og_title = soup.find("meta", property="og:title")
    if og_title:
        raw_title = og_title.get("content", "")
        meta.title_de = raw_title.strip() if raw_title else None

    # <title> tag fallback
    if not meta.title_de:
        title_tag = soup.find("title")
        if title_tag:
            meta.title_de = title_tag.get_text(strip=True)

    # Strategy B: JSON-LD
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            import json
            data = json.loads(script.string or "")
            if isinstance(data, dict):
                name = data.get("name") or data.get("headline")
                if name:
                    meta.title_de = str(name)
        except Exception:
            pass

    # Strategy C: Fedlex data API JSON
    # Convert www URL to data URI for API call
    data_url = url.replace("www.fedlex.admin.ch", "fedlex.data.admin.ch")
    # Remove language suffix for data URI
    data_uri = re.sub(r"/(de|fr|it|rm|en)$", "", data_url)

    try:
        api_resp = requests.get(
            data_uri,
            headers={**HEADERS, "Accept": "application/json"},
            timeout=TIMEOUT,
        )
        if api_resp.ok:
            try:
                api_data = api_resp.json()
                _parse_fedlex_api(meta, api_data)
            except Exception:
                pass
    except Exception as exc:
        meta.warnings.append(f"API fetch failed: {exc}")

    # Derive SR number from URL if still missing
    # Pattern: /eli/cc/{year}/{as_number}
    m = re.search(r"/eli/cc/(\d{4})/([^/]+)", url)
    if m and not meta.as_number:
        meta.as_number = f"{m.group(1)}/{m.group(2)}"

    if not meta.title_de:
        meta.warnings.append(
            "Fedlex is a JavaScript SPA — full metadata requires the data API. "
            "Consider using the SPARQL endpoint for complete metadata."
        )

    return meta


def _parse_fedlex_api(meta: FetchedMetadata, data: dict) -> None:
    """Parse Fedlex JSON API response into FetchedMetadata fields."""
    # The Fedlex API returns JOLux-structured JSON
    # Top-level keys vary; handle both raw and consolidated objects

    def _find(d: dict, *keys):
        for k in keys:
            if k in d:
                return d[k]
        return None

    # Title in multiple languages
    titles = _find(data, "title", "dcterms:title", "jolux:title")
    if isinstance(titles, dict):
        meta.title_de = titles.get("de") or titles.get("deu")
        meta.title_fr = titles.get("fr") or titles.get("fra")
        meta.title_it = titles.get("it") or titles.get("ita")
    elif isinstance(titles, str):
        meta.title_de = titles

    # Short title / abbreviation
    abbrev = _find(data, "abbreviation", "jolux:abbreviation", "shortTitle")
    if isinstance(abbrev, dict):
        meta.short_title = abbrev.get("de") or abbrev.get("fr") or abbrev.get("it")
    elif isinstance(abbrev, str):
        meta.short_title = abbrev

    # SR number
    sr = _find(data, "classifiedByTaxonomyEntry", "jolux:classifiedByTaxonomyEntry",
               "srNumber", "jolux:srNumber")
    if sr:
        # SR comes as a URI like https://fedlex.data.admin.ch/vocabulary/classification/101
        if isinstance(sr, str) and "/" in sr:
            meta.sr_number = sr.rstrip("/").split("/")[-1]
        elif isinstance(sr, str):
            meta.sr_number = sr

    # Dates
    for field_name, keys in [
        ("enactment_date", ["jolux:dateDocument", "dateDocument"]),
        ("entry_into_force", ["jolux:dateEntryInForce", "dateEntryInForce"]),
        ("repeal_date", ["jolux:dateNoLongerInForce", "dateNoLongerInForce"]),
        ("publication_date", ["jolux:publicationDate", "publicationDate"]),
    ]:
        val = _find(data, *keys)
        if val:
            setattr(meta, field_name, str(val)[:10])  # keep YYYY-MM-DD

    # Status
    if meta.repeal_date:
        meta.status = "repealed"
    elif meta.entry_into_force:
        meta.status = "current"


# ── ZH-Lex legacy extractor ───────────────────────────────────────────────────

def _extract_zhlex(url: str, soup: BeautifulSoup, html: str) -> FetchedMetadata:
    """
    Extract metadata from zhlex.zh.ch/Erlass.html pages.
    These are older Lotus Notes-rendered HTML pages with predictable structure.
    """
    meta = FetchedMetadata(source_url=url, platform="zh-lex")
    meta.raw_html_snippet = html[:2000]

    text = soup.get_text(separator=" ", strip=True)

    # Title: usually in <title> or first <h1>/<h2>
    title_tag = soup.find("title")
    if title_tag:
        raw = title_tag.get_text(strip=True)
        # Remove site suffix
        meta.title_de = re.sub(r"\s*[|\-–—].*$", "", raw).strip() or None

    h1 = soup.find("h1") or soup.find("h2")
    if h1 and not meta.title_de:
        meta.title_de = h1.get_text(strip=True) or None

    # LS Ordnungsnummer
    m = re.search(r"Ordnungsnummer[:\s]+([0-9.]+)", text)
    if m:
        meta.sr_number = m.group(1)  # treat LS number as sr_number

    # Short title (Kurztitel or Abkürzung)
    m = re.search(r"(?:Abk[üu]rzung|Kurztitel)[:\s]+([A-ZÄÖÜ][A-Za-zäöüÄÖÜ]+)", text)
    if m:
        meta.short_title = m.group(1)

    # Dates: dd.mm.yyyy pattern labeled
    date_patterns = [
        (r"Erlassdatum[:\s]+(\d{2}\.\d{2}\.\d{4})", "enactment_date"),
        (r"Inkraftsetzungsdatum[:\s]+(\d{2}\.\d{2}\.\d{4})", "entry_into_force"),
        (r"Aufhebungsdatum[:\s]+(\d{2}\.\d{2}\.\d{4})", "repeal_date"),
        (r"Publikationsdatum[:\s]+(\d{2}\.\d{2}\.\d{4})", "publication_date"),
        (r"Stand\s+(?:am|vom)[:\s]+(\d{2}\.\d{2}\.\d{4})", "consolidation_date"),
    ]
    for pattern, field_name in date_patterns:
        m = re.search(pattern, text)
        if m:
            setattr(meta, field_name, _ddmmyyyy_to_iso(m.group(1)))

    # Status
    if meta.repeal_date:
        meta.status = "repealed"
    elif "aufgehoben" in text.lower():
        meta.status = "repealed"
    elif meta.entry_into_force:
        meta.status = "current"

    return meta


def _extract_zhch_portal(url: str, soup: BeautifulSoup, html: str) -> FetchedMetadata:
    """
    Extract metadata from zh.ch portal pages (/zhlex-ls/erlass-…).
    These pages use a structured layout with labeled fields.
    """
    meta = FetchedMetadata(source_url=url, platform="zh-lex")
    meta.raw_html_snippet = html[:2000]

    text = soup.get_text(separator=" ", strip=True)

    # Title from og:title or h1
    og = soup.find("meta", property="og:title")
    if og:
        meta.title_de = og.get("content", "").strip() or None

    if not meta.title_de:
        h1 = soup.find("h1")
        if h1:
            meta.title_de = h1.get_text(strip=True) or None

    # Look for structured field labels in the page
    for label_text, field_name in [
        ("Erlassdatum", "enactment_date"),
        ("Inkraftsetzungsdatum", "entry_into_force"),
        ("Aufhebungsdatum", "repeal_date"),
        ("Publikationsdatum", "publication_date"),
    ]:
        m = re.search(
            label_text + r"[^0-9]*(\d{2}\.\d{2}\.\d{4})",
            text
        )
        if m:
            setattr(meta, field_name, _ddmmyyyy_to_iso(m.group(1)))

    # LS number from URL path if not found in text
    ls_m = re.search(r"erlass-([0-9_]+)-\d{4}", url)
    if ls_m and not meta.sr_number:
        meta.sr_number = ls_m.group(1).replace("_", ".")

    # Status
    if meta.repeal_date:
        meta.status = "repealed"
    elif "aufgehoben" in text.lower():
        meta.status = "repealed"
    elif meta.entry_into_force:
        meta.status = "current"

    return meta


# ── Utilities ─────────────────────────────────────────────────────────────────

def _ddmmyyyy_to_iso(raw: str) -> str:
    m = re.match(r"^(\d{2})\.(\d{2})\.(\d{4})$", raw.strip())
    if m:
        return f"{m.group(3)}-{m.group(2)}-{m.group(1)}"
    return raw
