# Blueprint

This document defines the major architecture of the GitHub workflow generating, with a strong focus on `input/`. It is intended as a reusable blueprint for workflow design, onboarding, and quality checks.

## 1) High-level architecture

`ech-*` uses a source-to-generated pattern:

- `input/` = authoritative source of truth (human-maintained)
- `output/` = generated artifacts (machine-maintained)
- `misc/` = references, notes, and project support material not part of the pipeline.

Design rule:

- Edit only `input/` - Never hand-edit generated files in `output/`.

## 2) Input architecture (core blueprint)

`input/` is split into schema, example data, localization chapters, and rendering config.

### 2.1 Canonical schema layer

- `input/schema.yaml`
  - Canonical LinkML schema for eCH-0294 Actors.
  - Defines classes, slots, enums, constraints, and multilingual annotations.
  - Imports shared cross-standard elements from eCH-0292 meta schema.

- Root container class: `Container` (tree root)
- Constraint patterns:
  - `required` slot usage for mandatory fields
  - `any_of` blocks for alternative required conditions
  - mixins for reusable metadata (identification, temporal validity, creation/modification)

### 2.2 Example data layer

- `input/data_*.yaml`
  - Example instance datasets that must validate against `schema.yaml`.
  - Used for conversion outputs (JSON, RDF/Turtle) and doc examples.

Data contract:

- Top-level payload follows `Container`-style collections 
- Temporal semantics are explicit where needed (`valid_from`, `valid_through`, `is_active`).

### 2.3 Documentation chapter layer (localized narrative)

- `input/de/*.md`
- `input/fr/*.md`
- `input/en/*.md`

Purpose:

- Hand-authored narrative chapters (head, intro, class sections, shared elements).
- Merged with generated schema docs during pipeline execution.

Chapter naming pattern:

- Ordered numeric prefixes (`01_...`, `02_...`, ...), ensuring deterministic merge order.

### 2.4 Example extraction configuration

- `input/pipeline_examples_generator_config.yaml`

Purpose:

- Declares which classes and slots should receive extracted examples in generated documentation.
- Controls max example counts per slot.

### 2.5 Document rendering assets

- `input/template.docx`

Purpose:

- Reference template for final DOCX rendering via Pandoc.

## 3) Output architecture (generated)

`output/` is entirely generated from `input/` and workflow scripts.

Main artifact groups:

- Schema exports:
  - `output/schema.json`
  - `output/schema.ttl`
- Converted data examples:
  - `output/data_*.json`
  - `output/data_*.ttl`
- Generated documentation:
  - `output/docs/{de,fr,en}/...`
  - `output/documentation_merged_{de,fr,en}.md`
  - `output/ech-0294_actors_{de,fr,en}.docx`
  - `output/ech-0294_actors_{de,fr,en}.pdf`

## 4) Workflow blueprint (automation contract)

The GitHub Actions pipeline for eCH-0294 is triggered on changes under `ech-0294_actors/input/**`.

Canonical sequence:

1. Clean and prepare `output/`
2. Generate schema artifacts from `input/schema.yaml`
3. Convert each `input/data_*.yaml` to JSON and RDF/Turtle
4. Extract examples using `pipeline_examples_generator_config.yaml`
5. Generate localized docs (`de`, `fr`, `en`)
6. Merge docs and render DOCX/PDF
7. Commit changed generated files in `output/`

## 5) Reusable definition for future standards

Use this as a template for other eCH modules:

- Keep one canonical schema file in `input/`.
- Keep all source examples as `data_*.yaml` in `input/`.
- Separate human narrative chapters by language in `input/{lang}/`.
- Keep a dedicated example-extraction config in `input/`.
- Treat `output/` as disposable/regenerable build artifacts.
- Trigger CI only from `input/**` changes.

## 6) Governance rules

- Source of truth: `input/`
- Generated truth: `output/`
- No manual edits to generated files
- Schema changes must be accompanied by updated example data
- Narrative chapter changes should preserve chapter order and language parity

## 7) Minimal quality checklist

Before merging `input/` changes:

1. `schema.yaml` still models `Person`, `Group`, `Membership`, `InterestLink` consistently.
2. Every `data_*.yaml` remains schema-conformant.
3. Example extraction config references existing classes/slots.
4. Localized chapter sets (`de/fr/en`) remain complete enough for merge.
5. Workflow regenerates `output/` without manual fixes.
