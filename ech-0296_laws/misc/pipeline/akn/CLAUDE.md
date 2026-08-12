# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AKN-CH Pipeline: Converts Swiss legal document URLs (Fedlex, ZH-Lex) into Akoma Ntoso 3.0 FRBR URIs with fragment identifiers, human-readable citations, and a Svelte-based annotation UI.

## Commands

### Start the API (FastAPI)
```bash
cd akn-pipeline
PYTHONPATH=packages uvicorn api.main:app --reload --port 8787
```

### Start the UI (Svelte + Vite)
```bash
cd akn-pipeline/ui
npm run dev
# → http://localhost:5173 (proxies /api to :8787)
```

### Run all tests
```bash
cd akn-pipeline
PYTHONPATH=packages pytest api/tests/ packages/frbr_uri/tests/ -v
```

### Run a single test file
```bash
PYTHONPATH=packages pytest packages/frbr_uri/tests/test_resolver.py -v
```

### Run a single test by name
```bash
PYTHONPATH=packages pytest packages/frbr_uri/tests/test_resolver.py -v -k "test_name"
```

### Annotate AKN XML (visualize structure)
```bash
# From local file
python tools/akn_annotate.py document.xml

# From Fedlex URL
python tools/akn_annotate.py "https://fedlex.data.admin.ch/filestore/.../de/xml/..." -o

# -o flag opens result in browser
```

## Test Samples

Test XML files are stored in `tests/`. Always name samples after the original file:

```
tests/BBl-2025-2900-DE.xml    # Bundesblatt 2025 2900 German
tests/SR-220-DE.xml           # Obligationenrecht German
```

To test the annotator:
```bash
python tools/akn_annotate.py tests/BBl-2025-2900-DE.xml -o
```

## Architecture

### Core Library: `packages/frbr_uri/`

- **resolver.py** — `FRBRResolver`: Loads jurisdiction profiles (JSON) and builds Work/Expression/Manifestation/Item URIs
- **fragment.py** — `FragmentRef`, `SubdivisionRef`: AKN eId building, compact syntax (`#a47-p2-lit-a`), human citations, jurisdiction resolution
- **ranges.py** — `RangeRef`, `MultiSelectionRef`, `SelectionState`: Contiguous ranges (`#a7~a18`) and discrete multi-selections (`#a7,a11,a28`)
- **reference.py** — `LegalReferenceBuilder`, `LegalReference`: High-level API combining URL parsing, fragment building, and metadata fetching
- **parsers/url_parser.py** — Parses Fedlex (`fedlex.admin.ch`) and ZH-Lex (`zhlex.zh.ch`, `zh.ch`) URLs into `ParsedDocumentUrl`
- **parsers/page_fetcher.py** — HTTP fetch for metadata extraction (titles, SR numbers, dates)
- **profiles/*.json** — Jurisdiction profiles defining URI templates, document types, language codes

### REST API: `api/main.py`

FastAPI endpoints:
- `GET/POST /resolve` — URL → full AKN reference with URIs + fragment + citation
- `POST /fragment` — Build fragment from subdivision inputs
- `GET /fragment/parse` — Parse any fragment format (eId, compact, human DE/FR)
- `POST /selection` — Parse ranges and multi-selections
- `GET /jurisdiction` — Resolve shorthand (ZH, 261) to canonical ID (ch-zh, ch-zh-261)

### Frontend: `ui/`

Svelte 5 + Vite with ProseMirror (legal text editor) and CodeMirror (AKN XML source).

Key files:
- `src/stores.js` — Svelte stores bridging editors to API state
- `src/prosemirror.js` — PM schema with legal document nodes (article, paragraph, litera) and cross-reference marks

## Key Concepts

### FRBR Levels
```
Work:          /akn/ch-zh/lei/2024-01-15/170-4
Expression:    /akn/ch-zh/lei/2024-01-15/170-4/deu@2024-01-15
Manifestation: /akn/ch-zh/lei/2024-01-15/170-4/deu@2024-01-15.xml
```

### Fragment Syntax
| Format | Example |
|--------|---------|
| AKN eId | `art_47.para_2.lit_a` |
| Compact | `#a47-p2-lit-a` |
| Human DE | `Art. 47 Abs. 2 lit. a` |
| Range | `#a7~a18` or `#a7_p2~a8_p2` |
| Multi | `#a7,a11,a28` |

Range endpoints use `_` as level separator (not `-`) to avoid ambiguity.

### Jurisdiction IDs
- Federal: `ch`
- Canton: `ch-zh`, `ch-zg`, `ch-vd`
- Municipality: `ch-zh-261` (BFS number)

### Document Pointer Priority
1. Short title: `OR`, `DSG`, `BV`
2. SR/LS number: `SR 220`, `LS 170.41`
3. AS number: `AS 2022/491`
4. Composed: `ch-zh-261/2023/5`

## Adding a New Jurisdiction Profile

Create `packages/frbr_uri/profiles/{jurisdiction-id}.json` following `profile.schema.json`. Required fields: `jurisdiction`, `akn_prefix`, `language_codes`, `default_language`, `document_types`, `uri_templates`.

## Dependencies

Python: fastapi, uvicorn, requests, beautifulsoup4, pydantic, pytest, lxml

UI: svelte, vite, prosemirror-*, codemirror, @codemirror/lang-xml
