#!/usr/bin/env python3
"""
ech_doc_filename.py <input/<lang>/01_head.md> <lang-code: d|f|e> [version]

Print the eCH-conform document filename stem (no extension), following the
eCH-0003 naming convention:

    <TYPE>_<lang>_<STATUS>_<YYYY-MM-DD>_<eCH-XXXX>_V<version>_<Title>

Example:
    STAN_d_DRA_2026-07-22_eCH-0294_V1.0.0_Politische Akteure - Personen, Gruppen und Organe

All parts are derived from the metadata table in 01_head.md so the released
"Beilagen" stay in sync with the document (version/status/date live only there).
"""
import re
import sys


def field(head, *labels):
    for label in labels:
        m = re.search(r"\|\s*\*\*" + re.escape(label) + r"\*\*\s*\|([^|\n]*)\|", head)
        if m and m.group(1).strip():
            return m.group(1).strip()
    return ""


# eCH-0003 document-type prefix, keyed by the "Kategorie" / "Catégorie" field.
# Only STAN is used here; default to STAN for any Standard-like category.
TYPE_CODE = {
    "standard": "STAN",
    "norme": "STAN",
    "best practice": "BPRA",
    "bonne pratique": "BPRA",
    "hilfsmittel": "TOOL",
    "aide": "TOOL",
    "white paper": "WHIT",
    "livre blanc": "WHIT",
    "addendum": "ADDE",
}

# eCH-0003 status codes used in filenames. Anything pre-approval (In Arbeit,
# Entwurf, Vorschlag / Proposal / Proposition) is a draft -> DRA; approved -> DEF.
STATUS_CODE = {
    "genehmigt": "DEF",
    "approved": "DEF",
    "approuvé": "DEF",
    "annulliert": "NUL",
    "ersetzt": "REP",
    "replaced": "REP",
    "remplacé": "REP",
}


def main():
    path = sys.argv[1]
    lang = sys.argv[2]  # d | f | e
    head = open(path, encoding="utf-8").read()

    number = field(head, "eCH-Nummer", "eCH number", "Numéro eCH") or "eCH-0294"
    category = field(head, "Kategorie", "Category", "Catégorie")
    status = field(head, "Status", "Statut")
    date = field(head, "Ausgabedatum", "Issue date", "Date de publication")
    version = sys.argv[3] if len(sys.argv) > 3 else field(head, "Version")
    name = field(head, "Name", "Nom").strip("* ").strip()

    type_code = TYPE_CODE.get(category.lower(), "STAN")
    status_code = STATUS_CODE.get(status.lower(), "DRA")

    # Readable, filesystem-safe title: colon (de/en) or " : " (fr) -> " - ".
    title = re.sub(r"\s*:\s*", " - ", name)
    title = re.sub(r'[\\/*?"<>|]', "", title).strip()

    stem = f"{type_code}_{lang}_{status_code}_{date}_{number}_V{version}_{title}"
    print(stem)


if __name__ == "__main__":
    main()
