#!/usr/bin/env python3
"""
set_docx_page_label.py <file.docx> <lang>

Translate the page counter in the DOCX header ("Page 3 of 47") into <lang>.

The Word reference template carries one header for all languages, with the
wording around the PAGE and NUMPAGES fields written out as static text. Pandoc
copies it unchanged, so the German and French documents would otherwise show
the English wording. This script rewrites just those two text runs; the fields
themselves stay untouched, so Word and LibreOffice keep updating the numbers.

The runs are recognised by their content ("Page" before the PAGE field, "of"
between the two fields), independent of the language currently in the template.
"""
import re
import sys
import zipfile

# Wording per language: text before the PAGE field, text between the two fields.
LABELS = {
    "de": ("Seite ", " von"),
    "fr": ("Page ", " sur"),
    "en": ("Page ", " of"),
    "it": ("Pagina ", " di"),
}

# All wordings this script may encounter in a template, so that a document can be
# re-labelled repeatedly without depending on the language it started from.
BEFORE = {v[0].strip() for v in LABELS.values()}
BETWEEN = {v[1].strip() for v in LABELS.values()}


def set_text(run_xml, text):
    """Replace the content of the single <w:t> in `run_xml` with `text`."""

    def repl(m):
        open_tag = m.group(1)
        if "xml:space" not in open_tag:
            open_tag = open_tag[:-1] + ' xml:space="preserve">'
        return open_tag + text + "</w:t>"

    return re.sub(r"(<w:t[^>]*>)[^<]*</w:t>", repl, run_xml, count=1)


def relabel(xml, before, between):
    """Rewrite the two static runs around the page fields."""
    hits = {"before": 0, "between": 0}

    def repl_run(m):
        run = m.group(0)
        content = "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", run)).strip()
        if content in BEFORE:
            hits["before"] += 1
            return set_text(run, before)
        if content in BETWEEN:
            hits["between"] += 1
            return set_text(run, between)
        return run

    return re.sub(r"<w:r[ >](?:(?!</w:r>).)*</w:r>", repl_run, xml, flags=re.S), hits


def main():
    path, lang = sys.argv[1], sys.argv[2]
    if lang not in LABELS:
        print(f"set_docx_page_label.py: unsupported language '{lang}'", file=sys.stderr)
        sys.exit(1)
    before, between = LABELS[lang]

    with zipfile.ZipFile(path) as zin:
        names = zin.namelist()
        data = {n: zin.read(n) for n in names}

    total = {"before": 0, "between": 0}
    for name in names:
        if not re.match(r"word/header\d+\.xml$", name):
            continue
        xml = data[name].decode("utf-8")
        if "PAGE" not in xml:
            continue
        new_xml, hits = relabel(xml, before, between)
        if new_xml != xml:
            data[name] = new_xml.encode("utf-8")
        total["before"] += hits["before"]
        total["between"] += hits["between"]

    if not total["before"]:
        print(f"set_docx_page_label.py: page counter not found in {path}", file=sys.stderr)
        sys.exit(1)

    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zout:
        for n in names:
            zout.writestr(n, data[n])
    print(f"set_docx_page_label.py: header set to '{before.strip()} N{between} M' ({lang}) in {path}")


if __name__ == "__main__":
    main()
