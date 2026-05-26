"""Extract per-class and per-slot examples from Container-level data_*.yaml files.

Creates:
- output/examples/  → Class-level YAML example files for gen-doc --example-directory
- output/schema_enriched.yaml → Copy of schema with slot examples injected

Controlled by: <ech-folder>/input/pipeline_examples_generator_config.yaml

Usage:
    python extract_examples.py <ech-folder>

Example:
    python extract_examples.py ech-0294_actors
"""

import sys
import re
import shutil
from pathlib import Path
from collections import defaultdict

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
    """Recursively extract class-level examples for allowed classes."""
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


def collect_slot_values(obj, allowed_slots: set, collected: dict):
    """Recursively collect values for configured slots from nested data."""
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in allowed_slots and not isinstance(value, (dict, list)):
                collected[key].add(str(value))
            collect_slot_values(value, allowed_slots, collected)
    elif isinstance(obj, list):
        for item in obj:
            collect_slot_values(item, allowed_slots, collected)


def enrich_schema(schema_path: Path, output_path: Path, slot_examples: dict, max_examples: int):
    """Write a copy of schema.yaml with examples: injected on configured slots."""
    with open(schema_path, encoding="utf-8") as f:
        schema = yaml.safe_load(f)

    slots = schema.get("slots", {})
    for slot_name, values in slot_examples.items():
        if slot_name not in slots:
            continue
        if slots[slot_name] is None:
            slots[slot_name] = {}
        examples = [{"value": v} for v in sorted(values)[:max_examples]]
        slots[slot_name]["examples"] = examples

    with open(output_path, "w", encoding="utf-8") as f:
        yaml.dump(schema, f, default_flow_style=False, allow_unicode=True,
                  sort_keys=False, width=120)

    print(f"\nEnriched schema written to {output_path}")
    for slot_name, values in sorted(slot_examples.items()):
        shown = sorted(values)[:max_examples]
        print(f"  {slot_name}: {shown}")


def load_config(ech_folder: Path) -> dict:
    config_path = ech_folder / "input" / "pipeline_examples_generator_config.yaml"
    if not config_path.exists():
        print(f"ERROR: Config not found: {config_path}")
        sys.exit(1)

    with open(config_path, encoding="utf-8") as f:
        config = yaml.safe_load(f)

    return config


def extract(ech_folder: str):
    base = Path(ech_folder)
    input_dir = base / "input"
    output_dir = base / "output"
    examples_dir = output_dir / "examples"

    config = load_config(base)
    allowed_classes = set(config.get("classes", []))
    allowed_slots = set(config.get("slots", []))
    max_examples = config.get("max_examples_per_slot", 3)

    print(f"Config: classes={sorted(allowed_classes)}")
    print(f"Config: slots={sorted(allowed_slots)}")

    if examples_dir.exists():
        shutil.rmtree(examples_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    examples_dir.mkdir()

    data_files = sorted(input_dir.glob("data_*.yaml"))
    if not data_files:
        print(f"No data_*.yaml files found in {input_dir}")
        sys.exit(1)

    slot_values = defaultdict(set)

    for data_file in data_files:
        stem = data_file.stem.replace("data_", "")

        container_dest = examples_dir / f"Container-{stem}.yaml"
        shutil.copy2(data_file, container_dest)
        print(f"  Container-{stem}.yaml")

        with open(data_file, encoding="utf-8") as f:
            data = yaml.safe_load(f)

        if not isinstance(data, dict):
            continue

        # Class examples
        extracted = extract_nested(data, stem, allowed_classes)
        for filename, item in extracted:
            filepath = examples_dir / filename
            with open(filepath, "w", encoding="utf-8") as f:
                yaml.dump(item, f, default_flow_style=False,
                          allow_unicode=True, sort_keys=False)
            print(f"  {filename}")

        # Slot values
        if allowed_slots:
            collect_slot_values(data, allowed_slots, slot_values)

    print(f"\nClass examples written to {examples_dir}")

    # Enriched schema
    if allowed_slots and slot_values:
        schema_path = input_dir / "schema.yaml"
        enriched_path = output_dir / "pipeline_examples_generator_schema.yaml"
        enrich_schema(schema_path, enriched_path, slot_values, max_examples)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_examples.py <ech-folder>")
        sys.exit(1)
    extract(sys.argv[1])
