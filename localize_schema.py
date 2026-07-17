#!/usr/bin/env python3
"""
localize_schema.py <input_schema.yaml> <lang> <output_schema.yaml>

Produce a language-specific copy of a LinkML schema for `gen-doc`. For every
element (schema, class, slot, enum, permissible value, type, subset) that carries
a `annotations.description_<lang>`, its `description` is replaced by that
translation. Elements without a translation keep their English `description`
(fallback), so untranslated parts surface as English in an otherwise translated
document.

`lang` is a two-letter code: `de`, `fr` (or `en`, which is a no-op — English
already lives in `description`).

This runs after extract_examples.py (so injected `examples:` are preserved) and
before gen-doc, once per target language. The output is a generated artifact.
"""
import sys

import yaml


def annotation_value(ann_value):
    """An annotation may be a plain string or a {tag, value} mapping."""
    if isinstance(ann_value, dict):
        return ann_value.get("value")
    return ann_value


def localize(node, lang):
    """Recursively swap `description` -> `description_<lang>` where present."""
    if isinstance(node, dict):
        ann = node.get("annotations")
        if isinstance(ann, dict):
            key = f"description_{lang}"
            if key in ann:
                translated = annotation_value(ann[key])
                if translated:
                    node["description"] = translated
        for value in node.values():
            localize(value, lang)
    elif isinstance(node, list):
        for item in node:
            localize(item, lang)


def main():
    if len(sys.argv) != 4:
        print("usage: localize_schema.py <input.yaml> <lang> <output.yaml>", file=sys.stderr)
        sys.exit(2)
    input_path, lang, output_path = sys.argv[1], sys.argv[2], sys.argv[3]

    with open(input_path, encoding="utf-8") as f:
        schema = yaml.safe_load(f)

    if lang != "en":
        localize(schema, lang)

    with open(output_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(schema, f, allow_unicode=True, sort_keys=False, width=4096)
    print(f"localize_schema.py: wrote {output_path} ({lang})")


if __name__ == "__main__":
    main()
