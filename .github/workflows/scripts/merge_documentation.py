import os
import sys
import re
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - yaml ships with the CI image
    yaml = None

def modify_header(content):
    """
    Modifies the header of the content to include a local id. 
    Looks for headers in the format `# Class: AgendaItem` 
    and replaces them with `# Class: AgendaItem{#AgendaItem}`
    so that they can be linked to in the documentation.

    Args:
        content (str): The content of the markdown file.

    Returns:
        str: The modified content with the header.
    """

    # Lines of the form "## Klasse: Person" / "# Slot: local_id" / "# Typ: String".
    # The keyword is localized by the docgen templates and the heading level
    # differs by element kind (classes and enums are h2, slots and types h1);
    # gen-doc also leaves a trailing space. Matching only "# Class: X" -- as an
    # earlier version did -- therefore produced no anchor at all, and every
    # cross-reference in the document pointed nowhere.
    pattern = r"^(#{1,3} (?:Klasse|Classe|Class|Slot|Enum|Typ|Type)\s*:\s*(\w+))[ \t]*$"

    # The anchor is an empty inline span, not a heading attribute. Pandoc turns
    # a heading attribute into a `bookmarkStart` *before* the heading paragraph,
    # and where the preceding element is a table -- which is the normal case
    # here, since every element doc ends with one -- LibreOffice discards that
    # bookmark when converting the DOCX to PDF. Every cross-reference into such
    # a section then leads nowhere in the PDF, while it still works in Word. As
    # an inline span the bookmark sits inside the heading paragraph and survives.
    def replace_header(match):
        name = match.group(2)
        return f"{match.group(1)} []{{#{name}}}"

    # Replace all headers in the content
    return re.sub(pattern, replace_header, content, flags=re.MULTILINE)

def modify_links(content):
    """
    Modifies the links in the content from external markdown links to internal links. 
    Looks for links in the format `[AgendaItem](AgendaItem.md)` 
    and replaces them with `[AgendaItem](#AgendaItem)`

    Args:
        content (str): The content of the markdown file.

    Returns:
        str: The modified content with the links.
    """
    # Regular expression pattern to match links in the format [AgendaItem](AgendaItem.md)
    pattern = r"\[(.*?)\]\((.*?)\.md\)"

    # Function to replace the matched link with the modified link
    def replace_link(match):
        name = match.group(1)
        return f"[{name}](#{name})"

    # Replace all links in the content
    return re.sub(pattern, replace_link, content)

def demote_headings(content):
    """Push every heading of an included file one level down.

    Without it the generated `## Klasse: Meeting` sits at the same level as the
    authored `## Meeting (Einzelne Sitzung)` that introduces it, so Word numbers
    the two as sibling sections and the prose reads as a chapter of its own
    rather than as the lead-in to the class it describes.

    Headings inside fenced code blocks are left alone: the LinkML source and the
    YAML examples both contain comment lines starting with `#`, which are not
    headings. Level 6 is the deepest ATX heading, so it stays as it is.
    """
    out, in_fence = [], False
    for line in content.split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        elif not in_fence and re.match(r"^#{1,5} ", line):
            line = "#" + line
        out.append(line)
    return "\n".join(out)


def process_includes(file_link, lang=None, demote=False):
    """
    Opens the file from the given link, reads its content,
    makes the inclusions and modifies the header and links
    in the inclusions and writes the final content to a new file.

    Args:
        file_link (str): The link to the markdown file that
        contains the include directives.
        lang (str): Optional language code. When set, include paths pointing
        to `.../output/docs/...` are redirected to the per-language docs
        directory `.../output/docs/<lang>/...`, so the same language-agnostic
        include directive resolves to the localized generated docs.
        demote (bool): When true, the headings of every included file are
        pushed one level down, so a generated element doc becomes a subsection
        of the authored section that introduces it. Off by default -- a
        document written against the flat layout keeps its structure.
    """
    # Read the content of the file
    with open(file_link, 'r', encoding='utf-8') as f:
        content = f.read()

    # For all includes
    # Pattern of include directive
    include_pattern = r"\{\{include:(?:'([^']+)'|([^\}]+))\}\}"
    # Build a list with all the includes results are tuples
    includes = re.findall(include_pattern, content)
    # For each include, read the file and replace the include directive with the content
    for include in includes:
        # The path as written in the directive (quoted or unquoted variant)
        inc_path = include[1] if include[1] else include[0]
        # For a localized build, read the generated docs from output/docs/<lang>/
        read_path = inc_path.replace('/output/docs/', f'/output/docs/{lang}/') if lang else inc_path
        # Read the content of the included file
        with open(read_path, 'r', encoding='utf-8') as f:
            raw_content = f.read()
            raw_content = modify_header(raw_content)
            raw_content = modify_links(raw_content)
            if demote:
                raw_content = demote_headings(raw_content)
            # Replace the include directive with the content of the included file
            directive = f"{{{{include:{inc_path}}}}}" if include[1] else f"{{{{include:'{inc_path}'}}}}"
            content = content.replace(directive, raw_content)

    return content

def slugify(text):
    """Mirror of `slugify()` in extract_examples.py.

    The example file names are built from the title with that function, and
    gen-doc turns the file name back into the heading. To match a heading to
    its configured title, the same transformation has to be applied here —
    matching on the raw title would fail wherever it contains punctuation
    (brackets, apostrophes) or exceeds the length limit.
    """
    text = text.replace(" ", "_").replace("/", "_").replace(".", "_")
    text = re.sub(r"[^A-Za-z0-9_-]", "", text)
    return text[:80]


def localize_example_headings(content, path, lang):
    """Translate the example headings into `lang`.

    gen-doc derives the heading of an example from its file name, and the same
    example files are used for every language. The titles themselves live in
    `input/pipeline_examples_generator_config.yaml` under `example_titles`,
    keyed by the instance's `local_id` and given per language. Here the heading
    that gen-doc produced is swapped for the one of the target language.
    """
    if not lang or yaml is None:
        return content

    config_path = Path(path) / "input" / "pipeline_examples_generator_config.yaml"
    if not config_path.exists():
        return content
    with open(config_path, encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}

    titles = config.get("example_titles") or {}
    source_lang = config.get("example_title_language", "en")

    # Composite examples carry their titles inline rather than keyed by an
    # instance, but their headings are localized in exactly the same way.
    entries = list(titles.values()) + list(config.get("composite_examples") or [])

    # Heading as written by gen-doc -> title in the target language.
    mapping = {}
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        written = entry.get(source_lang)
        wanted = entry.get(lang)
        if written and wanted and written != wanted:
            mapping[slugify(written).replace("_", " ")] = wanted

    if not mapping:
        return content

    def repl(m):
        prefix, heading = m.group(1), m.group(2).strip()
        # The class prefix ("Person-") is already stripped by the template.
        return f"{prefix}{mapping.get(heading, heading)}"

    return re.sub(r"(^#### [^:]+:\s*)(.+)$", repl, content, flags=re.M)


def unlink_dangling_targets(content):
    """Turn cross-references without a target back into plain text.

    `modify_links()` rewrites every generated link into a document-internal
    one, including links to elements that are not part of the document -- the
    built-in types (String, Date, Boolean) and the per-slot pages, which are
    not included anywhere. In Word and PDF those render as blue link text that
    leads nowhere, which is worse than no link: the reader tries it. Only
    references whose anchor was actually written survive as links.
    """
    anchors = set(re.findall(r"\{#([A-Za-z_]\w*)\}", content))

    def repl(match):
        text, target = match.group(1), match.group(2)
        return match.group(0) if target in anchors else text

    return re.sub(r"\[([^\]]+)\]\(#([A-Za-z_]\w*)\)", repl, content)


def process_folder(path, lang=None, demote=False):
    """
    Processes all markdown files in the given folder and applies the modifications.

    Args:
        path (str): The path to the folder containing the markdown files.
        lang (str): Optional language code (e.g. 'de', 'fr', 'en'). When set,
        prose is read from `<path>/input/<lang>/` and the merged output is
        written to `documentation_merged_<lang>.md`. Without it, the original
        single-language behaviour applies (`<path>/input/`).
        demote (bool): Passed on to `process_includes()`. Set per standard --
        eCH-0293 introduces every element doc with a section of its own and
        wants them nested; the other documents keep the flat layout.
    """
    content = ""

    # Set your target directory (per-language subfolder when lang is given)
    input_dir = f"{path}/input/{lang}" if lang else f"{path}/input"
    directory = Path(input_dir)

    # Find all markdown files (non-recursive)
    md_files = sorted([f.name for f in directory.glob('*.md')])

    for file in md_files:
        content += process_includes(f"{input_dir}/{file}", lang, demote) + "\n"

    content = localize_example_headings(content, path, lang)
    content = unlink_dangling_targets(content)

    # Write the modified content to a new file
    suffix = f"_{lang}" if lang else ""
    output_file = f"{path}/output/documentation_merged{suffix}.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--demote-includes"]
    demote = "--demote-includes" in sys.argv[1:]

    if len(args) not in (1, 2):
        print("Usage: python .github/workflows/scripts/merge_documentation.py "
              "<path> [lang] [--demote-includes]")
        sys.exit(1)

    path = args[0]
    lang = args[1] if len(args) == 2 else None
    process_folder(path, lang, demote)