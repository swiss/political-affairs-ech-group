# ech-0294 Actors

This sub-group defines political actors including persons, groups, memberships, and interest links.


---

## Folder Structure

```
ech-0294_actors/
├── input/                          # ✏️ Authoritative source definitions (edit here)
│   ├── schema.yaml                 # LinkML schema: classes, slots, and enumerations
│   └── data_*.yaml                 # Data files conforming to the schema
│
└── output/                         # ⚙️ Auto-generated — do not edit manually
    ├── schema.ttl                  # OWL ontology derived from schema.yaml
    ├── schema.json                 # JSON Schema derived from schema.yaml
    ├── data_*.json                 # Data files converted to JSON
    ├── data_*.ttl                  # Data files converted to RDF/Turtle
    ├── docs/                       # Per-class/enum Markdown pages (gen-doc output)
    ├── documentation_merged.md     # Single merged Markdown document
    └── ech-0294_actors.docx        # Final Word document (via Pandoc)
```

---

## How It Works

The pipeline is triggered automatically on every push to `input/` and runs the following steps:

1. **Generate artefacts** — `schema.yaml` is compiled into OWL (`.ttl`) and JSON Schema (`.json`); data files are converted to JSON and RDF.
2. **Extract examples** — examples are extracted from data files and placed in `output/examples/`.
3. **Generate documentation** — `gen-doc` produces per-class and per-enum Markdown pages in `output/docs/`.
4. **Merge documentation** — all pages are merged into a single `documentation_merged.md`.
5. **Convert to Word** — Pandoc converts the merged Markdown to `ech-0294_actors.docx` using `template.docx`.

All generated files are committed back to the repository automatically.
