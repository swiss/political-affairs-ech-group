"""Extract per-class and per-slot examples from Container-level data_*.yaml files.

Creates:
- output/examples/  → Class-level YAML example files for gen-doc --example-directory
- output/schema_enriched.yaml → Copy of schema with slot examples injected

Controlled by: <ech-folder>/input/pipeline_examples_generator_config.yaml

Usage:
    python .github/workflows/scripts/extract_examples.py <ech-folder>

Example:
    python .github/workflows/scripts/extract_examples.py ech-0294_actors
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
    "person_reference": "PersonReference",
    "group_reference": "GroupReference",
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


# A code block in the DOCX/PDF holds 97 characters per line. PyYAML treats the
# width as a soft limit and overshoots by up to one word, so the wrap is set
# well below that -- otherwise the renderer wraps a second time and the value
# ends up spread over two different indentation levels.
YAML_WIDTH = 80


# Codes whose leading zero carries meaning, e.g. the legal form "0109" (Verein).
# PyYAML quotes "0106" and "0110" on its own, because under its YAML 1.1
# resolver those read as octal numbers -- but "0109" contains a 9, is therefore
# no valid octal, resolves as a string and is emitted bare. The printed example
# then shows a four-digit code that looks like a number, and a reader (or a
# parser applying a different resolver) may take it for 109.
LEADING_ZERO_CODE = re.compile(r"^0[0-9]+$")


def represent_str(dumper, data):
    """Quote leading-zero codes, emit long prose as a folded block scalar.

    A wrapped plain scalar continues at an indentation of its own, which makes
    it hard to see where a value begins and ends. A folded scalar keeps every
    line at the same indentation and reads as one coherent value. Folding joins
    the lines back with spaces on load, so it stays lossless -- but only for
    text without line breaks or edge whitespace, hence the guard. Short values
    are left alone: forcing a folded scalar on e.g. '0110' would drop its
    quoting and turn it into a number.
    """
    if LEADING_ZERO_CODE.match(data):
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="'")
    if len(data) > YAML_WIDTH and "\n" not in data and data == data.strip():
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=">")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


yaml.add_representer(str, represent_str)


def slugify(text: str) -> str:
    """Turn a title into a file name; gen-doc renders it back as the heading.

    Kept in sync with `slugify()` in merge_documentation.py, which reproduces
    the same transformation to match a heading back to its configured title.
    """
    text = text.replace(" ", "_").replace("/", "_").replace(".", "_")
    text = re.sub(r"[^A-Za-z0-9_-]", "", text)
    return text[:80]


def title_for_instance(obj, titles: dict, lang: str) -> str:
    """Return the configured, language-specific title for an instance, if any.

    Keyed by `local_id`, or by `global_uri` where an instance carries no local
    identifier, so a data file can be reordered or renamed without breaking the
    mapping. Falls back to German, then to any language present.
    """
    if not isinstance(obj, dict):
        return ""
    entry = None
    for key in ("local_id", "global_uri"):
        entry = titles.get(str(obj.get(key, "")))
        if entry:
            break
    if not entry:
        return ""
    if isinstance(entry, str):
        return slugify(entry)
    return slugify(entry.get(lang) or entry.get("de") or next(iter(entry.values()), ""))


def plain_text(value):
    """Reduce a slot value to a single string usable in a file name.

    A multilingual slot holds a list of {value, language} entries; without this
    the whole structure would be stringified and every instance would end up
    with the same file name, silently overwriting one another.
    """
    if isinstance(value, list):
        value = value[0] if value else None
    if isinstance(value, dict):
        value = value.get("value")
    return str(value) if value else ""


def label_for_instance(obj, index: int) -> str:
    for key in ("label", "global_uri", "name", "id"):
        if key in obj and obj[key]:
            val = plain_text(obj[key])
            if not val:
                continue
            val = val.split("/")[-1].split(":")[-1]
            return slugify(val)
    return str(index + 1)


def instance_key(obj) -> str:
    """The key an instance is addressed by in the configuration."""
    if not isinstance(obj, dict):
        return ""
    for key in ("local_id", "global_uri"):
        value = obj.get(key)
        if value:
            return str(value)
    return ""


def extract_nested(obj, context: str, allowed_classes: set, parent_label: str = "",
                   titles: dict = None, lang: str = "de",
                   held_back: set = None, collected: dict = None) -> list:
    """Recursively extract class-level examples for allowed classes.

    Instances listed in `held_back` are not written on their own; they are put
    into `collected` so that a composite example can assemble them afterwards.
    """
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
                key = instance_key(item)
                if held_back and key in held_back:
                    collected[key] = item
                else:
                    title = title_for_instance(item, titles or {}, lang)
                    if title:
                        filename = f"{class_name}-{title}.yaml"
                    else:
                        prefix = f"{parent_label}_" if parent_label else ""
                        filename = f"{class_name}-{context}_{prefix}{item_label}.yaml"
                    results.append((filename, item))
            results.extend(extract_nested(item, context, allowed_classes, item_label,
                                          titles, lang, held_back, collected))

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


CLASS_TO_SLOT = {cls: slot for slot, cls in SLOT_TO_CLASS.items()}


def write_composites(composites: list, collected: dict, examples_dir: Path, lang: str):
    """Write one file per composite example, holding all its members.

    The members are wrapped in their container slot, so the file reads like an
    excerpt of a data file and a relation between the instances -- who refers to
    whom -- can be followed within the one listing.
    """
    for composite in composites:
        class_name = composite.get("class")
        slot_name = CLASS_TO_SLOT.get(class_name)
        title = composite.get(lang) or composite.get("de") or ""
        members = [collected[m] for m in (composite.get("members") or []) if m in collected]
        missing = [m for m in (composite.get("members") or []) if m not in collected]
        if missing:
            print(f"  WARNING: composite '{title}' misses members {missing}")
        if not (class_name and slot_name and title and members):
            print(f"  WARNING: composite '{title}' skipped (class/slot/title/members missing)")
            continue
        filename = f"{class_name}-{slugify(title)}.yaml"
        with open(examples_dir / filename, "w", encoding="utf-8") as f:
            yaml.dump({slot_name: members}, f, default_flow_style=False,
                      allow_unicode=True, sort_keys=False, width=YAML_WIDTH)
        print(f"  {filename}  (composite of {len(members)})")


def extract(ech_folder: str):
    base = Path(ech_folder)
    input_dir = base / "input"
    output_dir = base / "output"
    examples_dir = output_dir / "examples"

    config = load_config(base)
    allowed_classes = set(config.get("classes", []))
    allowed_slots = set(config.get("slots", []))
    max_examples = config.get("max_examples_per_slot", 3)
    example_titles = config.get("example_titles", {}) or {}
    # The same example files are used for every document language, so their names
    # -- which gen-doc renders as the heading -- are written in the schema
    # language (English) rather than duplicated per language.
    title_lang = config.get("example_title_language", "en")
    # Composite examples show several instances together -- the only way to make
    # a relation between them, such as parent_groups, visible in one listing.
    composites = config.get("composite_examples") or []
    held_back = {m for c in composites for m in (c.get("members") or [])}
    collected = {}

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
        extracted = extract_nested(data, stem, allowed_classes,
                                   titles=example_titles, lang=title_lang,
                                   held_back=held_back, collected=collected)
        for filename, item in extracted:
            filepath = examples_dir / filename
            with open(filepath, "w", encoding="utf-8") as f:
                yaml.dump(item, f, default_flow_style=False,
                          allow_unicode=True, sort_keys=False, width=YAML_WIDTH)
            print(f"  {filename}")

        # Slot values
        if allowed_slots:
            collect_slot_values(data, allowed_slots, slot_values)

    write_composites(composites, collected, examples_dir, title_lang)

    print(f"\nClass examples written to {examples_dir}")

    # Enriched schema
    if allowed_slots and slot_values:
        schema_path = input_dir / "schema.yaml"
        enriched_path = output_dir / "pipeline_examples_generator_schema.yaml"
        enrich_schema(schema_path, enriched_path, slot_values, max_examples)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python .github/workflows/scripts/extract_examples.py <ech-folder>")
        sys.exit(1)
    extract(sys.argv[1])
