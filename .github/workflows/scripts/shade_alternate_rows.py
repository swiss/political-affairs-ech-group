#!/usr/bin/env python3
"""
.github/workflows/scripts/shade_alternate_rows.py <file.docx> [<file.docx> ...]

Bake zebra striping directly into every table: give every other body row a light
gray cell background. Unlike table-style row banding (which Word renders only
under specific tblLook/tblStyleRowBandSize conditions), explicit per-cell shading
renders identically in Word, LibreOffice and PDF.

Idempotent-ish: re-running re-applies the same shading (existing shd elements are
replaced). The header row (first row) is left unshaded.
"""
import sys
import zipfile
from xml.etree import ElementTree as ET

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = f"{{{W}}}"
FILL = "F2F2F2"
DOC = "word/document.xml"

# Schema order of w:tcPr children; w:shd must be inserted before any of these.
AFTER_SHD = {f"{NS}{t}" for t in ("noWrap", "tcMar", "textDirection", "tcFit", "vAlign", "hideMark")}


def set_cell_shading(tc):
    tcPr = tc.find(f"{NS}tcPr")
    if tcPr is None:
        tcPr = ET.Element(f"{NS}tcPr")
        tc.insert(0, tcPr)
    for existing in tcPr.findall(f"{NS}shd"):
        tcPr.remove(existing)
    shd = ET.Element(f"{NS}shd", {f"{NS}val": "clear", f"{NS}color": "auto", f"{NS}fill": FILL})
    # Insert before the first child that must follow shd, else append.
    idx = len(list(tcPr))
    for i, child in enumerate(list(tcPr)):
        if child.tag in AFTER_SHD:
            idx = i
            break
    tcPr.insert(idx, shd)


def shade(xml_bytes):
    ET.register_namespace("w", W)
    root = ET.fromstring(xml_bytes)
    for tbl in root.iter(f"{NS}tbl"):
        rows = tbl.findall(f"{NS}tr")
        for i, row in enumerate(rows):
            if i == 0 or i % 2 == 0:  # skip header (0) and even body rows -> shade 1,3,5,...
                continue
            for tc in row.findall(f"{NS}tc"):
                set_cell_shading(tc)
    body = ET.tostring(root, encoding="unicode")
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r\n' + body).encode("utf-8")


def patch(path):
    with zipfile.ZipFile(path) as zin:
        names = zin.namelist()
        data = {n: zin.read(n) for n in names}
    data[DOC] = shade(data[DOC])
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zout:
        for n in names:
            zout.writestr(n, data[n])
    print(f"shade_alternate_rows.py: zebra shading baked into {path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: .github/workflows/scripts/shade_alternate_rows.py <file.docx> ...", file=sys.stderr)
        sys.exit(2)
    for p in sys.argv[1:]:
        patch(p)
