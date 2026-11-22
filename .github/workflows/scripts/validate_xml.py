"""Validate the generated example XML of a subgroup against its own XSD and
Schematron (both generated from schema.yaml by linkml-xsd).

    python .github/workflows/scripts/validate_xml.py ech-0294_actors

Checks every output/data_*.xml against output/schema.xsd and, if present,
output/schema.sch. Exits 1 on the first failing document set, printing GitHub
Actions ::error annotations, so a release never ships XML that its own XSD
rejects.
"""

import sys
from pathlib import Path

from lxml import etree, isoschematron

SVRL = "{http://purl.oclc.org/dsdl/svrl}"


def main(subgroup: str) -> int:
    output = Path(subgroup) / "output"
    documents = sorted(output.glob("data_*.xml"))
    if not documents:
        print(f"::error::no {output}/data_*.xml to validate")
        return 1
    xsd = etree.XMLSchema(etree.parse(str(output / "schema.xsd")))
    sch_path = output / "schema.sch"
    schematron = (
        isoschematron.Schematron(etree.parse(str(sch_path)), store_report=True)
        if sch_path.exists()
        else None
    )
    failed = 0
    for path in documents:
        document = etree.parse(str(path))
        problems = []
        if not xsd.validate(document):
            problems += [f"line {e.line}: {e.message}" for e in xsd.error_log]
        if schematron is not None and not schematron.validate(document):
            for item in schematron.validation_report.iter(f"{SVRL}failed-assert"):
                text = (item.findtext(f"{SVRL}text") or "").strip()
                problems.append(f"{item.get('location')}: {text}")
        if problems:
            failed += 1
            for problem in problems:
                print(f"::error file={path}::{problem}")
        else:
            print(f"ok  {path}")
    return 1 if failed else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
