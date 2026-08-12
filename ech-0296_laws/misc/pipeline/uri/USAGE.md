# USAGE — pipeline/uri

How to actually run `uri.ipynb`, what it does, and the ELI/AKN conventions it's built on. Originally
extracted from the ELI Annotation Tool's own manual (`spec/misc/sources/ELI/ELI/eli-annotation-tool/
doc/user_manual/*.rst`) — moved here since it's this pipeline's own operating notes, not something
specific to that vendored tool.

## Running it

```bash
cd pipeline/uri
.venv/bin/jupyter lab uri.ipynb          # local, ad hoc
```

Or via the shared `py.mgajdo.ch` JupyterLab service (internal/WireGuard only) — see `services/jupyter/`
at the infra root. That server's root is `web/legaldocml.ch/`, so it shows every sibling pipeline
(`pipeline/akn`, `pipeline/schema`, `pipeline/uri`, and any future `pipeline/*`), not just this one.

`.venv` here has `pandas`, `jupyter`/`jupyterlab`, `pytest`, and the ELI Annotation Tool installed
**editable** from its vendored location:

```bash
.venv/bin/pip install -e ../../spec/misc/sources/ELI/ELI/eli-annotation-tool pandas jupyter jupyterlab pytest pyyaml
```

## What `uri.ipynb` does, section by section

- **§0 Setup** — imports both toolkits: `frbr_uri` (AKN side — resolver, legacy-URL parser, fragment/eId
  builder) and `eli_annotation` (ELI side — the Annotation Tool's real classes, not its web UI).
- **§1 Vocabulary definitions** — loads an Excel vocabulary as a `pandas` DataFrame for manual review/
  editing, then converts it to real SKOS RDF via `any2skos.xl2rdf` — the same converter the tool's own
  "Import vocabulary" button uses. See "Vocabulary conventions" below for the exact format.
- **§2 Construct URIs from `eli:` metadata** — drives `any2eli.build_uris_for_entities`, which internally
  uses `URIScheme.build_uri()` (see "URI scheme syntax" below) — the exact mechanism the web UI's admin
  form-config page uses.
- **§3 Legacy → citation → new AKN → new ELI** — the 4-column comparison table. ELI column is filled only
  for federal (Fedlex) sources, where the legacy URI already is a real ELI URI; left blank for cantonal
  sources, where no real ELI URI scheme has been designed yet (see `uri_components.yaml`'s `jurisdictions`
  section — that's the actual design task, not a gap to silently paper over).
- **§4 Export to `lib/uris/`** — stub, blocked on the cantonal ELI-URI design.
- **§5 Authoritative URI-component definitions** — loads `uri_components.yaml` (hand-edited source of
  truth) and generates `spec/input/appendix/uri-components.md`. Edit the YAML, re-run this section's
  cells; never hand-edit the generated `.md`.

## URI scheme syntax (the `{property|operator}` DSL)

Four chained URIs, each extending the previous by appending one or more path segments: **abstract legal
resource** → **legal resource** → **legal expression** (one per language) → **format** (one per
language × format).

**Property insertion**: `{eli:version}` — curly braces around the property name; the value is inserted
as-is (must already be well-formed for a URI).

**Date decomposition — the `|` operator**: extracts one component from a date-typed property instead of
the full `YYYY-MM-DD`:

```
{eli:date_publication|year}   -> YYYY   (e.g. 2017)
{eli:date_publication|month}  -> MM     (e.g. 11)
{eli:date_publication|day}    -> DD     (e.g. 23)
```

RFC 6570 has no native equivalent for this — worth keeping as a candidate building block if
`pipeline/uri` ever needs its own general-purpose template generator.

**Controlled-vocabulary values**: if a property's value is a SKOS concept, its `skos:notation` is what
gets inserted — not the concept URI, not `prefLabel`. **Every SKOS concept used in a URI scheme must
have a `skos:notation`**, enforced by the tool, not just a convention.

## Vocabulary conventions

Two accepted input formats:

- **SKOS RDF/XML or RDF/Turtle** — imported as-is.
- **Excel** — a header block (ConceptScheme metadata) ends and a body (one row per Concept) begins at
  the row where column A contains `Concept URI`. Columns are `dct:`-/`skos:`-/custom-prefixed property
  names. Full spec: `eli-annotation-tool/doc/user_manual/excel-vocab-specif.rst`. Real worked example:
  `eli-annotation-tool/tests/data/test00.xlsx` ("weekdays" — converts cleanly, verified live).

Four vocabularies ship pre-loaded in the tool's own `data/vocabs/`: languages, IANA media-types,
`eli:InForce-`, `eli:LegalValue-`.

The Excel↔SKOS round-trip (`any2skos.py convert`/`csv`) is a direct, already-working implementation of
the same "CSV/enum → SKOS" step `pipeline/schema/schema.ipynb`'s cell 3 is stubbed for — reuse it rather
than re-implementing, and it's the natural feed for wiring SSSOM (`sssom-py`) against vocabularies built
this way.

## Historical Fedlex URI eras (why `frbr_uri`'s parser isn't as simple as it looks)

Confirmed via `spec/URI_fedlex_template.md`: Fedlex's own URI scheme is **not** temporally uniform.
Three genuinely distinct historical shapes exist, not just formatting variants of the modern one:

- **1848–1947**: `{collection}/{volume}_{page-de}_{page-fr}_{page-it}` — no year at all; volume is a
  roman numeral in the earlier part of the range, revised to arabic at some point within it (exact
  cutover date not yet pinned down).
- **1948–1999** (OC/CC): `{year}/{page-de}_{page-fr}_{page-it}` — no separate volume field.
- **Pre-2000 FGA specifically**: `{year}/{volume}_{page-de}_{page-fr}_{page-it}` — per-language page
  numbers can be *empty* when only one language was scanned/aligned; the page number itself derives from
  Bundesarchiv scan order, not a semantic numbering.

`lib/uris/frbr_uri/parsers/url_parser.py` handles all three (fixed 2026-07-29).
Not yet handled: `historicaldossierID` suffix, the non-main-act `-{ordernumber}` suffix, and
cross-collection basic-act suffixes (`_{collection_basicact}`) — real, documented variants, out of scope
for that specific fix.
