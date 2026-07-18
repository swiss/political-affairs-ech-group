#!/usr/bin/env python3
"""
.github/workflows/scripts/set_docx_updatefields.py <file.docx> [<file.docx> ...]

Force Word to refresh all fields — most importantly the table of contents — when
the document is opened, by setting <w:updateFields w:val="true"/> in the DOCX's
word/settings.xml.

Why this exists: pandoc writes only an *empty* TOC field (it cannot paginate).
Word fills that field in on open, but only if updateFields is set. Passing the
flag through the reference template is unreliable — the pandoc version installed
on the CI runner regenerates settings.xml and drops the flag. Injecting it here,
after pandoc has run, is deterministic and version-independent.

Idempotent: does nothing if the flag is already present.
"""
import re
import shutil
import sys
import tempfile
import zipfile

SETTINGS = "word/settings.xml"
FLAG = '<w:updateFields w:val="true"/>'


def patch(path: str) -> bool:
    with zipfile.ZipFile(path) as zin:
        names = zin.namelist()
        if SETTINGS not in names:
            print(f"{path}: no {SETTINGS} — skipped", file=sys.stderr)
            return False
        data = {n: zin.read(n) for n in names}

    xml = data[SETTINGS].decode("utf-8")
    if "w:updateFields" in xml:
        print(f"{path}: updateFields already set — unchanged")
        return False

    new_xml, n = re.subn(r"(<w:settings\b[^>]*>)", r"\1" + FLAG, xml, count=1)
    if n != 1:
        print(f"{path}: could not locate <w:settings> — skipped", file=sys.stderr)
        return False
    data[SETTINGS] = new_xml.encode("utf-8")

    # Rewrite the archive, preserving every other entry byte-for-byte.
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".docx")
    tmp.close()
    with zipfile.ZipFile(tmp.name, "w", zipfile.ZIP_DEFLATED) as zout:
        for n in names:
            zout.writestr(n, data[n])
    shutil.move(tmp.name, path)
    print(f"{path}: updateFields set (Word will refresh the TOC on open)")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    for p in sys.argv[1:]:
        patch(p)
