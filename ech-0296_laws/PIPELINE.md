# PIPELINE

Documents the three `pipeline/` tools. Architecture, journal, and rationale detail live in the parent
infra monorepo's planning docs, not duplicated here.

## `pipeline/akn`

The AKN-side service/tooling, moved here from `web/fdlx.ch/akn-pipeline` (history preserved via `git mv`):
- `api/` — FastAPI resolver API (its URI-resolution logic now lives in `lib/uris/`, which this calls).
- `annotator/`, `ui/` — Svelte/Vite apps (annotation UI experiments —
  these two overlap and haven't been reconciled yet).
- `tools/akn_annotate.py` — the annotation-generation script.
- `template/{kav,ech}/` — Word document templates: `kav/` (Swiss federal legislative drafting templates,
  Word styles → AKN XML elements/attributes) and `ech/` (generic eCH standard-document templates).
- `package.json`/`package-lock.json` — the Recogito + CETEIcean + pdf.js + Solid-OIDC annotation stack
  (`@recogito/pdf-annotator`, `@recogito/text-annotator-tei`, `CETEIcean`,
  `@inrupt/solid-client-authn-browser`) — design doc not included in this repo.
- Calls out to `services/morgana-xproc` for the actual Word→AKN-XML transformation (validated against the
  official AKN `.xsd` + fedlex `.sch`), orchestrated by an Airflow DAG (not yet built) for
  the full construction flow: `template.docx → Morgana XProc → raw AKN XML → inject metadata (pipeline/
  schema) → inject URIs (pipeline/uri) → final AKN document`.

No notebook here — this is a running service (FastAPI + Svelte apps), not a notebook-driven pipeline.

## `pipeline/uri`

Construction + resolution generator. Takes `spec/input/schema.yaml`'s URI-relevant slots +
`lib/uris/frbr_uri`'s per-jurisdiction profile JSON (`ch.json`, `ch-zh.json`, ...), generates/validates the
RFC 6570 URI construction templates, and keeps `lib/uris/`'s resolver config in sync — rather than the two
being hand-maintained separately.

How to run: `cd pipeline/uri && jupyter notebook uri.ipynb` (button-per-step).

## `pipeline/schema`

The ELI↔AKN crosswalk generator: SSSOM mappings, generated SKOS concept schemes, LinkML-derived
cardinality/range docs (matching the upstream eCH group's own `gen-doc` convention).
- `meta/` — vendored LinkML import dependency (`schema.yaml`+`schema_common.yml`, from
  `ech-0292_meta`/`ch.paf.link`): FRBR `Work`/`Expression`/`Manifestation` + shared mixins
  (`HasTemporalValidity`, `HasIdentification`, `MultilingualValue`, etc.).
- `mappings/eli-akn.sssom.tsv` — the **sole canonical** hand-curated/generated mapping file; everything
  else (the `spec/input/appendix/eli-akn-mapping.md` annex, `public/mappings/*`) is a derived export.
- `fedlex-sparql/` — live SPARQL exploration tooling (notebooks + a `.sparqlbook`) for querying the actual
  jolux/Fedlex LINDAS data, to check what maps to which ELI ontology term.
- `ontology-tutorial.md`, `linkml-tutorial/` — reference material for the ELI-ontology-mapping work (see
  the priority TODO: the authoritative ELI ontology Excel sheet, still pending from the user).

How to run: `cd pipeline/schema && jupyter notebook schema.ipynb` (button-per-step: load → validate →
generate → export).

## `services/morgana-xproc`

Not under `pipeline/` — a standalone XProc processing tool (Java/Saxon-based), hosted at the
infrastructure root matching the `services/dokieli`-style convention for shared, container-able tools.
Does the actual Word→AKN-XML transformation `pipeline/akn` calls out to.
