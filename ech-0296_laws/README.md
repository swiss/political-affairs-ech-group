# eCH-0296 – Erlasse und Gesetzestexte

Anwendungsprofile für **Akoma Ntoso** (AKN4CH / AKN-AP-CH) und den **European Legislation Identifier**
(ELI-AP-CH) für die Schweiz. Grundlage für die Publikation und den Austausch von Erlassen und
Gesetzestexten zwischen Bund, Kantonen und Gemeinden sowie mit dem Ausland.

| | |
|---|---|
| eCH-Nummer | 0296 |
| Kategorie | Standard |
| Reifegrad | Definiert |
| Version | 0.1.0 |
| Status | In Arbeit |
| Fachgruppe | Politische Geschäfte |
| Sprachen | Deutsch (Original), Französisch (Übersetzung) |
| Editor | Martin Gajdos ([martin.gajdos@me.com](mailto:martin.gajdos@me.com)) |

## Approach

Sources are re-derived from the official ELI and Akoma Ntoso specifications and rebuilt as a
**LinkML-native pipeline**: hand-authored source material in `spec/` feeds Python notebooks in
`pipeline/` that generate the SSSOM mapping set, the SKOS controlled vocabularies, and the URI
construction/resolution logic — rather than hand-maintaining a mapping document and a resolver
separately. See [`PIPELINE.md`](PIPELINE.md) for how each tool works and how to run it.

## Repository structure

```
spec/           the standard itself — sources + authored content
  input/
    main/       the 4 normative modules: identifier, content, metadata (+ intro, informative)
    appendix/   dependencies, references, tooling, and the generated ELI↔AKN mapping annex
    examples/   worked AKN/ELI examples (federal + cantonal)
    schemas/    vendored AKN 3.0 XSDs (OASIS + Fedlex-flavoured), Fedlex Schematron
  misc/         reference material: ELI (core/DL/I), AKN (NC, AKN4EU, AKN4CH), FRBR, the EU's
                ELI Annotation Tool, Schematron/XProc references, drafting-methodology sources
                (Bundeskanzlei guidelines, LeGes) — background reading, not normative

lib/            runtime libraries
  uris/         frbr_uri — FRBR-URI resolver, fragment identifiers, legacy-URL reverse-engineering
  metadata/     ELI property definitions
  data/         example AKN XML documents with ELI identifiers

pipeline/       the tooling that builds spec/'s generated artifacts (not itself normative)
  akn/          Word→AKN-XML construction: KAV/eCH Word templates, a FastAPI resolver API
                (calls into lib/uris/); the actual Word→XML transform runs through Morgana XProc,
                a separate tool not included in this repository
  uri/          FRBR/ELI URI-template construction + validation (uri.ipynb)
  schema/       the ELI↔AKN crosswalk: SSSOM mapping set, LinkML-generated SKOS vocabularies,
                live SPARQL tooling against Fedlex's jolux data (schema.ipynb, fedlex-sparql/)
```

## Roadmap

The three normative modules (**URI/identifier**, **metadata**, **content**) are each backed by a
`pipeline/` tool that generates the corresponding `spec/` artifact rather than hand-maintaining it:

- **URI** (`pipeline/uri`) — constructs and validates the RFC 6570 URI templates for Swiss legal
  resources (federal via Fedlex, cantonal/municipal where no ELI scheme exists yet), reusing
  `lib/uris/frbr_uri`'s per-jurisdiction resolver profiles.
- **Metadata** (`pipeline/schema`) — the ELI↔AKN crosswalk, generated with
  [**sssom-py**](https://github.com/mapping-commons/sssom-py) from `pipeline/schema/mappings/eli-akn.sssom.tsv`
  (the sole hand-curated mapping file — `spec/input/appendix/eli-akn-mapping.md` and the published
  vocabularies are derived exports, not edited directly). Local SKOS concept schemes (resource type,
  subdivision type, legal value, in-force status, …) are generated LinkML enum/CSV → SKOS, aligned to
  ELI/Eurovoc. `pipeline/schema/fedlex-sparql/` queries the live Fedlex SPARQL endpoint to pull the
  actual jolux metadata (concept schemes, vocabularies) that the mapping needs to check against.
- **Content** (`pipeline/akn`) — the AKN XML structure, bounded to what AKN Level-2 conformance
  requires (structure, FRBR URIs/IDs, metadata levels A–D), constructed from Word via Morgana XProc
  and validated against the official XSD + Fedlex Schematron.

Both the coverage of the crosswalk (mapped vs. unmapped, by conformance level A–D) and the vocabulary
coverage (defined locally / reused from ELI / aligned to Eurovoc / missing) are rendered as living
tables from `pipeline/schema/schema.ipynb`'s output — currently the substantive open work.

## Publication

The rendered standard (this content plus a generated coverage/mapping view) is published at
[legaldocml.ch](https://legaldocml.ch) under `/ap` (machine-readable JSON-LD alignment) and
`/application-profile` (the human-readable crosswalk) — generated from this same LinkML pipeline, with
Word-document export as an additional output alongside the site, matching this working group's own
`schema.yaml` → generated-`.docx` convention. That build tooling (an Astro site, deploy config) lives in
the parent infrastructure monorepo and isn't included in this repository.

## Standards in play

ELI Core + ELI-DL (draft legislation) + ELI implementation guidance · schema.org · Akoma Ntoso 3.0
(OASIS) + its Naming Convention (AKN-NC — AKN has no formal OWL ontology) · Eurovoc (subjects).

## License

CC-BY-4.0
