"""Ein AKN-Dokument in schema-konformes LinkML-YAML uebersetzen.

    python akn_to_linkml.py <schema.yaml> <akn.xml> <out.yaml>

Der Konverter kennt keine Elementnamen: Er liest die Bindung aus dem Schema --
`annotations.xml_element` sagt, welche Klasse zu welchem AKN-Element gehoert,
`xml_attribute`/`xml_name`, welcher Slot aus welchem Attribut kommt. Was das
Schema nicht modelliert, wird uebersprungen und am Ende gemeldet, statt still
zu verschwinden.
"""
import sys
from collections import Counter, defaultdict

import yaml
import xml.etree.ElementTree as etree

AKN = "http://docs.oasis-open.org/legaldocml/ns/akn/3.0"
XML = "http://www.w3.org/XML/1998/namespace"
FEDLEX = "http://fedlex.admin.ch/"
NAMESPACES = {"akn": AKN, "xml": XML, "fedlex": FEDLEX}


def attr_key(name):
    """Attributname aus dem Schema in die Schreibweise von ElementTree.

    `xml_name` kann einen Praefix tragen -- xml:lang, fedlex:generator --, und
    ElementTree adressiert solche Attribute ueber {Namensraum}name. Ohne diese
    Umsetzung liest `element.get("xml:lang")` schlicht nichts.
    """
    prefix, sep, local = name.partition(":")
    if sep and prefix in NAMESPACES:
        return f"{{{NAMESPACES[prefix]}}}{local}"
    return name


class Schema:
    """Die Abbildungsregeln, aus dem LinkML-Schema gelesen."""

    def __init__(self, path):
        with open(path, encoding="utf-8") as fh:
            self.raw = yaml.safe_load(fh)
        self.classes = self.raw["classes"]
        self.slots = self.raw["slots"]
        # AKN-Element -> Klassen, die es tragen. Mehrere sind moeglich: akn:p ist
        # sowohl der Vorspann-Absatz als auch der Inhaltsabsatz.
        self.class_by_element = defaultdict(list)
        for name, defn in self.classes.items():
            el = self._ann(defn).get("xml_element")
            if el:
                self.class_by_element[el.split(":")[-1]].append(name)
        # Subklassen der abstrakten Basen: InlineElement fuer den gemischten
        # Inhalt, BlockElement fuer die geordnete Folge aus Absatz, Aufzaehlung
        # und Tabelle.
        self.inline_by_element = self._subclasses("InlineElement")
        self.block_by_element = self._subclasses("BlockElement")

    def _subclasses(self, base):
        out = {}
        for name, defn in self.classes.items():
            if defn.get("is_a") == base:
                el = self._ann(defn).get("xml_element")
                if el:
                    out[el.split(":")[-1]] = name
        return out

    @staticmethod
    def _ann(defn):
        return (defn or {}).get("annotations") or {}

    def slot_def(self, slot):
        return self.slots.get(slot, {})

    def class_slots(self, cls):
        """Slots der Klasse, inklusive der geerbten."""
        out, seen = [], set()
        while cls:
            defn = self.classes.get(cls, {})
            for s in defn.get("slots", []):
                if s not in seen:
                    seen.add(s)
                    out.append(s)
            cls = defn.get("is_a")
        return out

    def attribute_slots(self, cls):
        """(Slotname, XML-Attributname) je Slot, der aus einem Attribut kommt."""
        result = []
        for slot in self.class_slots(cls):
            ann = self._ann(self.slot_def(slot))
            if ann.get("xml_attribute"):
                result.append((slot, ann.get("xml_name", slot)))
        return result

    def child_slots(self, cls):
        """(Slotname, Zielklasse, mehrwertig, Elementname) je Kind-Slot."""
        result = []
        for slot in self.class_slots(cls):
            defn = self.slot_def(slot)
            ann = self._ann(defn)
            if ann.get("xml_attribute"):
                continue
            rng = defn.get("range")
            if rng not in self.classes:
                # Kein Klassen-Range: ein Textslot wie doc_number.
                result.append((slot, None, defn.get("multivalued", False),
                               (ann.get("xml_element") or "").split(":")[-1] or slot))
                continue
            # Der Elementname steht am Slot, sonst an der Zielklasse.
            el = ann.get("xml_element") or self._ann(self.classes[rng]).get("xml_element") or ""
            result.append((slot, rng, defn.get("multivalued", False), el.split(":")[-1]))
        return result


def local(tag):
    """Elementname ohne Namensraum."""
    return tag.split("}")[-1] if isinstance(tag, str) else ""


class Converter:
    def __init__(self, schema):
        self.s = schema
        self.skipped = Counter()

    def convert(self, element, cls):
        """Ein XML-Element in die Instanz der angegebenen Klasse uebersetzen."""
        out = {}

        for slot, attr in self.s.attribute_slots(cls):
            value = element.get(attr_key(attr))
            if value is not None:
                out[slot] = value

        children = self.s.child_slots(cls)
        by_element = {el: (slot, rng, multi) for slot, rng, multi, el in children if el}

        # Blockinhalt in Lesereihenfolge, mit Typ-Diskriminator je Eintrag.
        if any(slot == "content_blocks" for slot, _, _, _ in children):
            blocks = []
            for child in element:
                if not isinstance(child.tag, str):
                    continue
                name = local(child.tag)
                block_cls = self.s.block_by_element.get(name)
                if not block_cls:
                    self.skipped[f"{local(element.tag)} > {name}"] += 1
                    continue
                item = {"element_type": block_cls}
                item.update(self.convert(child, block_cls))
                blocks.append(item)
            if blocks:
                out["content_blocks"] = blocks
            elif not out:
                # Leeres Element, etwa eine leere Tabellenzelle: der LinkML-Lader
                # nimmt in einer Liste kein leeres Objekt an, eine leere Liste
                # aber schon -- und beim Zurueckschreiben entsteht dasselbe
                # leere Element.
                out["content_blocks"] = []
            # Klassen, die neben dem Blockinhalt eigene Kinder fuehren -- der
            # Hauptteil eines Anhangs etwa --, holen diese anschliessend ab.
            if not any(slot not in ("content_blocks",) and rng
                       for slot, rng, _, _ in children):
                return out

        has_inline = any(slot == "inline_content" for slot, _, _, _ in children)
        # Eine Klasse, die nur gemischten Inhalt kennt, liest Text und
        # Auszeichnung in Lesereihenfolge und ist damit fertig.
        if has_inline and len(by_element) <= 1:
            inline = self.inline(element)
            if inline:
                out["inline_content"] = inline
            return out

        for child in element:
            if not isinstance(child.tag, str):
                continue  # Kommentar oder Verarbeitungsanweisung
            name = local(child.tag)
            if name not in by_element:
                self.skipped[f"{local(element.tag)} > {name}"] += 1
                continue
            slot, rng, multi = by_element[name]
            value = self.convert(child, rng) if rng else (child.text or "")
            if multi:
                out.setdefault(slot, []).append(value)
            else:
                out[slot] = value

        # Klassen mit eigenen Kind-Slots *und* gemischtem Inhalt -- der
        # Vorspann-Absatz etwa, der neben Nummer und Titel freien Text traegt:
        # was kein bekanntes Kind war, kommt als Inline-Inhalt dazu. Die bereits
        # abgeholten Kinder werden dabei ausgelassen, sonst stuende ihr Text ein
        # zweites Mal da.
        if has_inline and "inline_content" not in out:
            leftover = self.inline(element, skip=set(by_element))
            if leftover:
                out["inline_content"] = leftover

        # Eine leere Tabellenzelle traegt nichts -- und ein leeres Objekt lehnt
        # der LinkML-Lader in einer Liste ab ("Empty list elements are not
        # allowed"). Der erste mehrwertige Slot der Klasse wird deshalb
        # ausdruecklich als leere Liste gesetzt: sachlich dasselbe, und beim
        # Zurueckschreiben entsteht wieder das leere Element.
        if not out:
            for slot, rng, multi, _ in children:
                if multi:
                    out[slot] = []
                    break
        return out

    def inline(self, element, skip=frozenset()):
        """Text und Inline-Elemente als geordnete Liste.

        `skip` nennt Elementnamen, die der Aufrufer schon als eigenen Slot
        abgeholt hat; ihr Text gehoert dann nicht noch einmal hierher.
        """
        items = []
        if element.text and element.text.strip():
            items.append({"element_type": "TextRun", "text": " ".join(element.text.split())})
        for child in element:
            if not isinstance(child.tag, str):
                continue
            name = local(child.tag)
            if name in skip:
                if child.tail and child.tail.strip():
                    items.append({"element_type": "TextRun",
                                  "text": " ".join(child.tail.split())})
                continue
            cls = self.s.inline_by_element.get(name)
            if cls:
                item = {"element_type": cls}
                item.update(self.convert(child, cls))
                items.append(item)
            else:
                self.skipped[f"inline > {name}"] += 1
                # Der Text eines nicht modellierten Elements geht nicht verloren.
                if child.text and child.text.strip():
                    items.append({"element_type": "TextRun",
                                  "text": " ".join(child.text.split())})
            if child.tail and child.tail.strip():
                items.append({"element_type": "TextRun",
                              "text": " ".join(child.tail.split())})
        return items


def main(schema_path, xml_path, out_path):
    schema = Schema(schema_path)
    tree = etree.parse(xml_path)
    root = tree.getroot()

    conv = Converter(schema)
    # Das Wurzelelement ist akomaNtoso; die tree_root-Klasse traegt es.
    root_cls = next(n for n, d in schema.classes.items() if d.get("tree_root"))
    data = conv.convert(root, root_cls)

    with open(out_path, "w", encoding="utf-8") as fh:
        yaml.safe_dump(data, fh, allow_unicode=True, sort_keys=False, width=100)

    print(f"geschrieben: {out_path}")
    if conv.skipped:
        print("\nnicht abgebildet (Element im Kontext -> Anzahl):")
        for key, count in conv.skipped.most_common():
            print(f"  {key}: {count}")


if __name__ == "__main__":
    main(*sys.argv[1:4])
