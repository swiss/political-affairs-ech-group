"""
frbr_uri/reference.py
tags: akn, reference, builder

High-level LegalReference builder — the single API the Svelte frontend calls.

Given a source URL (Fedlex / ZH-Lex) and optional subdivision inputs,
produces a fully resolved LegalReference with:
  - FRBRUris (Work / Expression / Manifestation / Item)
  - DocumentPointer (short title or SR number)
  - FragmentRef (article, paragraph, litera, etc.)
  - Full fragment URI and human-readable citation
  - Optionally: fetched page metadata (title, dates, status)

Usage:
    from frbr_uri.reference import LegalReferenceBuilder

    builder = LegalReferenceBuilder()
    ref = builder.from_url(
        "https://www.fedlex.admin.ch/eli/cc/1999/404/de",
        article="47", paragraph="2", litera="a",
        fetch=True
    )
    print(ref.fragment_uri)
    # /akn/ch/lei/1999-01-01/404/deu@1999-01-01#art_47.para_2.lit_a
    print(ref.human_citation("de"))
    # BV Art. 47 Abs. 2 lit. a
    print(ref.display_uri)
    # BV#art_47.para_2.lit_a
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .fragment import (
    FragmentRef, DocumentPointer, build_fragment,
    parse_fragment, resolve_jurisdiction
)
from .parsers.url_parser import parse_legal_url, ParsedDocumentUrl, UnsupportedUrlError
from .resolver import FRBRResolver, FRBRUris


_DEFAULT_RESOLVER = None

def _get_resolver() -> FRBRResolver:
    global _DEFAULT_RESOLVER
    if _DEFAULT_RESOLVER is None:
        _DEFAULT_RESOLVER = FRBRResolver()
    return _DEFAULT_RESOLVER


@dataclass
class LegalReference:
    """
    A complete, resolved reference to a point in Swiss legislation.
    """
    # Source
    source_url: str
    parsed_url: ParsedDocumentUrl

    # FRBR identifiers
    frbr_uris: Optional[FRBRUris] = None

    # Document pointer (short title / SR)
    document_pointer: DocumentPointer = field(
        default_factory=lambda: DocumentPointer()
    )

    # Subdivision fragment
    fragment: FragmentRef = field(default_factory=lambda: FragmentRef())

    # Fetched metadata (if fetch=True was requested)
    page_meta: Optional[object] = None  # FetchedMetadata

    # Resolution notes
    warnings: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    @property
    def fragment_uri(self) -> str:
        """
        Full AKN expression URI with fragment, e.g.:
        /akn/ch/lei/1999-01-01/404/deu@1999-01-01#art_47.para_2.lit_a
        """
        if not self.frbr_uris:
            return ""
        base = self.frbr_uris.expression
        if self.fragment.is_empty():
            return base
        return base + self.fragment.fragment()

    @property
    def work_fragment_uri(self) -> str:
        """Work-level URI with fragment (version-independent reference)."""
        if not self.frbr_uris:
            return ""
        base = self.frbr_uris.work
        if self.fragment.is_empty():
            return base
        return base + self.fragment.fragment()

    @property
    def display_uri(self) -> str:
        """
        Compact human-readable URI using the document pointer:
          OR#art_11.para_3   (if short title available)
          SR-220#art_11.para_3  (if SR number available)
          ch/1999/404#art_11    (fallback)
        """
        ptr = self.document_pointer.akn_pointer()
        if self.fragment.is_empty():
            return ptr
        return ptr + self.fragment.fragment()

    @property
    def eli_subdivision_uri(self) -> str:
        """
        ELI Subdivisions-style path URI (for API routing):
        /akn/ch/lei/1999-01-01/404/art_47/para_2/lit_a
        """
        if not self.frbr_uris:
            return ""
        return self.frbr_uris.work + self.fragment.eli_path() if not self.fragment.is_empty() else self.frbr_uris.work

    def human_citation(self, lang: str = "de") -> str:
        """
        Full human citation:
          BV Art. 47 Abs. 2 lit. a   (de)
          OR Art. 11 al. 3 let. b    (fr)
        """
        ptr_id = self.document_pointer.preferred_id()
        frag = self.fragment.human_readable(lang)
        if frag:
            return f"{ptr_id} {frag}"
        return ptr_id

    def as_dict(self) -> dict:
        d = {
            "source_url": self.source_url,
            "jurisdiction": self.parsed_url.jurisdiction,
            "doc_type": self.parsed_url.doc_type,
            "platform": self.parsed_url.platform,
            "document_pointer": {
                "short_title": self.document_pointer.short_title,
                "sr_number": self.document_pointer.sr_number,
                "preferred_id": self.document_pointer.preferred_id(),
                "akn_pointer": self.document_pointer.akn_pointer(),
            },
            "fragment": {
                "eid": self.fragment.eid() if not self.fragment.is_empty() else None,
                "fragment": self.fragment.fragment() if not self.fragment.is_empty() else None,
                "human_de": self.fragment.human_readable("de") if not self.fragment.is_empty() else None,
                "human_fr": self.fragment.human_readable("fr") if not self.fragment.is_empty() else None,
            },
            "uris": {
                "work": self.frbr_uris.work if self.frbr_uris else None,
                "expression": self.frbr_uris.expression if self.frbr_uris else None,
                "manifestation": self.frbr_uris.manifestation if self.frbr_uris else None,
                "fragment_uri": self.fragment_uri,
                "work_fragment_uri": self.work_fragment_uri,
                "display_uri": self.display_uri,
                "eli_subdivision_uri": self.eli_subdivision_uri,
            },
            "warnings": self.warnings,
            "notes": self.notes,
        }
        if self.page_meta:
            d["metadata"] = self.page_meta.to_dict()
        return d


class LegalReferenceBuilder:
    """
    High-level builder for LegalReference objects.

    The primary entry point for the Svelte frontend API endpoint.
    """

    def __init__(self, resolver: Optional[FRBRResolver] = None):
        self.resolver = resolver or _get_resolver()

    def from_url(
        self,
        url: str,
        *,
        # Subdivision inputs (all optional)
        chapter: Optional[str] = None,
        section: Optional[str] = None,
        article: Optional[str] = None,
        paragraph: Optional[str] = None,
        number: Optional[str] = None,
        litera: Optional[str] = None,
        sublitera: Optional[str] = None,
        # Metadata fetch
        fetch: bool = False,
        # Document pointer override
        short_title: Optional[str] = None,
        sr_number: Optional[str] = None,
    ) -> LegalReference:
        """
        Build a LegalReference from a source URL plus optional subdivision inputs.

        Args:
            url:        Source URL (Fedlex or ZH-Lex)
            chapter:    Kapitel number (optional)
            section:    Abschnitt number (optional)
            article:    Artikel number
            paragraph:  Absatz number
            number:     Ziffer (number in list)
            litera:     Buchstabe (letter in list)
            sublitera:  Doppelbuchstabe
            fetch:      If True, fetch the page for title/SR/dates
            short_title: Override for document short title (OR, DSG, ...)
            sr_number:  Override for SR/LS citation number
        """
        warnings: list[str] = []
        notes: list[str] = []

        # 1. Parse URL
        try:
            parsed = parse_legal_url(url)
        except UnsupportedUrlError as e:
            parsed = None
            warnings.append(str(e))

        if parsed is None:
            return LegalReference(
                source_url=url,
                parsed_url=ParsedDocumentUrl(
                    jurisdiction="ch", doc_type="act",
                    date="0000-01-01", number="unknown"
                ),
                warnings=warnings,
            )

        warnings.extend(parsed.warnings)
        notes.extend(parsed.notes)

        # 2. Resolve FRBR URIs
        frbr_uris = None
        try:
            kwargs = parsed.to_resolver_kwargs()
            frbr_uris = self.resolver.resolve(**kwargs)
        except Exception as e:
            warnings.append(f"FRBR resolution failed: {e}")

        # 3. Fetch page metadata if requested
        page_meta = None
        if fetch:
            try:
                from .parsers.page_fetcher import fetch_metadata
                page_meta = fetch_metadata(url)
                warnings.extend(page_meta.warnings)
                # Use fetched data to fill gaps
                if not short_title and page_meta.short_title:
                    short_title = page_meta.short_title
                if not sr_number and page_meta.sr_number:
                    sr_number = page_meta.sr_number
            except Exception as e:
                warnings.append(f"Page fetch failed: {e}")

        # 4. Build DocumentPointer (F8: short title > SR > AS > fallback)
        doc_ptr = DocumentPointer(
            short_title=short_title,
            sr_number=sr_number or parsed.ls_number,
            as_number=parsed.pub_number,
            jurisdiction=parsed.jurisdiction,
            year=parsed.pub_year,
            seq=parsed.pub_number,
        )

        # 5. Build fragment
        fragment = build_fragment(
            chapter=chapter,
            section=section,
            article=article,
            paragraph=paragraph,
            number=number,
            litera=litera,
            sublitera=sublitera,
        )

        return LegalReference(
            source_url=url,
            parsed_url=parsed,
            frbr_uris=frbr_uris,
            document_pointer=doc_ptr,
            fragment=fragment,
            page_meta=page_meta,
            warnings=warnings,
            notes=notes,
        )

    def from_shorthand(
        self,
        jurisdiction: str = "",
        short_title: Optional[str] = None,
        sr_number: Optional[str] = None,
        as_number: Optional[str] = None,
        year: Optional[str] = None,
        number: Optional[str] = None,
        *,
        article: Optional[str] = None,
        paragraph: Optional[str] = None,
        litera: Optional[str] = None,
        chapter: Optional[str] = None,
        section: Optional[str] = None,
        num: Optional[str] = None,
    ) -> LegalReference:
        """
        Build a LegalReference from structured inputs without a source URL.

        jurisdiction: "ch", "ZH", "261", "ch-zh", "ch-zh-261" (or empty → "ch")
        short_title:  "OR", "DSG", "ZGB"
        sr_number:    "220", "235.1", "170.41"
        year + number: for AS/OS-style references
        """
        jid = resolve_jurisdiction(jurisdiction)

        doc_ptr = DocumentPointer(
            short_title=short_title,
            sr_number=sr_number,
            as_number=as_number,
            jurisdiction=jid,
            year=year,
            seq=number,
        )

        fragment = build_fragment(
            chapter=chapter,
            section=section,
            article=article,
            paragraph=paragraph,
            number=num,
            litera=litera,
        )

        # Minimal parsed stub
        parsed = ParsedDocumentUrl(
            jurisdiction=jid,
            doc_type="act",
            date=f"{year}-01-01" if year else "0000-01-01",
            number=sr_number or as_number or number or "unknown",
        )

        return LegalReference(
            source_url="",
            parsed_url=parsed,
            document_pointer=doc_ptr,
            fragment=fragment,
            notes=[
                "Built from structured inputs (no source URL). "
                "FRBR URIs not fully resolved without a parsed URL."
            ],
        )
