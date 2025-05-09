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

def process_includes(file_link):
    """
    Opens the file from the given link, reads its content,
    makes the inclusions and modifies the header and links 
    in the inclusions and writes the final content to a new file.
    
    Args:
        file_link (str): The link to the markdown file that
        contains the include directives.
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
        # Read the content of the included file
        with open(include[1], 'r', encoding='utf-8') as f:
            raw_content = f.read()
            raw_content = modify_header(raw_content)
            raw_content = modify_links(raw_content)
            # Replace the include directive with the content of the included file
            content = content.replace(f"{{{{include:{include[1]}}}}}", raw_content)

    return content

def process_folder(path):
    """
    Processes all markdown files in the given folder and applies the modifications.

    Args:
        path (str): The path to the folder containing the markdown files.
    """
    content = ""
    
    # Set your target directory
    directory = Path(path + '/input')

    # Find all markdown files (non-recursive)
    md_files = sorted([f.name for f in directory.glob('*.md')])
    
    for file in md_files:
        content += process_includes(path + '/input/' + file) + "\n"

    # Write the modified content to a new file
    output_file = path + '/output/documentation_merged.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python merge_documentation.py <path>")
        sys.exit(1)

    path = sys.argv[1]
    process_folder(path)