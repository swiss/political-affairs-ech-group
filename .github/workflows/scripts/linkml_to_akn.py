"""LinkML-YAML zurueck in ein AKN-Dokument schreiben.

    python linkml_to_akn.py <schema.yaml> <data.yaml> <out.xml>

Der Gegenweg zu akn_to_linkml.py und wie dieser schema-getrieben: Welches
Element ein Slot schreibt, steht in `annotations.xml_element`, welches Attribut
in `xml_attribute`/`xml_name`. Zusammen erlauben die beiden Richtungen den
Rundlauf -- eine echte Fedlex-Datei einlesen, als YAML halten, wieder
ausschreiben und mit dem Original vergleichen.
"""
import sys
import xml.etree.ElementTree as ET

import yaml

AKN = "http://docs.oasis-open.org/legaldocml/ns/akn/3.0"
FEDLEX = "http://fedlex.admin.ch/"
XML_NS = "http://www.w3.org/XML/1998/namespace"


class Writer:
    def __init__(self, schema):
        self.classes = schema["classes"]
        self.slots = schema["slots"]

    # -- Schema-Auskuenfte ---------------------------------------------------

    @staticmethod
    def _ann(defn):
        return (defn or {}).get("annotations") or {}

    def class_slots(self, cls):
        out, seen, cur = [], set(), cls
        while cur:
            defn = self.classes.get(cur, {})
            for s in defn.get("slots", []):
                if s not in seen:
                    seen.add(s)
                    out.append(s)
            cur = defn.get("is_a")
        return out

    def element_name(self, slot, value_cls):
        """Das Element, das dieser Slot schreibt."""
        ann = self._ann(self.slots.get(slot, {}))
        name = ann.get("xml_element")
        if not name and value_cls:
            name = self._ann(self.classes.get(value_cls, {})).get("xml_element")
        return name

    def attribute_name(self, slot):
        ann = self._ann(self.slots.get(slot, {}))
        if not ann.get("xml_attribute"):
            return None
        return ann.get("xml_name", slot)

    # -- Schreiben -----------------------------------------------------------

    def qname(self, name):
        """'akn:act' -> '{namespace}act'."""
        prefix, _, local = name.partition(":")
        ns = {"akn": AKN, "fedlex": FEDLEX, "xml": XML_NS}.get(prefix, AKN)
        return f"{{{ns}}}{local}"

    def write(self, parent, tag, value, cls):
        el = ET.SubElement(parent, self.qname(tag)) if parent is not None \
            else ET.Element(self.qname(tag))
        self.fill(el, value, cls)
        return el

    def fill(self, el, value, cls):
        if not isinstance(value, dict):
            el.text = str(value)
            return

        for slot in self.class_slots(cls):
            if slot not in value:
                continue
            attr = self.attribute_name(slot)
            if attr:
                el.set(self.qname(attr) if ":" in attr or attr == "lang" else attr,
                       str(value[slot]))

        for slot in self.class_slots(cls):
            if slot not in value or self.attribute_name(slot):
                continue
            if slot in ("inline_content", "element_type"):
                continue
            if isinstance(value[slot], list) and value[slot] \
                    and isinstance(value[slot][0], dict) and "element_type" in value[slot][0]:
                # Geordnete Folge mit Typ-Diskriminator: der Eintrag nennt seine
                # Klasse, die Klasse ihr Element.
                for item in value[slot]:
                    item_cls = item.get("element_type")
                    tag = self._ann(self.classes.get(item_cls, {})).get("xml_element")
                    if not tag:
                        continue
                    child = ET.SubElement(el, self.qname(tag))
                    self.fill(child, {k: v for k, v in item.items()
                                      if k != "element_type"}, item_cls)
                continue
            defn = self.slots.get(slot, {})
            rng = defn.get("range")
            child_cls = rng if rng in self.classes else None
            tag = self.element_name(slot, child_cls)
            items = value[slot] if isinstance(value[slot], list) else [value[slot]]
            for item in items:
                if child_cls:
                    self.write(el, tag, item, child_cls)
                else:
                    ET.SubElement(el, self.qname(tag)).text = str(item)

        if "inline_content" in value:
            self.fill_inline(el, value["inline_content"])

    def fill_inline(self, el, items):
        """Text und Auszeichnung in Lesereihenfolge zurueckschreiben."""
        last = None
        for item in items:
            cls = item.get("element_type")
            if cls == "TextRun":
                text = item.get("text", "")
                if last is None:
                    el.text = (el.text or "") + text
                else:
                    last.tail = (last.tail or "") + text
                continue
            tag = self._ann(self.classes.get(cls, {})).get("xml_element")
            if not tag:
                continue
            child = ET.SubElement(el, self.qname(tag))
            self.fill(child, {k: v for k, v in item.items() if k != "element_type"}, cls)
            last = child


def main(schema_path, data_path, out_path):
    with open(schema_path, encoding="utf-8") as fh:
        schema = yaml.safe_load(fh)
    with open(data_path, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)

    writer = Writer(schema)
    root_cls = next(n for n, d in schema["classes"].items() if d.get("tree_root"))
    root_tag = Writer._ann(schema["classes"][root_cls]).get("xml_element")

    ET.register_namespace("", AKN)
    ET.register_namespace("fedlex", FEDLEX)
    root = writer.write(None, root_tag, data, root_cls)

    ET.ElementTree(root).write(out_path, encoding="UTF-8", xml_declaration=True)
    print(f"geschrieben: {out_path}")


if __name__ == "__main__":
    main(*sys.argv[1:4])
