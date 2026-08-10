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

---

## Pipeline

Jeder Push auf `input/` löst den Workflow `.github/workflows/ech-0294.yaml` aus:

1. **Artefakte erzeugen** — `schema.yaml` wird zu OWL und JSON Schema kompiliert, die
   Datendateien nach JSON und RDF konvertiert.
2. **Beispiele schneiden** — `extract_examples.py` schreibt je Instanz eine Datei nach
   `output/examples/` und legt eine Schema-Kopie mit Slot-Beispielen an. Gesteuert wird
   das über `pipeline_examples_generator_config.yaml`, wo auch die sprechenden Titel der
   Beispiele stehen.
3. **Dokumentation erzeugen** — `gen-doc` rendert je Sprache die Seiten nach
   `output/docs/<lang>/`, mit den Beispielen aus Schritt 2.
4. **Zusammenführen** — `merge_documentation.py` setzt die verfassten Kapitel aus
   `input/<lang>/` und die generierten Seiten zu `documentation_merged_<lang>.md`
   zusammen; eingebunden werden sie über `{{include:…}}`-Direktiven.
5. **Word und PDF** — Pandoc erzeugt das DOCX gegen `template.docx`; anschliessend werden
   Fusszeile, Seitenzähler und Zeilenschattierung gesetzt, danach konvertiert LibreOffice
   das fertige Dokument samt Inhaltsverzeichnis ins PDF.

Die erzeugten Dateien werden automatisch zurück ins Repository committet.

**Release:** Der Workflow „Release ech-0294" wird von Hand mit einer frei gewählten
Versionsnummer gestartet. Er taggt den Stand als `ech-0294-v<version>` und hängt Word und
PDF je Sprache — benannt nach der Nomenklatur von eCH-0003 —, das Schema in allen drei
Formaten, die Beispieldaten und ein ZIP mit allem an ein GitHub Release.

---

## Lokal bauen

```bash
pip install -r requirements.txt

python .github/workflows/scripts/extract_examples.py ech-0294_actors
gen-doc ech-0294_actors/output/pipeline_examples_generator_schema.yaml \
  --directory ech-0294_actors/output/docs/de \
  --template-directory ech-0292_meta/input/docgen/de \
  --example-directory ech-0294_actors/output/examples
python .github/workflows/scripts/merge_documentation.py ech-0294_actors de
```

Für Französisch und Englisch dasselbe mit dem jeweiligen Sprachkürzel; für `fr` und `de`
schreibt vorher `localize_schema.py` die übersetzten Beschreibungen in eine Schema-Kopie.

Beispieldaten gegen das Schema prüfen:

```bash
linkml-validate -s ech-0294_actors/input/schema.yaml ech-0294_actors/input/data_memberships.yaml
```

---

## Weiterführend

- `docs/common/workflow.md` — die Pipeline im Detail, für alle Standards der Fachgruppe
- `docs/common/linkml_guidelines.md` — Modellierungsregeln
- `docs/common/naming.md` — Benennung von Klassen, Slots und Enumerationen
- `docs/common/design_principles.md` — Grundsätze hinter dem Datenmodell
