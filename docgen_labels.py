#!/usr/bin/env python3
"""
docgen_labels.py

Regenerate the localized gen-doc template folders from the English source.
`ech-0292_meta/input/docgen/en/` is the single source of truth for the Jinja2
templates; this tool copies them into `.../de/` and `.../fr/` and replaces the
static English UI labels (headings, table headers, property-row names) with
their German / French equivalents. Element *descriptions* are NOT touched here —
those come from the per-language schema produced by localize_schema.py.

Run this whenever the English templates change, to keep all languages in sync.

Only labels that actually render for these schemas are translated; the long tail
of rarely-used LinkML labels is left English (harmless, and easy to extend via
the LABELS dict below).

Replacements are applied longest-key-first so multi-column headers are handled
before the bare single-cell labels they contain.
"""
import os
import shutil

DOCGEN = os.path.join("ech-0292_meta", "input", "docgen")

# English label -> {de, fr}. Keys are distinctive substrings from the templates.
LABELS = {
    # element titles (prefix incl. trailing space so only the heading matches)
    "## Class: ": {"de": "## Klasse: ", "fr": "## Classe: "},
    "# Type: ": {"de": "# Typ: ", "fr": "# Type: "},
    # section headings
    "### Type and Range": {"de": "### Typ und Wertebereich", "fr": "### Type et plage"},
    "### Cardinality and Requirements": {"de": "### Kardinalität und Anforderungen", "fr": "### Cardinalité et exigences"},
    "## Applicable Classes": {"de": "## Anwendbare Klassen", "fr": "## Classes applicables"},
    "## Type Properties": {"de": "## Typ-Eigenschaften", "fr": "## Propriétés du type"},
    "## LinkML Source": {"de": "## LinkML-Quelle", "fr": "## Source LinkML"},
    "## Properties": {"de": "## Eigenschaften", "fr": "## Propriétés"},
    "### Attribute": {"de": "### Attribute", "fr": "### Attributs"},
    "### Usages": {"de": "### Verwendungen", "fr": "### Utilisations"},
    "### Permissible Values": {"de": "### Zulässige Werte", "fr": "### Valeurs admissibles"},
    "### Mixin Usage": {"de": "### Mixin-Verwendung", "fr": "### Utilisation de mixin"},
    "### Value Constraints": {"de": "### Wertebeschränkungen", "fr": "### Contraintes de valeur"},
    "### Slot Characteristics": {"de": "### Slot-Eigenschaften", "fr": "### Caractéristiques du slot"},
    "### Enumeration Source": {"de": "### Quelle der Aufzählung", "fr": "### Source de l'énumération"},
    "#### Example: ": {"de": "#### Beispiel: ", "fr": "#### Exemple : "},
    "Inheritance: ": {"de": "Vererbung: ", "fr": "Héritage : "},
    "##### Constraints": {"de": "##### Einschränkungen", "fr": "##### Contraintes"},
    "##### Rules": {"de": "##### Regeln", "fr": "##### Règles"},
    "At least one of the following must be set:": {"de": "Mindestens eines der folgenden Felder muss gesetzt sein:", "fr": "Au moins l'un des champs suivants doit être renseigné :"},
    "Exactly one of the following must be set:": {"de": "Genau eines der folgenden Felder muss gesetzt sein:", "fr": "Exactement un des champs suivants doit être renseigné :"},
    "All of the following must be set:": {"de": "Alle folgenden Felder müssen gesetzt sein:", "fr": "Tous les champs suivants doivent être renseignés :"},
    "None of the following may be set:": {"de": "Keines der folgenden Felder darf gesetzt sein:", "fr": "Aucun des champs suivants ne doit être renseigné :"},
    "## Examples": {"de": "## Beispiele", "fr": "## Exemples"},
    "### Examples": {"de": "### Beispiele", "fr": "### Exemples"},
    "## Notes": {"de": "## Hinweise", "fr": "## Notes"},
    "## Comments": {"de": "## Kommentare", "fr": "## Commentaires"},
    "## Schema Diagram": {"de": "## Schema-Diagramm", "fr": "## Diagramme du schéma"},
    "## Classes": {"de": "## Klassen", "fr": "## Classes"},
    "## Enumerations": {"de": "## Enums", "fr": "## Énumérations"},
    "## Types": {"de": "## Typen", "fr": "## Types"},
    "## Subsets": {"de": "## Subsets", "fr": "## Sous-ensembles"},
    # table headers (full multi-column — must come before single-cell labels)
    "| Name | Cardinality and Range | Description |": {"de": "| Name | Kardinalität und Wertebereich | Beschreibung |", "fr": "| Nom | Cardinalité et plage | Description |"},
    "| Name | Description | Modifies Slot |": {"de": "| Name | Beschreibung | Ändert Slot |", "fr": "| Nom | Description | Modifie le slot |"},
    "| Value | Description | Additional Info |": {"de": "| Wert | Beschreibung | Zusätzliche Info |", "fr": "| Valeur | Description | Info supplémentaire |"},
    "| Property | Value |": {"de": "| Eigenschaft | Wert |", "fr": "| Propriété | Valeur |"},
    "| Value | Description |": {"de": "| Wert | Beschreibung |", "fr": "| Valeur | Description |"},
    "| Class | Description |": {"de": "| Klasse | Beschreibung |", "fr": "| Classe | Description |"},
    "| Slot | Description |": {"de": "| Slot | Beschreibung |", "fr": "| Slot | Description |"},
    "| Enumeration | Description |": {"de": "| Aufzählung | Beschreibung |", "fr": "| Énumération | Description |"},
    "| Type | Description |": {"de": "| Typ | Beschreibung |", "fr": "| Type | Description |"},
    "| Subset | Description |": {"de": "| Subset | Beschreibung |", "fr": "| Sous-ensemble | Description |"},
    # single-cell property-row / header labels
    "| Slot URI |": {"de": "| Slot-URI |", "fr": "| URI du slot |"},
    "| Domain Of |": {"de": "| Domäne von |", "fr": "| Domaine de |"},
    "| Multivalued |": {"de": "| Mehrwertig |", "fr": "| Multivalué |"},
    "| Identifier |": {"de": "| Identifikator |", "fr": "| Identifiant |"},
    "| Required |": {"de": "| Erforderlich |", "fr": "| Requis |"},
    "| Range |": {"de": "| Wertebereich |", "fr": "| Plage |"},
    "| Value |": {"de": "| Wert |", "fr": "| Valeur |"},
    "| Name |": {"de": "| Name |", "fr": "| Nom |"},
}


def translate(text, lang):
    for en in sorted(LABELS, key=len, reverse=True):
        text = text.replace(en, LABELS[en][lang])
    return text


def main():
    en_dir = os.path.join(DOCGEN, "en")
    for lang in ("de", "fr"):
        out_dir = os.path.join(DOCGEN, lang)
        os.makedirs(out_dir, exist_ok=True)
        for name in os.listdir(en_dir):
            if not name.endswith(".jinja2"):
                continue
            with open(os.path.join(en_dir, name), encoding="utf-8") as f:
                content = f.read()
            with open(os.path.join(out_dir, name), "w", encoding="utf-8") as f:
                f.write(translate(content, lang))
        print(f"docgen_labels.py: wrote {out_dir}")


if __name__ == "__main__":
    main()
