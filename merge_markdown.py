import os
import sys
import re

def merge_markdown(folder):
    """
    Merges all markdown files in a given folder into a single markdown file.

    Args:
        folder (str): The path to the folder containing markdown files.
    """
    
    folder_path = folder + '/output/docs/'

    # Check if the folder exists
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")
    # Check if the folder is a directory
    if not os.path.isdir(folder_path):
        raise NotADirectoryError(f"The path '{folder_path}' is not a directory.")
    # Check if the folder is empty
    if not os.listdir(folder_path):
        raise ValueError(f"The folder '{folder_path}' is empty.")
    # Check if there are markdown files in the folder
    if not any(filename.endswith('.md') for filename in os.listdir(folder_path)):
        raise ValueError(f"No markdown files found in the folder '{folder_path}'.")
    
    # Create a list to store the content of each markdown file
    content = []

    # Iterate through all files in the specified folder
    for filename in os.listdir(folder):
        if filename.endswith('.md'):
            with open(os.path.join(folder, filename), 'r', encoding='utf-8') as f:
                content.append(replace_includes(f.read()))

    # Join all content into a single string
    merged_content = "\n\n".join(content)

    # Replace all include directives with the actual content
    
    # Pattern of include directive
    include_pattern = r'{{< include (.*?) >}}'

    # Write the merged content to a new markdown file
    with open(os.path.join(folder, 'output/merged.md'), 'w', encoding='utf-8') as f:
        f.write(merged_content)

def replace_includes(content):
    """
    Replaces all include directives in the content with the actual content of the included files.

    Args:
        content (str): The content of the markdown file.

    Returns:
        str: The content with all include directives replaced.
    """
    
    # Pattern of include directive
    include_pattern = r'{{include:(.+?)}}'

    # Replace all include directives with the actual content
    def replace_include(match):
        filename = match.group(1).strip()
        print(f"Replacing include directive with content from '{filename}'")
        with open(os.path.join(filename), 'r', encoding='utf-8') as f:
            return f.read()

    return re.sub(include_pattern, replace_include, content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python merge_markdown.py <path>")
        sys.exit(1)

    path = sys.argv[1]
    merge_markdown(path)