"""Den Crosswalk eines Standards aus seinem LinkML-Schema ziehen.

    python .github/workflows/scripts/export_mappings.py <ech-folder> [lang]

Liest die Mapping-Slots (`exact_mappings`, `close_mappings`, `narrow_mappings`,
`broad_mappings`, `related_mappings`) aus `<ech-folder>/input/schema.yaml` und
schreibt sie zweimal nach `<ech-folder>/output/mappings/`:

* `<name>.sssom.tsv` -- ein SSSOM-Mapping-Set (Simple Standard for Sharing
  Ontology Mappings). SSSOM ist selbst in LinkML definiert, weshalb sich die
  Mapping-Slots eines LinkML-Schemas ohne Umweg in dieses Austauschformat
  ueberfuehren lassen; `sssom`-Werkzeuge lesen die Datei direkt.
* `<name>.md` -- dieselben Zuordnungen als Tabelle, die ein Kapitel ueber
  `{{include:...}}` in das Word-Dokument holt.

Damit ist das Schema die einzige Quelle: Wer eine Klasse an ein Element eines
anderen Vokabulars bindet, aendert das Schema -- nicht zusaetzlich eine von Hand
gepflegte Zuordnungstabelle und einen Anhang.
"""
import sys
from pathlib import Path

import yaml

# LinkML-Mapping-Slot -> SSSOM-Praedikat. Die Reihenfolge ist die der
# Ausgabe: erst die exakten Entsprechungen, dann die schwaecheren.
PREDICATES = {
    "exact_mappings": "skos:exactMatch",
    "close_mappings": "skos:closeMatch",
    "narrow_mappings": "skos:narrowMatch",
    "broad_mappings": "skos:broadMatch",
    "related_mappings": "skos:relatedMatch",
}

# Womit eine Zeile begruendet ist. Die Zuordnungen entstehen beim Modellieren,
# nicht aus einem automatischen Abgleich zweier bestehender Vokabulare.
JUSTIFICATION = "semapv:ManualMappingCuration"

COLUMNS = ["subject_id", "predicate_id", "object_id", "mapping_justification",
           "subject_label", "object_label", "subject_type"]

# SSSOM-Typ und Bezeichnung je LinkML-Elementart, pro Dokumentsprache.
KINDS = {
    "classes": ("owl class", {"de": "Klasse", "fr": "Classe", "en": "Class"}),
    "slots": ("owl object property", {"de": "Slot", "fr": "Slot", "en": "Slot"}),
    "enums": ("skos concept scheme", {"de": "Enum", "fr": "Énumération", "en": "Enum"}),
    "types": ("owl class", {"de": "Typ", "fr": "Type", "en": "Type"}),
}

HEADINGS = {
    "de": ("Element in diesem Standard", "Art", "Beziehung", "Entspricht"),
    "fr": ("Élément de la présente norme", "Type", "Relation", "Correspond à"),
    "en": ("Element in this standard", "Kind", "Relation", "Corresponds to"),
}

# Ohne Eintrag im curie_map laesst sich eine SSSOM-Datei nicht aufloesen. Die
# Praefixe stammen aus dem Schema; die der Praedikate und Begruendungen kommen
# hier dazu, weil sie im Schema nicht deklariert sein muessen.
FIXED_PREFIXES = {
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "semapv": "https://w3id.org/semapv/vocab/",
    "owl": "http://www.w3.org/2002/07/owl#",
}


def collect(schema, lang):
    """Eine Zeile je Mapping, in der Reihenfolge des Schemas."""
    rows = []
    default_prefix = schema.get("default_prefix") or "this"
    for kind, (subject_type, labels) in KINDS.items():
        for name, defn in (schema.get(kind) or {}).items():
            for slot, predicate in PREDICATES.items():
                for target in (defn or {}).get(slot, []):
                    rows.append({
                        "subject_id": f"{default_prefix}:{name}",
                        "predicate_id": predicate,
                        "object_id": target,
                        "mapping_justification": JUSTIFICATION,
                        "subject_label": name,
                        "object_label": target.split(":", 1)[-1],
                        "subject_type": subject_type,
                        "_kind": labels.get(lang, labels["en"]),
                    })
    return rows


def write_sssom(rows, path, schema):
    prefixes = dict(FIXED_PREFIXES)
    prefixes.update({k: v for k, v in (schema.get("prefixes") or {}).items()
                     if not isinstance(v, dict)})
    with path.open("w", encoding="utf-8") as fh:
        fh.write("# curie_map:\n")
        for prefix, uri in sorted(prefixes.items()):
            fh.write(f"#   {prefix}: {uri}\n")
        fh.write("# license: https://creativecommons.org/publicdomain/zero/1.0/\n")
        fh.write(f"# mapping_set_id: {schema['id'].rstrip('/')}/mappings\n")
        fh.write("\t".join(COLUMNS) + "\n")
        for row in rows:
            fh.write("\t".join(row[c] for c in COLUMNS) + "\n")


def write_markdown(rows, path, lang):
    element, kind, relation, target = HEADINGS.get(lang, HEADINGS["en"])
    with path.open("w", encoding="utf-8") as fh:
        fh.write(f"| {element} | {kind} | {relation} | {target} |\n|---|---|---|---|\n")
        for row in rows:
            # Das Praedikat ohne Praefix: in der Tabelle zaehlt exactMatch vs.
            # closeMatch, der SKOS-Namensraum steht in der SSSOM-Datei.
            predicate = row["predicate_id"].split(":", 1)[-1]
            fh.write(f"| `{row['subject_label']}` | {row['_kind']} | {predicate} "
                     f"| `{row['object_id']}` |\n")


def main(folder, lang):
    schema_path = Path(folder) / "input" / "schema.yaml"
    with schema_path.open(encoding="utf-8") as fh:
        schema = yaml.safe_load(fh)

    rows = collect(schema, lang)
    out_dir = Path(folder) / "output" / "mappings"
    out_dir.mkdir(parents=True, exist_ok=True)

    name = Path(folder).name
    write_sssom(rows, out_dir / f"{name}.sssom.tsv", schema)
    write_markdown(rows, out_dir / f"{name}_{lang}.md", lang)
    print(f"export_mappings.py: {len(rows)} Zuordnungen -> {out_dir}/{name}.sssom.tsv, "
          f"{name}_{lang}.md")


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        print("Usage: python .github/workflows/scripts/export_mappings.py <ech-folder> [lang]")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2] if len(sys.argv) == 3 else "de")
