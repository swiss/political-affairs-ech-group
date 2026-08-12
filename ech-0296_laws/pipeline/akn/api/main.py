"""
api/main.py
tags: fastapi, akn, api

AKN Pipeline REST API
=====================

Endpoints:

  POST /resolve           URL → FRBRUris + fragment + human citation
  GET  /resolve           Same via query params (convenient for browser/Svelte)
  POST /fragment          Build fragment from subdivision inputs
  GET  /fragment/parse    Parse compact (#a47-p2-lit-a) or human (Art. 47 Abs. 2) string
  GET  /jurisdiction      Resolve jurisdiction shorthand (ZH, 261, ch-zh-261)
  GET  /health            Health check

Run:
  cd akn-pipeline
  PYTHONPATH=packages uvicorn api.main:app --reload --port 8787

OpenAPI docs:  http://localhost:8787/docs
Redoc:         http://localhost:8787/redoc
"""

from __future__ import annotations

import sys
from pathlib import Path

# Allow running from the akn-pipeline directory with PYTHONPATH=packages
sys.path.insert(0, str(Path(__file__).parent.parent / "packages"))

from typing import Optional

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from frbr_uri.reference import LegalReferenceBuilder
from frbr_uri.fragment import (
    build_fragment, parse_fragment, parse_compact_fragment,
    compact_fragment, resolve_jurisdiction, FragmentRef,
)
from frbr_uri.parsers.url_parser import parse_legal_url, UnsupportedUrlError
from frbr_uri.resolver import FRBRResolver


# ── App setup ─────────────────────────────────────────────────────────────────

app = FastAPI(
    title="AKN Pipeline API",
    description=(
        "Resolves Swiss legal document URLs (Fedlex, ZH-Lex) to AKN/FRBR URIs, "
        "builds fragment identifiers for subdivisions (Art. / Abs. / lit.), "
        "and produces human-readable citations in DE/FR/IT."
    ),
    version="0.1.0",
    license_info={"name": "MIT"},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # tighten in production
    allow_methods=["*"],
    allow_headers=["*"],
)

_builder = LegalReferenceBuilder()
_resolver = FRBRResolver()


# ── Pydantic models ───────────────────────────────────────────────────────────

class SubdivisionInput(BaseModel):
    chapter:    Optional[str] = Field(None, example="3",   description="Kapitel / Chapitre")
    section:    Optional[str] = Field(None, example="2",   description="Abschnitt / Section")
    article:    Optional[str] = Field(None, example="47",  description="Artikel / Article")
    paragraph:  Optional[str] = Field(None, example="2",   description="Absatz / Alinéa")
    number:     Optional[str] = Field(None, example="3",   description="Ziffer / Chiffre")
    litera:     Optional[str] = Field(None, example="a",   description="Buchstabe / Lettre")
    sublitera:  Optional[str] = Field(None, example="aa",  description="Doppelbuchstabe")
    annex:      Optional[str] = Field(None, example="2",   description="Anhang / Annexe")


class ResolveRequest(BaseModel):
    url: str = Field(
        ...,
        example="https://www.fedlex.admin.ch/eli/cc/1999/404/20210307/de",
        description="Source URL from Fedlex or ZH-Lex"
    )
    subdivision: SubdivisionInput = Field(default_factory=SubdivisionInput)
    short_title: Optional[str] = Field(None, example="BV")
    sr_number:   Optional[str] = Field(None, example="101")
    fetch:       bool = Field(False, description="Fetch the page for title/SR/dates")
    lang:        str  = Field("de",  description="Language for human citation: de/fr/it")


class FragmentBuildRequest(BaseModel):
    subdivision: SubdivisionInput
    lang: str = Field("de", description="Language for human_readable label")


class FragmentResponse(BaseModel):
    eid:          str
    fragment:     str
    compact:      str
    human_de:     str
    human_fr:     str
    human_it:     str
    eli_path:     str


class DocumentPointerResponse(BaseModel):
    short_title:  Optional[str]
    sr_number:    Optional[str]
    preferred_id: str
    akn_pointer:  str


class URIsResponse(BaseModel):
    work:               Optional[str]
    expression:         Optional[str]
    manifestation:      Optional[str]
    fragment_uri:       str
    work_fragment_uri:  str
    display_uri:        str
    eli_subdivision_uri: str


class ParsedURLResponse(BaseModel):
    jurisdiction:  str
    doc_type:      str
    date:          str
    number:        str
    lang:          Optional[str]
    version:       Optional[str]
    platform:      str
    source_uri:    str
    ls_number:     Optional[str]
    pub_year:      Optional[str]
    pub_number:    Optional[str]
    warnings:      list[str]
    notes:         list[str]


class MetadataResponse(BaseModel):
    title_de:           Optional[str]
    title_fr:           Optional[str]
    title_it:           Optional[str]
    short_title:        Optional[str]
    sr_number:          Optional[str]
    enactment_date:     Optional[str]
    entry_into_force:   Optional[str]
    repeal_date:        Optional[str]
    consolidation_date: Optional[str]
    status:             str


class ResolveResponse(BaseModel):
    parsed_url:       ParsedURLResponse
    document_pointer: DocumentPointerResponse
    fragment:         Optional[FragmentResponse]
    uris:             URIsResponse
    human_citation:   str
    metadata:         Optional[MetadataResponse]
    warnings:         list[str]
    notes:            list[str]


# ── Helpers ───────────────────────────────────────────────────────────────────

def _fragment_response(frag: FragmentRef) -> Optional[FragmentResponse]:
    if frag.is_empty():
        return None
    return FragmentResponse(
        eid=frag.eid(),
        fragment=frag.fragment(),
        compact=compact_fragment(frag),
        human_de=frag.human_readable("de"),
        human_fr=frag.human_readable("fr"),
        human_it=frag.human_readable("it"),
        eli_path=frag.eli_path(),
    )


def _build_resolve_response(ref, lang: str) -> ResolveResponse:
    p = ref.parsed_url
    ptr = ref.document_pointer
    uris = ref.frbr_uris

    meta = None
    if ref.page_meta:
        m = ref.page_meta
        meta = MetadataResponse(
            title_de=m.title_de,
            title_fr=m.title_fr,
            title_it=m.title_it,
            short_title=m.short_title,
            sr_number=m.sr_number,
            enactment_date=m.enactment_date,
            entry_into_force=m.entry_into_force,
            repeal_date=m.repeal_date,
            consolidation_date=m.consolidation_date,
            status=m.status,
        )

    return ResolveResponse(
        parsed_url=ParsedURLResponse(
            jurisdiction=p.jurisdiction,
            doc_type=p.doc_type,
            date=p.date,
            number=p.number,
            lang=p.lang,
            version=p.version,
            platform=p.platform,
            source_uri=p.source_uri,
            ls_number=getattr(p, "ls_number", None),
            pub_year=getattr(p, "pub_year", None),
            pub_number=getattr(p, "pub_number", None),
            warnings=p.warnings,
            notes=p.notes,
        ),
        document_pointer=DocumentPointerResponse(
            short_title=ptr.short_title,
            sr_number=ptr.sr_number,
            preferred_id=ptr.preferred_id(),
            akn_pointer=ptr.akn_pointer(),
        ),
        fragment=_fragment_response(ref.fragment),
        uris=URIsResponse(
            work=uris.work if uris else None,
            expression=uris.expression if uris else None,
            manifestation=uris.manifestation if uris else None,
            fragment_uri=ref.fragment_uri,
            work_fragment_uri=ref.work_fragment_uri,
            display_uri=ref.display_uri,
            eli_subdivision_uri=ref.eli_subdivision_uri,
        ),
        human_citation=ref.human_citation(lang),
        metadata=meta,
        warnings=ref.warnings,
        notes=ref.notes,
    )


# ── Endpoints ─────────────────────────────────────────────────────────────────

@app.get("/health")
def health():
    """Health check."""
    return {"status": "ok", "version": "0.1.0"}


@app.post("/resolve", response_model=ResolveResponse, summary="Resolve a legal document URL")
def resolve_post(body: ResolveRequest):
    """
    Resolve a Fedlex or ZH-Lex URL to AKN/FRBR URIs.

    Optionally include subdivision inputs (article, paragraph, litera, etc.)
    to generate a fragment identifier and human-readable citation.

    Set `fetch: true` to also retrieve the page title, short title, SR number,
    and dates from the source website.
    """
    ref = _builder.from_url(
        body.url,
        chapter=body.subdivision.chapter,
        section=body.subdivision.section,
        article=body.subdivision.article,
        paragraph=body.subdivision.paragraph,
        number=body.subdivision.number,
        litera=body.subdivision.litera,
        sublitera=body.subdivision.sublitera,
        short_title=body.short_title,
        sr_number=body.sr_number,
        fetch=body.fetch,
    )
    return _build_resolve_response(ref, body.lang)


@app.get("/resolve", response_model=ResolveResponse, summary="Resolve via query params")
def resolve_get(
    url: str = Query(..., description="Fedlex or ZH-Lex URL"),
    article:   Optional[str] = Query(None),
    paragraph: Optional[str] = Query(None),
    litera:    Optional[str] = Query(None),
    number:    Optional[str] = Query(None),
    chapter:   Optional[str] = Query(None),
    section:   Optional[str] = Query(None),
    short_title: Optional[str] = Query(None),
    sr_number:   Optional[str] = Query(None),
    fetch:     bool = Query(False),
    lang:      str  = Query("de"),
):
    """
    GET version of /resolve — convenient for browser/Svelte live preview.

    Example:
      GET /resolve?url=https://www.fedlex.admin.ch/eli/cc/1999/404/20210307/de
                  &article=47&paragraph=2&litera=a&short_title=BV&lang=de
    """
    ref = _builder.from_url(
        url,
        chapter=chapter, section=section,
        article=article, paragraph=paragraph,
        number=number, litera=litera,
        short_title=short_title, sr_number=sr_number,
        fetch=fetch,
    )
    return _build_resolve_response(ref, lang)


@app.post("/fragment", response_model=FragmentResponse, summary="Build a fragment from subdivision inputs")
def fragment_build(body: FragmentBuildRequest):
    """
    Build a fragment identifier from structured subdivision inputs.

    Returns AKN eId, compact display (#a47-p2-lit-a), human labels, and ELI path.
    Use this endpoint when you have subdivision inputs but no source URL.
    """
    frag = build_fragment(
        chapter=body.subdivision.chapter,
        section=body.subdivision.section,
        article=body.subdivision.article,
        paragraph=body.subdivision.paragraph,
        number=body.subdivision.number,
        litera=body.subdivision.litera,
        sublitera=body.subdivision.sublitera,
        annex=body.subdivision.annex,
    )
    if frag.is_empty():
        raise HTTPException(status_code=422, detail="No subdivision inputs provided.")
    return _fragment_response(frag)


@app.get("/fragment/parse", response_model=FragmentResponse, summary="Parse a fragment string")
def fragment_parse(
    q: str = Query(
        ...,
        description=(
            "Fragment string to parse. Accepts: "
            "AKN eId (art_47.para_2.lit_a), "
            "compact (#a47-p2-lit-a), "
            "human DE (Art. 47 Abs. 2 lit. a), "
            "human FR (Art. 47 Al. 2 let. a)"
        ),
        example="#a47-p2-lit-a",
    )
):
    """
    Parse any fragment string format into a normalised FragmentResponse.

    Accepts all four formats:
    - AKN eId:  `art_47.para_2.lit_a`
    - Compact:  `#a47-p2-lit-a`
    - Human DE: `Art. 47 Abs. 2 lit. a`
    - Human FR: `Art. 47 Al. 2 let. a`
    """
    # Try compact first (contains only compact prefixes + numbers/letters)
    import re
    stripped = q.strip().lstrip("#")
    is_compact = bool(re.match(r"^[a-z]+[\d\-]", stripped)) and "_" not in stripped

    if is_compact:
        frag = parse_compact_fragment(q)
    else:
        frag = parse_fragment(q)

    if frag.is_empty():
        raise HTTPException(status_code=422, detail=f"Could not parse fragment: {q!r}")
    return _fragment_response(frag)


@app.get("/jurisdiction", summary="Resolve a jurisdiction shorthand")
def jurisdiction_resolve(
    q: str = Query(
        ...,
        description="Shorthand: 'ch', 'ZH', 'ZG', '261', '1702', 'ch-zh-261', …",
        example="261",
    )
):
    """
    Resolve a jurisdiction shorthand to a canonical AKN jurisdiction id.

    - Empty / 'ch'     → 'ch'   (federal)
    - Canton code 'ZH' → 'ch-zh'
    - BFS number '261' → 'ch-zh-261'
    - Full 'ch-zh-261' → 'ch-zh-261'  (passthrough)
    """
    try:
        jid = resolve_jurisdiction(q)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    return {"input": q, "jurisdiction": jid}


@app.get("/parse-url", response_model=ParsedURLResponse, summary="Parse a legal document URL")
def parse_url(
    url: str = Query(..., description="Fedlex or ZH-Lex URL to parse")
):
    """
    Parse a Swiss legal document URL into its components without full FRBR resolution.
    Useful for quick inspection of what the pipeline extracts from a URL.
    """
    try:
        parsed = parse_legal_url(url)
    except UnsupportedUrlError as e:
        raise HTTPException(status_code=422, detail=str(e))
    return ParsedURLResponse(
        jurisdiction=parsed.jurisdiction,
        doc_type=parsed.doc_type,
        date=parsed.date,
        number=parsed.number,
        lang=parsed.lang,
        version=parsed.version,
        platform=parsed.platform,
        source_uri=parsed.source_uri,
        ls_number=getattr(parsed, "ls_number", None),
        pub_year=getattr(parsed, "pub_year", None),
        pub_number=getattr(parsed, "pub_number", None),
        warnings=parsed.warnings,
        notes=parsed.notes,
    )


# ── /selection endpoint (ranges + multi-selection) ────────────────────────────

from frbr_uri.ranges import parse_selection, compact_selection, human_selection, SelectionState


class SelectionRequest(BaseModel):
    raw: str = Field(
        ...,
        description=(
            "Selection string. Formats: "
            "single #a47-p2-lit-a | "
            "range #a7~a18 or #a7_p2~a8_p2 | "
            "multi #a7,a11,a28 | "
            "human Art. 47 Abs. 2"
        ),
        example="#a7~a18",
    )
    base_expression_uri: str = Field(
        "",
        description="Base AKN expression URI to append the selection to",
        example="/akn/ch/lei/1999-01-01/404/deu@2021-03-07",
    )
    document_pointer: str = Field("", example="BV")
    lang: str = Field("de")


class SelectionResponse(BaseModel):
    raw_input:        str
    selection_type:   str    # "single" | "range" | "multi"
    compact_display:  str
    human_de:         str
    human_fr:         str
    hash_uri:         str
    slash_uri:        str
    document_pointer: str
    errors:           list[str]


@app.post("/selection", response_model=SelectionResponse,
          summary="Parse a selection (single / range / multi) and build URIs")
def selection_parse(body: SelectionRequest):
    """
    Parse any selection string and return compact display, human label, and URIs.

    Supports:
    - **Single**: `#a47-p2-lit-a` — a single subdivision reference
    - **Range**: `#a7~a18` — a contiguous span (AKN portion reference)
    - **Multi**: `#a7,a11,a28` — discrete non-contiguous selections
    - **Human DE**: `Art. 47 Abs. 2 lit. a`

    Range endpoint syntax uses `_` as level separator: `#a7_p2~a8_p2`
    Multi uses `,` as separator: `#a7_p2,a11_lit-a`
    """
    from frbr_uri.ranges import FragmentRef, RangeRef, MultiSelectionRef

    state = SelectionState.from_raw(
        body.raw,
        base_expression_uri=body.base_expression_uri,
        document_pointer=body.document_pointer,
    )

    sel = state.selection
    if sel is None:
        sel_type = "error"
    elif isinstance(sel, RangeRef):
        sel_type = "range"
    elif isinstance(sel, MultiSelectionRef):
        sel_type = "multi"
    else:
        sel_type = "single"

    return SelectionResponse(
        raw_input=state.raw_input,
        selection_type=sel_type,
        compact_display=state.compact_display,
        human_de=state.human_de,
        human_fr=human_selection(sel, "fr") if sel else "",
        hash_uri=state.hash_uri,
        slash_uri=state.slash_uri,
        document_pointer=state.document_pointer,
        errors=state.errors,
    )
