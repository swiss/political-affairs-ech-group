"""
frbr_uri/parsers/url_parser.py
tags: akn, url-parser, fedlex, zh-lex

Parses URLs from Swiss legal publication platforms into a structured
ParsedDocumentUrl object that can be fed directly to FRBRResolver.

Supported platforms:
  - Fedlex (Classified Compilation, Official Compilation, Federal Gazette)
  - ZH-Lex (legacy zhlex.zh.ch and zh.ch portal URLs)

Usage:
    from frbr_uri.parsers.url_parser import parse_legal_url

    result = parse_legal_url("https://www.fedlex.admin.ch/eli/cc/1999/404/de")
    print(result.jurisdiction)   # "ch"
    print(result.doc_type)       # "act"
    print(result.date)           # "1999-01-01"
    print(result.number)         # "404"
    print(result.lang)           # "de"
    print(result.version)        # None
    print(result.source_uri)     # original URL
    print(result.akn_uris)       # FRBRUris if resolver was injected
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Optional
from urllib.parse import urlparse, parse_qs


# ── Language code mapping (2-letter → 3-letter) ──────────────────────────────
LANG_2_TO_3 = {
    "de": "deu",
    "fr": "fra",
    "it": "ita",
    "rm": "roh",
    "en": "eng",
}

# ── Date conversion helpers ───────────────────────────────────────────────────

def _yyyymmdd_to_iso(raw: str) -> str:
    """Convert Fedlex YYYYMMDD to ISO 8601 YYYY-MM-DD."""
    raw = raw.strip()
    if re.match(r"^\d{8}$", raw):
        return f"{raw[:4]}-{raw[4:6]}-{raw[6:8]}"
    return raw  # already ISO or unknown format


def _ddmmyyyy_to_iso(raw: str) -> str:
    """Convert ZH-Lex DD.MM.YYYY to ISO 8601 YYYY-MM-DD."""
    m = re.match(r"^(\d{2})\.(\d{2})\.(\d{4})$", raw.strip())
    if m:
        return f"{m.group(3)}-{m.group(2)}-{m.group(1)}"
    return raw


# ── Result dataclass ──────────────────────────────────────────────────────────

@dataclass
class ParsedDocumentUrl:
    """
    Structured representation of a parsed Swiss legal URL.

    All dates are in ISO 8601 (YYYY-MM-DD) format.
    Language codes are in 2-letter ISO 639-1 (as on source platform).
    """

    # Core FRBR fields
    jurisdiction: str                   # e.g. "ch", "ch-zh"
    doc_type: str                       # profile doc_type key, e.g. "act", "gazette"
    date: str                           # Work date (YYYY-MM-DD)
    number: str                         # Citation number or pub sequence number

    # Expression fields (may be None if URL is Work-level only)
    lang: Optional[str] = None          # 2-letter ISO 639-1
    version: Optional[str] = None       # YYYY-MM-DD consolidation/version date

    # Source platform metadata
    platform: str = ""                  # "fedlex-cc", "fedlex-oc", "fedlex-fga", "zh-lex"
    source_uri: str = ""                # original URL as-is
    collection: Optional[str] = None    # "cc", "oc", "fga", etc.
    pub_year: Optional[str] = None      # publication year (Fedlex)
    pub_number: Optional[str] = None    # publication sequence number (Fedlex AS number)
    ls_number: Optional[str] = None     # LS Ordnungsnummer (ZH-Lex)
    band_number: Optional[str] = None   # Band number (ZH-Lex version counter)
    inkraft_date: Optional[str] = None  # entry-into-force date (YYYY-MM-DD)
    erlass_date: Optional[str] = None   # enactment date (YYYY-MM-DD)

    # Historical Fedlex pre-1999 fields (volume/page-based identifiers; see
    # spec/URI_fedlex_template.md — "Vor 1999" / "Zwischen 1948 und 1999" /
    # "Zwischen 1848 und 1947"). None for modern (post-1999) sources.
    volume: Optional[str] = None          # roman (1848-1874) or arabic (1874-1947) numeral; FGA pre-2000 volume
    page_de: Optional[str] = None         # per-language page number from the Bundesarchiv scan order
    page_fr: Optional[str] = None
    page_it: Optional[str] = None

    # Warnings and notes for the UI
    warnings: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def to_resolver_kwargs(self) -> dict:
        """Return kwargs suitable for FRBRResolver.resolve()."""
        kwargs = {
            "jurisdiction": self.jurisdiction,
            "doc_type": self.doc_type,
            "date": self.date,
            "number": self.number,
        }
        if self.lang:
            kwargs["lang"] = self.lang
        if self.version:
            kwargs["version"] = self.version
        return kwargs


# ── Main parser ───────────────────────────────────────────────────────────────

class UnsupportedUrlError(ValueError):
    """Raised when the URL is not from a recognised platform."""


def parse_legal_url(url: str) -> ParsedDocumentUrl:
    """
    Parse a Swiss legal publication URL into a ParsedDocumentUrl.

    Raises:
        UnsupportedUrlError: If the URL pattern is not recognised.
    """
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    path = parsed.path

    # ── Fedlex ────────────────────────────────────────────────────────────────
    if host in ("fedlex.data.admin.ch", "www.fedlex.admin.ch"):
        return _parse_fedlex(url, path)

    # ── ZH-Lex legacy ────────────────────────────────────────────────────────
    if host in ("www.zhlex.zh.ch", "zhlex.zh.ch"):
        return _parse_zhlex_legacy(url, parsed)

    # ── ZH.ch portal ─────────────────────────────────────────────────────────
    if host in ("www.zh.ch", "zh.ch"):
        if "zhlex-ls" in path or "zhlex-os" in path:
            return _parse_zhch_portal(url, path)

    raise UnsupportedUrlError(
        f"URL not recognised as a supported Swiss legal platform: {url}\n"
        f"Supported: fedlex.data.admin.ch, www.fedlex.admin.ch, "
        f"www.zhlex.zh.ch, www.zh.ch (zhlex-ls paths)"
    )


# ── Fedlex parser ─────────────────────────────────────────────────────────────

# Patterns for Fedlex path segments after /eli/
# CC work:        /eli/cc/{year}/{number}
# CC expression:  /eli/cc/{year}/{number}/{versiondate}/{lang}
# OC work:        /eli/oc/{year}/{number}
# OC expression:  /eli/oc/{year}/{number}/{lang}
# FGA work/expr:  /eli/fga/{year}/{number}  or  /eli/fga/{year}/{number}/{lang}
#
# Historical (pre-1999) Fedlex patterns — see spec/URI_fedlex_template.md. Three distinct eras,
# each a genuinely different shape, not just a formatting variant of the modern one:
#   - 1848-1947: {collection}/{volume}_{page-de}_{page-fr}_{page-it}   (NO year; volume is roman
#     1848-1874, arabic 1874-1947 — distinguished from a modern 4-digit year by length/alphabet)
#   - 1948-1999 (oc/cc): {year}/{page-de}_{page-fr}_{page-it}          (3 parts, no volume)
#   - pre-2000 (fga specifically): {year}/{volume}_{page-de}_{page-fr}_{page-it}  (4 parts, has a
#     volume; per-language page fields can be *empty* strings when only one language was scanned/
#     aligned, e.g. "1_569__" or "1__1083_" — the page number itself derives from Bundesarchiv scan
#     order for the one available language, not a semantic per-language numbering)
# Checked BEFORE the generic *_WORK patterns below, whose greedy [^/]+ would otherwise swallow
# these as one opaque "number" and lose the real volume/page structure.

_FEDLEX_ROMAN_OR_SHORT_ARABIC_VOLUME = re.compile(r"^(?:[IVXLCDM]+|\d{1,3})$")

# Each may be followed by a modern consolidation {version}/{lang} suffix — a historical text can
# still have a real, current consolidated expression — captured explicitly rather than discarded
# by a generic wildcard, so the two eras' information both survive.
_OPTIONAL_VERSION_LANG_SUFFIX = r"(?:/(\d{8})/([a-z]{2}))?(?:/.*)?$"

_FEDLEX_PRE1947_VOLUME_PAGES = re.compile(
    r"^/eli/(oc|cc)/([IVXLCDM]+|\d{1,3})/(\d+)_(\d+)_(\d+)" + _OPTIONAL_VERSION_LANG_SUFFIX
)
_FEDLEX_1948_1999_YEAR_PAGES = re.compile(
    r"^/eli/(oc|cc)/(\d{4})/(\d+)_(\d+)_(\d+)" + _OPTIONAL_VERSION_LANG_SUFFIX
)
_FEDLEX_PRE2000_FGA_VOLUME_YEAR_PAGES = re.compile(
    r"^/eli/fga/(\d{4})/(\d+)_(\d*)_(\d*)_(\d*)" + _OPTIONAL_VERSION_LANG_SUFFIX
)

_FEDLEX_CC_EXPR = re.compile(
    r"^/eli/cc/(\d{4})/([^/]+)/(\d{8})/([a-z]{2})(?:/.*)?$"
)
_FEDLEX_CC_WORK = re.compile(
    r"^/eli/cc/(\d{4})/([^/]+)(?:/([a-z]{2}))?(?:/.*)?$"
)
_FEDLEX_OC_EXPR = re.compile(
    r"^/eli/oc/(\d{4})/([^/]+)/([a-z]{2})(?:/.*)?$"
)
_FEDLEX_OC_WORK = re.compile(
    r"^/eli/oc/(\d{4})/([^/]+)(?:/.*)?$"
)
_FEDLEX_FGA = re.compile(
    r"^/eli/fga/(\d{4})/([^/]+)(?:/([a-z]{2}))?(?:/.*)?$"
)

def _parse_fedlex(url: str, path: str) -> ParsedDocumentUrl:
    warnings = []
    notes = []

    # ── Historical (pre-1999) patterns — checked first, see module-level comment above ──

    # 1848-1947: {collection}/{volume}_{page-de}_{page-fr}_{page-it}, no year at all.
    m = _FEDLEX_PRE1947_VOLUME_PAGES.match(path)
    if m:
        collection, volume, page_de, page_fr, page_it, version_raw, lang = m.groups()
        version = _yyyymmdd_to_iso(version_raw) if version_raw else None
        warnings = []
        if not version:
            warnings.append("1848-1947 era: no year in the URI itself — Work date is unknown "
                             "from the URI alone; fetch the page for the actual publication date.")
        return ParsedDocumentUrl(
            jurisdiction="ch",
            doc_type="act" if collection == "cc" else "ordinance",
            date="0000-01-01",
            number=f"{volume}_{page_de}_{page_fr}_{page_it}",
            lang=lang,
            version=version,
            platform=f"fedlex-{collection}",
            source_uri=url,
            collection=collection,
            volume=volume,
            page_de=page_de, page_fr=page_fr, page_it=page_it,
            warnings=warnings,
            notes=[f"1848-1947 volume/page identifier (volume={volume}, roman 1848-1874 / arabic "
                   f"1874-1947). Page numbers are per-language Bundesarchiv scan positions, not a "
                   f"semantic article/page number."],
        )

    # 1948-1999 (oc/cc): {year}/{page-de}_{page-fr}_{page-it}, no separate volume.
    m = _FEDLEX_1948_1999_YEAR_PAGES.match(path)
    if m:
        collection, year, page_de, page_fr, page_it, version_raw, lang = m.groups()
        version = _yyyymmdd_to_iso(version_raw) if version_raw else None
        return ParsedDocumentUrl(
            jurisdiction="ch",
            doc_type="act" if collection == "cc" else "ordinance",
            date=f"{year}-01-01",
            number=f"{page_de}_{page_fr}_{page_it}",
            lang=lang,
            version=version,
            platform=f"fedlex-{collection}",
            source_uri=url,
            collection=collection,
            pub_year=year,
            page_de=page_de, page_fr=page_fr, page_it=page_it,
            notes=[f"1948-1999 volume/page identifier (year={year}, no separate volume field). "
                   f"Page numbers are per-language Bundesarchiv scan positions, not the SR/AS "
                   f"citation number."],
        )

    # Pre-2000 FGA specifically: {year}/{volume}_{page-de}_{page-fr}_{page-it} — page fields may
    # be empty strings when only one language was scanned/aligned (e.g. "1_569__").
    m = _FEDLEX_PRE2000_FGA_VOLUME_YEAR_PAGES.match(path)
    if m:
        year, volume, page_de, page_fr, page_it, version_raw, lang = m.groups()
        version = _yyyymmdd_to_iso(version_raw) if version_raw else None
        available_langs = [l for l, pg in (("de", page_de), ("fr", page_fr), ("it", page_it)) if pg]
        return ParsedDocumentUrl(
            jurisdiction="ch",
            doc_type="decision",
            date=f"{year}-01-01",
            number=f"{volume}_{page_de}_{page_fr}_{page_it}",
            lang=lang,
            version=version,
            platform="fedlex-fga",
            source_uri=url,
            collection="fga",
            pub_year=year,
            volume=volume,
            page_de=page_de or None, page_fr=page_fr or None, page_it=page_it or None,
            notes=[f"Pre-2000 FGA volume/page identifier (year={year}, volume={volume}). "
                   f"Page number(s) present for: {', '.join(available_langs) or 'none'} — an "
                   f"empty field means that language wasn't scanned/aligned for this entry, not "
                   f"that the page number is zero."],
        )

    # Classified Compilation — expression level (with consolidation date)
    m = _FEDLEX_CC_EXPR.match(path)
    if m:
        year, number, version_raw, lang = m.groups()
        version = _yyyymmdd_to_iso(version_raw)
        notes.append(
            f"URI number '{number}' is the AS publication sequence number, "
            f"not the SR citation number. SR number is in RDF metadata."
        )
        return ParsedDocumentUrl(
            jurisdiction="ch",
            doc_type="act",
            date=f"{year}-01-01",
            number=number,
            lang=lang,
            version=version,
            platform="fedlex-cc",
            source_uri=url,
            collection="cc",
            pub_year=year,
            pub_number=number,
            warnings=warnings,
            notes=notes,
        )

    # Classified Compilation — work level (possibly with lang suffix)
    m = _FEDLEX_CC_WORK.match(path)
    if m:
        year, number, lang = m.groups()
        if lang and not re.match(r"^\d{8}$", lang):  # avoid matching date as lang
            pass
        else:
            lang = None
        notes.append(
            f"Work-level URI: no version/consolidation date in URL. "
            f"Resolves to current version."
        )
        notes.append(
            f"URI number '{number}' is the AS publication sequence number."
        )
        return ParsedDocumentUrl(
            jurisdiction="ch",
            doc_type="act",
            date=f"{year}-01-01",
            number=number,
            lang=lang,
            platform="fedlex-cc",
            source_uri=url,
            collection="cc",
            pub_year=year,
            pub_number=number,
            warnings=warnings,
            notes=notes,
        )

    # Official Compilation — with language
    m = _FEDLEX_OC_EXPR.match(path)
    if m:
        year, number, lang = m.groups()
        return ParsedDocumentUrl(
            jurisdiction="ch",
            doc_type="ordinance",
            date=f"{year}-01-01",
            number=number,
            lang=lang,
            platform="fedlex-oc",
            source_uri=url,
            collection="oc",
            pub_year=year,
            pub_number=number,
            warnings=warnings,
            notes=["Official Compilation entry — original publication, not consolidated."],
        )

    # Official Compilation — work level
    m = _FEDLEX_OC_WORK.match(path)
    if m:
        year, number = m.groups()
        return ParsedDocumentUrl(
            jurisdiction="ch",
            doc_type="ordinance",
            date=f"{year}-01-01",
            number=number,
            platform="fedlex-oc",
            source_uri=url,
            collection="oc",
            pub_year=year,
            pub_number=number,
            warnings=warnings,
            notes=["Official Compilation entry — work level."],
        )

    # Federal Gazette
    m = _FEDLEX_FGA.match(path)
    if m:
        year, number, lang = m.groups()
        return ParsedDocumentUrl(
            jurisdiction="ch",
            doc_type="decision",
            date=f"{year}-01-01",
            number=number,
            lang=lang,
            platform="fedlex-fga",
            source_uri=url,
            collection="fga",
            pub_year=year,
            pub_number=number,
            warnings=["Federal Gazette entries are language-specific works; "
                      "AKN mapping treats language as expression discriminator."],
            notes=["BBl/FF/FF publication."],
        )

    raise UnsupportedUrlError(
        f"Fedlex URL path not recognised: {path}\n"
        f"Expected patterns: /eli/cc/…, /eli/oc/…, /eli/fga/…"
    )


# ── ZH-Lex legacy parser ──────────────────────────────────────────────────────
#
# URL format: http://www.zhlex.zh.ch/Erlass.html?Open&Ordnr={params}
# Ordnr can be:
#   {ls_number}
#   {ls_number},{erlass_date_ddmmyyyy},{inkraft_date_ddmmyyyy},{band}

def _parse_zhlex_legacy(url: str, parsed_url) -> ParsedDocumentUrl:
    qs = parse_qs(parsed_url.query, keep_blank_values=True)
    ordnr_raw = qs.get("Ordnr", [None])[0]

    if ordnr_raw is None:
        raise UnsupportedUrlError(f"ZH-Lex URL missing Ordnr parameter: {url}")

    parts = [p.strip() for p in ordnr_raw.split(",")]
    ls_number = parts[0]

    erlass_date = None
    inkraft_date = None
    band = None

    if len(parts) >= 4:
        erlass_date = _ddmmyyyy_to_iso(parts[1])
        inkraft_date = _ddmmyyyy_to_iso(parts[2])
        band = parts[3]

    # Use erlass_date as Work date; fallback to year-only placeholder
    work_date = erlass_date or "0000-01-01"
    version = inkraft_date  # best available version date for ZH-Lex

    warnings = []
    notes = [
        "ZH-Lex does not implement ELI-conformant URIs. The Ordnr is the LS citation number.",
        "ZH-Lex is German-language only; 'deu' is implicit.",
    ]
    if band:
        notes.append(
            f"Band number '{band}' is a sequential update counter, not a date. "
            f"Using Inkraftsetzungsdatum as @version if available."
        )
    if work_date == "0000-01-01":
        warnings.append(
            "No Erlassdatum in URL — Work date is unknown. "
            "Fetch the page to extract Erlassdatum from metadata."
        )

    return ParsedDocumentUrl(
        jurisdiction="ch-zh",
        doc_type="act",
        date=work_date,
        number=ls_number,
        lang="de",
        version=version,
        platform="zh-lex",
        source_uri=url,
        ls_number=ls_number,
        band_number=band,
        inkraft_date=inkraft_date,
        erlass_date=erlass_date,
        warnings=warnings,
        notes=notes,
    )


# ── ZH.ch portal parser ───────────────────────────────────────────────────────
#
# Path: …/zhlex-ls/erlass-{ordnr_encoded}-{erlass_date_encoded}-{inkraft_date_encoded}-{band}.html
# Encoding: dots→underscore, date components joined with underscore

_ZHCH_PORTAL_RE = re.compile(
    r"erlass-([0-9_]+)-(\d{4}_\d{2}_\d{2})-(\d{4}_\d{2}_\d{2})-(\d+)\.html"
)

def _parse_zhch_portal(url: str, path: str) -> ParsedDocumentUrl:
    m = _ZHCH_PORTAL_RE.search(path)
    if not m:
        raise UnsupportedUrlError(
            f"ZH.ch portal URL path not recognised: {path}\n"
            f"Expected pattern: …/erlass-{{ordnr}}-{{erlass_date}}-{{inkraft_date}}-{{band}}.html"
        )

    ordnr_enc, erlass_enc, inkraft_enc, band = m.groups()
    ls_number = ordnr_enc.replace("_", ".")
    erlass_date = erlass_enc.replace("_", "-")
    inkraft_date = inkraft_enc.replace("_", "-")

    return ParsedDocumentUrl(
        jurisdiction="ch-zh",
        doc_type="act",
        date=erlass_date,
        number=ls_number,
        lang="de",
        version=inkraft_date,
        platform="zh-lex",
        source_uri=url,
        ls_number=ls_number,
        band_number=band,
        inkraft_date=inkraft_date,
        erlass_date=erlass_date,
        warnings=[],
        notes=[
            "ZH.ch portal URL parsed (not a stable citation link — zhlex.zh.ch links preferred).",
            "ZH-Lex is German-language only; 'deu' is implicit.",
        ],
    )
