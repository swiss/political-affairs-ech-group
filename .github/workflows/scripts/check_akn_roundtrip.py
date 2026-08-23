"""Pruefen, ob das Schema die amtlichen AKN-Dateien noch vollstaendig traegt.

    python .github/workflows/scripts/check_akn_roundtrip.py <ech-folder> [<xml> ...]

Ohne Dateiangabe werden alle AkomaNtoso-Dateien unter
`<ech-folder>/misc/spec/input/examples/` geprueft.

Warum es diesen Schritt braucht: Das Schema speist Code, der nicht in diesem
Repo liegt -- den XSD- und XML-Konverter. Bricht eine Schemaaenderung dessen
Annahmen, faellt das hier sonst nicht auf. Der Rundlauf prueft genau diese
Annahmen, weil er dieselben Angaben verwendet: `xml_element` sagt, welches
Element eine Klasse schreibt, `xml_attribute` und `xml_name`, welches Attribut
ein Slot traegt, und die Reihenfolge der Slots die Reihenfolge im Dokument.

Zwei Pruefungen je Datei:

1. *Rundlauf.* Die Datei wird nach LinkML uebersetzt und zurueckgeschrieben.
   Original und Ergebnis muessen in jedem Knoten uebereinstimmen -- Pfad,
   Attribute, Text und Reihenfolge. Eine Abweichung heisst, dass das Modell
   etwas nicht mehr halten kann.

2. *Schemavalidierung*, sofern lxml vorhanden. Gemessen wird nicht, ob das
   Ergebnis gegen akomantoso30.xsd valide ist, sondern ob es *dieselben*
   Befunde hat wie das Original: Die amtliche Bundesverfassung verletzt die
   eId-Eindeutigkeit des AKN-Schemas an vier Stellen (siehe ADR 0006), und ein
   treues Abbild muss diesen Mangel wiedergeben, nicht heilen.
"""
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

SCRIPTS = Path(__file__).parent
AKN_MARKER = "akomaNtoso"


def nodes(path):
    """Jeden Knoten als (Pfad, Attribute, Text) in Dokumentreihenfolge.

    `xsi:schemaLocation` bleibt aussen vor: Es ist eine Angabe ueber das
    Dokument, nicht ueber seinen Inhalt, und die Konverter fuehren sie nicht.
    """
    out = []

    def walk(el, path):
        name = el.tag.split("}")[-1]
        here = f"{path}/{name}"
        attrs = tuple(sorted((k.split("}")[-1], v) for k, v in el.attrib.items()
                             if k.split("}")[-1] != "schemaLocation"))
        out.append((here, attrs, " ".join((el.text or "").split())))
        for child in el:
            if isinstance(child.tag, str):
                walk(child, here)

    walk(ET.parse(path).getroot(), "")
    return out


def run(script, *args):
    result = subprocess.run([sys.executable, str(SCRIPTS / script), *map(str, args)],
                            capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"{script}: {result.stderr.strip().splitlines()[-1:] or result.stdout}")


def schema_errors(xsd, path):
    """Die Befunde der Schemavalidierung, oder None, wenn lxml fehlt."""
    if xsd is None:
        return None
    from lxml import etree
    xsd.validate(etree.parse(str(path)))
    return sorted(e.message for e in xsd.error_log)


def load_xsd(folder):
    candidates = list(Path(folder).glob("misc/**/akomantoso30.xsd"))
    if not candidates:
        return None, "kein akomantoso30.xsd im Ordner"
    try:
        from lxml import etree
    except ImportError:
        return None, "lxml nicht installiert"
    return etree.XMLSchema(etree.parse(str(candidates[0]))), str(candidates[0])


def check(folder, xml_files, tmp):
    schema = Path(folder) / "input" / "schema.yaml"
    xsd, xsd_note = load_xsd(folder)
    print(f"Schemavalidierung: {xsd_note}")

    failures = []
    for xml in xml_files:
        name = Path(xml).stem[:44]
        yaml_path = tmp / (Path(xml).stem.replace(" ", "_") + ".yaml")
        back = tmp / (Path(xml).stem.replace(" ", "_") + ".xml")
        try:
            run("akn_to_linkml.py", schema, xml, yaml_path)
            run("linkml_to_akn.py", schema, yaml_path, back)
        except RuntimeError as err:
            failures.append(f"{name}: Konversion fehlgeschlagen -- {err}")
            print(f"  ✗ {name}")
            continue

        before, after = nodes(xml), nodes(back)
        if before != after:
            same = sum(1 for a, b in zip(before, after) if a == b)
            first = next((a[0] for a, b in zip(before, after) if a != b), "(Laenge)")
            failures.append(f"{name}: {same} von {len(before)} Knoten gleich, "
                            f"erste Abweichung bei {first}")
            print(f"  ✗ {name}: {len(before)} Knoten, {same} gleich")
            continue

        errs_before, errs_after = schema_errors(xsd, xml), schema_errors(xsd, back)
        if errs_before is not None and errs_before != errs_after:
            failures.append(f"{name}: Schemabefunde weichen ab -- Original "
                            f"{len(errs_before)}, Ergebnis {len(errs_after)}")
            print(f"  ✗ {name}: Schemabefunde weichen ab")
            continue

        note = "" if not errs_before else f", {len(errs_before)} Schemabefunde wie im Original"
        print(f"  ✓ {name}: {len(before)} Knoten{note}")

    return failures


def main(folder, args):
    if args:
        xml_files = args
    else:
        base = Path(folder) / "misc" / "spec" / "input" / "examples"
        xml_files = sorted(p for p in base.glob("*/*.xml")
                           if AKN_MARKER in p.read_text(encoding="utf-8", errors="ignore")[:400])
    if not xml_files:
        print("Keine AkomaNtoso-Dateien gefunden -- nichts zu pruefen.")
        return 0

    print(f"Rundlauf ueber {len(xml_files)} amtliche AKN-Dateien:")
    # Die Zwischenergebnisse sind Pruefmaterial, kein Artefakt des Standards --
    # sie gehoeren nicht in output/, das die Action committet.
    with tempfile.TemporaryDirectory() as tmp:
        failures = check(folder, xml_files, Path(tmp))
    if failures:
        print(f"\nFEHLGESCHLAGEN ({len(failures)}):")
        for f in failures:
            print(f"  {f}")
        print("\nDas Schema traegt diese Dateien nicht mehr vollstaendig. Meist fehlt "
              "eine xml_element- oder xml_name-Angabe, oder die Reihenfolge der Slots "
              "weicht vom Inhaltsmodell von Akoma Ntoso ab.")
        return 1
    print(f"\nAlle {len(xml_files)} Dateien laufen verlustfrei durch.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python .github/workflows/scripts/check_akn_roundtrip.py "
              "<ech-folder> [<xml> ...]")
        sys.exit(1)
    sys.exit(main(sys.argv[1], sys.argv[2:]))
