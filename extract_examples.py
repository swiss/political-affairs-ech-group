"""Extract per-class examples from Container-level data_*.yaml files.

Creates an examples/ folder with:
- Container-<name>.yaml  (full file, for Container-class docs)
- <ClassName>-<label>.yaml  (individual instances, for per-class docs)

Which classes get examples is controlled by:
    <ech-folder>/input/pipeline_examples_generator_config.yaml

Usage:
    python extract_examples.py <ech-folder>

Example:
    python extract_examples.py ech-0294_actors
"""

import sys
import re
import shutil
from pathlib import Path

import yaml

SLOT_TO_CLASS = {
    # Container-level slots
    "persons": "Person",
    "groups": "Group",
    "memberships": "Membership",
    "interest_links": "InterestLink",
    "legislatures": "Legislature",
    "sessions": "Session",
    "meetings": "Meeting",
    "agenda_items": "AgendaItem",
    "speeches": "Speech",
    "votings": "Voting",
    "elections": "Election",
    # Nested slots (inside Person, etc.)
    "names": "Name",
    "addresses": "Address",
    "language_proficiencies": "LanguageProficiency",
    "citizenships": "Citizenship",
    "genders": "Gender",
    "occupations": "Occupation",
    "trainings": "Training",
    "contacts": "Contact",
    "electoral_district": "ElectoralDistrict",
    # Group-level
    "group_types": "GroupType",
    "role_types": "RoleType",
    # Operations-level nested
    "attendances": "Attendance",
    "individual_attendances": "IndividualAttendance",
    "individual_votes": "IndividualVote",
    "resolutions": "Resolution",
    "documents": "Manifestation",
    "media": "Media",
}


def slugify(text: str) -> str:
    text = text.replace(" ", "_").replace("/", "_").replace(".", "_")
    text = re.sub(r"[^A-Za-z0-9_-]", "", text)
    return text[:60]


def label_for_instance(obj, index: int) -> str:
    for key in ("label", "global_uri", "name", "id"):
        if key in obj and obj[key]:
            val = str(obj[key])
            val = val.split("/")[-1].split(":")[-1]
            return slugify(val)
    return str(index + 1)


def extract_nested(obj, context: str, allowed_classes: set, parent_label: str = "") -> list:
    """Recursively extract examples for allowed classes from nested data."""
    results = []
    if not isinstance(obj, dict):
        return results

    for slot_name, class_name in SLOT_TO_CLASS.items():
        value = obj.get(slot_name)
        if value is None:
            continue

        items = value if isinstance(value, list) else [value]
        for i, item in enumerate(items):
            if not isinstance(item, dict):
                continue
            item_label = label_for_instance(item, i)
            if class_name in allowed_classes:
                prefix = f"{parent_label}_" if parent_label else ""
                filename = f"{class_name}-{context}_{prefix}{item_label}.yaml"
                results.append((filename, item))
            results.extend(extract_nested(item, context, allowed_classes, item_label))

    return results


def load_config(ech_folder: Path) -> set:
    config_path = ech_folder / "input" / "pipeline_examples_generator_config.yaml"
    if not config_path.exists():
        print(f"ERROR: Config not found: {config_path}")
        sys.exit(1)

    with open(config_path, encoding="utf-8") as f:
        config = yaml.safe_load(f)

    classes = set(config.get("classes", []))
    print(f"Config: generating examples for {sorted(classes)}")
    return classes


def extract(ech_folder: str):
    base = Path(ech_folder)
    input_dir = base / "input"
    output_dir = base / "output"
    examples_dir = output_dir / "examples"

    allowed_classes = load_config(base)

    if examples_dir.exists():
        shutil.rmtree(examples_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    examples_dir.mkdir()

    data_files = sorted(input_dir.glob("data_*.yaml"))
    if not data_files:
        print(f"No data_*.yaml files found in {input_dir}")
        sys.exit(1)

    for data_file in data_files:
        stem = data_file.stem.replace("data_", "")

        container_dest = examples_dir / f"Container-{stem}.yaml"
        shutil.copy2(data_file, container_dest)
        print(f"  Container-{stem}.yaml")

        with open(data_file, encoding="utf-8") as f:
            data = yaml.safe_load(f)

        if not isinstance(data, dict):
            continue

        extracted = extract_nested(data, stem, allowed_classes)
        for filename, item in extracted:
            filepath = examples_dir / filename
            with open(filepath, "w", encoding="utf-8") as f:
                yaml.dump(item, f, default_flow_style=False,
                          allow_unicode=True, sort_keys=False)
            print(f"  {filename}")

    print(f"\nExamples written to {examples_dir}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_examples.py <ech-folder>")
        sys.exit(1)
    extract(sys.argv[1])
