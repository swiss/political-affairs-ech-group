#!/usr/bin/env python3
"""
pdf_footer_info.py <input/<lang>/01_head.md>

Derive the PDF footer line from a chapter's metadata table so it stays in sync
with the document (version/status live only in 01_head.md, not hardcoded).

Prints, e.g.:  eCH-0294 – Political Affairs / Actors / 1.0.0 / Vorschlag
(The issue date is appended only once the "Ausgabedatum" field is filled in.)
"""
import re
import sys


def field(head, *labels):
    for label in labels:
        m = re.search(r"\|\s*\*\*" + re.escape(label) + r"\*\*\s*\|([^|\n]*)\|", head)
        if m and m.group(1).strip():
            return m.group(1).strip()
    return ""


# "<Fachgruppe> / <Standard>" label per language (matches the document language).
LABELS = {
    "de": "Politische Geschäfte / Akteure",
    "fr": "Affaires politiques / Acteurs",
    "en": "Political Affairs / Actors",
}


def main():
    path = sys.argv[1]
    head = open(path, encoding="utf-8").read()
    lang_match = re.search(r"/(de|fr|en)/", path)
    label = LABELS.get(lang_match.group(1) if lang_match else "en", LABELS["en"])
    number = field(head, "eCH-Nummer", "eCH number", "Numéro eCH") or "eCH-0294"
    version = field(head, "Version")
    status = field(head, "Status", "Statut")
    date = field(head, "Ausgabedatum", "Issue date", "Date de publication")
    parts = [f"{number} – {label}", version, status, date]
    print(" / ".join(p for p in parts if p))


if __name__ == "__main__":
    main()
