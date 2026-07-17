import os
import sys
import re
from pathlib import Path

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

    # Regular expression pattern to match lines starting with "# <Keyword>: <Name>"
    pattern = r"^(# (Class|Slot|Enum|Type): (\w+))$"

    # Function to replace the matched header with the modified header
    def replace_header(match):
        keyword = match.group(2)
        name = match.group(3)
        return f"{match.group(1)}{{#{name}}}"

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

def process_includes(file_link, lang=None):
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
            # Replace the include directive with the content of the included file
            directive = f"{{{{include:{inc_path}}}}}" if include[1] else f"{{{{include:'{inc_path}'}}}}"
            content = content.replace(directive, raw_content)

    return content

def process_folder(path, lang=None):
    """
    Processes all markdown files in the given folder and applies the modifications.

    Args:
        path (str): The path to the folder containing the markdown files.
        lang (str): Optional language code (e.g. 'de', 'fr', 'en'). When set,
        prose is read from `<path>/input/<lang>/` and the merged output is
        written to `documentation_merged_<lang>.md`. Without it, the original
        single-language behaviour applies (`<path>/input/`).
    """
    content = ""

    # Set your target directory (per-language subfolder when lang is given)
    input_dir = f"{path}/input/{lang}" if lang else f"{path}/input"
    directory = Path(input_dir)

    # Find all markdown files (non-recursive)
    md_files = sorted([f.name for f in directory.glob('*.md')])

    for file in md_files:
        content += process_includes(f"{input_dir}/{file}", lang) + "\n"

    # Write the modified content to a new file
    suffix = f"_{lang}" if lang else ""
    output_file = f"{path}/output/documentation_merged{suffix}.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        print("Usage: python merge_documentation.py <path> [lang]")
        sys.exit(1)

    path = sys.argv[1]
    lang = sys.argv[2] if len(sys.argv) == 3 else None
    process_folder(path, lang)