#!/usr/bin/env python3
"""
set_docx_footer.py <file.docx> <footer-text>

Overwrite the eCH footer info line in a generated DOCX with <footer-text>, so the
Word footer stays in sync with the metadata (same string the PDF uses). The Word
reference template carries only a placeholder; deriving it here avoids drift.

The footer line is identified by the text "Political Affairs" in a footer part.
Its paragraph's runs are collapsed to a single run carrying the new text (the
run's formatting is kept from the first run).
"""
import re
import sys
import zipfile


def xml_escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def set_paragraph_text(para, text):
    """Put `text` in the first <w:t> of the paragraph, empty the remaining ones."""
    state = {"done": False}

    def repl(m):
        open_tag = m.group(1)
        if state["done"]:
            return open_tag + "</w:t>"
        state["done"] = True
        if "xml:space" not in open_tag:
            open_tag = open_tag[:-1] + ' xml:space="preserve">'
        return open_tag + xml_escape(text) + "</w:t>"

    return re.sub(r"(<w:t[^>]*>)[^<]*</w:t>", repl, para)


def main():
    path, footer = sys.argv[1], sys.argv[2]
    with zipfile.ZipFile(path) as zin:
        names = zin.namelist()
        data = {n: zin.read(n) for n in names}

    changed = False
    for name in names:
        if not re.match(r"word/footer\d+\.xml$", name):
            continue
        xml = data[name].decode("utf-8")
        if "Political Affairs" not in xml:
            continue

        def repl_para(m):
            para = m.group(0)
            return set_paragraph_text(para, footer) if "Political Affairs" in para else para

        new_xml = re.sub(r"<w:p[ >].*?</w:p>", repl_para, xml, flags=re.S)
        if new_xml != xml:
            data[name] = new_xml.encode("utf-8")
            changed = True

    if not changed:
        print(f"set_docx_footer.py: footer line not found in {path}", file=sys.stderr)
        sys.exit(1)

    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zout:
        for n in names:
            zout.writestr(n, data[n])
    print(f"set_docx_footer.py: footer set to '{footer}' in {path}")


if __name__ == "__main__":
    main()
