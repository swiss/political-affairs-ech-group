# eCH-0294 Politische Akteure

Datenstandard für die Akteure des politischen Betriebs: **Personen**, **Gruppen und Organe**
(Parlamente, Regierungen, Kommissionen, Fraktionen, Parteien), ihre **Mitgliedschaften**
sowie die **Interessenbindungen** zu Organisationen ausserhalb dieses Schemas.

Massgeblich ist `input/schema.yaml` — eine LinkML-Definition, aus der alle weiteren
Artefakte erzeugt werden: JSON Schema, OWL/RDF, die Dokumentation und das Word-Dokument
in Deutsch, Französisch und Englisch.

---

## Ordnerstruktur

```
ech-0294_actors/
├── input/                                  # Quelle — hier wird bearbeitet
│   ├── schema.yaml                         # LinkML-Schema: Klassen, Slots, Enumerationen
│   ├── data_*.yaml                         # Beispieldaten (echte, publizierte Fälle)
│   ├── pipeline_examples_generator_config.yaml  # Welche Klassen/Slots Beispiele erhalten
│   ├── de/ fr/ en/                         # Verfasste Kapitel je Sprache (01_head.md …)
│   └── template.docx                       # Word-Vorlage (Formatvorlagen, Kopf-/Fusszeile)
│
└── output/                                 # Automatisch erzeugt — nicht von Hand ändern
    ├── schema.json                         # JSON Schema
    ├── schema.ttl                          # OWL-Ontologie
    ├── data_*.json / data_*.ttl            # Beispieldaten als JSON und RDF/Turtle
    ├── examples/                           # Aus den Daten geschnittene Einzelbeispiele
    ├── docs/{de,fr,en}/                    # Seite je Klasse, Slot, Enum (gen-doc)
    ├── documentation_merged_{de,fr,en}.md  # Verfasste Kapitel + generierte Doku
    ├── ech-0294_actors_{de,fr,en}.docx     # Word-Dokument je Sprache
    └── ech-0294_actors_{de,fr,en}.pdf      # PDF je Sprache
```

Die Beschreibungen im Schema werden dreisprachig geführt: Englisch in `description`,
Deutsch und Französisch in `annotations.description_de` / `description_fr`. Fehlt eine
Übersetzung, erscheint im übersetzten Dokument der englische Text.
