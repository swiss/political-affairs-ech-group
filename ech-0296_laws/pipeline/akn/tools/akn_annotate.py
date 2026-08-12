#!/usr/bin/env python3
"""
tools/akn_annotate.py

AKN XML Annotator — generates an HTML viewer with three views:
  .raw  — XML tree structure
  .meta — FRBR metadata table
  .html — Rendered preface and body

Usage:
    python tools/akn_annotate.py document.xml
    python tools/akn_annotate.py tests/BBl-2025-2900-DE.xml -o
"""

from __future__ import annotations

import argparse
import html as html_module
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

from lxml import etree


def strip_ns(tag: str) -> str:
    """Remove namespace prefix: {http://...}name → name"""
    return tag.split("}")[-1] if "}" in tag else tag


def get_tag_color(tag: str) -> str:
    """Assign colors to different tag categories."""
    if tag.startswith("FRBR"):
        return "#2e7d32"
    if tag in ("meta", "identification", "references", "notes"):
        return "#1565c0"
    if tag.startswith("TLC"):
        return "#7b1fa2"
    if tag in ("akomaNtoso", "act", "bill", "doc", "judgment"):
        return "#c41e3a"
    if tag in ("preface", "preamble", "body", "conclusions"):
        return "#e65100"
    if tag in ("chapter", "section", "subsection", "article", "paragraph", "subparagraph"):
        return "#00796b"
    if tag in ("p", "blockList", "item", "num", "heading", "content", "listIntroduction"):
        return "#5d4037"
    if tag in ("span", "ref", "rref", "mref", "b", "i", "u", "sup", "sub", "authorialNote"):
        return "#546e7a"
    return "#37474f"


# ── Side Navigation / Filter System ────────────────────────────────────────────

# FRBR elements that can appear at each level
FRBR_ELEMENTS = {
    "work": ["FRBRthis", "FRBRuri", "FRBRdate", "FRBRauthor", "FRBRcountry", "FRBRnumber", "FRBRname", "FRBRauthoritative", "FRBRsubtype"],
    "expression": ["FRBRthis", "FRBRuri", "FRBRdate", "FRBRauthor", "FRBRlanguage"],
    "manifestation": ["FRBRthis", "FRBRuri", "FRBRdate", "FRBRauthor", "FRBRformat"],
}

# Color coding for FRBR elements
FRBR_COLORS = {
    "FRBRthis": "#1565c0",      # blue
    "FRBRuri": "#1976d2",       # blue
    "FRBRdate": "#2e7d32",      # green
    "FRBRauthor": "#7b1fa2",    # purple
    "FRBRcountry": "#0288d1",   # light blue
    "FRBRnumber": "#e65100",    # orange
    "FRBRname": "#c2185b",      # pink
    "FRBRauthoritative": "#00796b",  # teal
    "FRBRsubtype": "#546e7a",   # grey
    "FRBRlanguage": "#0097a7",  # cyan
    "FRBRformat": "#5d4037",    # brown
}


def extract_side_nav_data(root) -> dict:
    """Extract all data needed for side navigation."""
    data = {
        "frbr_levels": {"work": [], "expression": [], "manifestation": []},
        "references": [],
        "preface_elements": [],
        "body_structure": [],
    }

    # Extract FRBR elements per level
    for elem in root.iter():
        tag = strip_ns(elem.tag)
        parent = elem.getparent()
        parent_tag = strip_ns(parent.tag) if parent is not None else ""

        if parent_tag == "FRBRWork" or tag == "FRBRWork":
            level = "work"
        elif parent_tag == "FRBRExpression" or tag == "FRBRExpression":
            level = "expression"
        elif parent_tag == "FRBRManifestation" or tag == "FRBRManifestation":
            level = "manifestation"
        else:
            level = None

        if level and tag.startswith("FRBR") and tag not in ["FRBRWork", "FRBRExpression", "FRBRManifestation"]:
            # Get value/attribute summary
            val = elem.get("value", "") or elem.get("date", "") or elem.get("language", "")
            if len(val) > 30:
                val = val[:27] + "..."
            data["frbr_levels"][level].append({"tag": tag, "value": val})

    # Extract references (TLC*)
    for elem in root.iter():
        tag = strip_ns(elem.tag)
        if tag.startswith("TLC"):
            href = elem.get("href", "")
            show_as = elem.get("showAs", "")
            # Check if it's a "core" reference (legal-institution, etc)
            is_core = "legal-institution" in href
            data["references"].append({
                "tag": tag,
                "showAs": show_as,
                "href": href,
                "isCore": is_core,
            })

    # Extract preface/preamble elements hierarchically
    def extract_content_tree(parent_elem, depth=0):
        """Recursively extract content elements with depth."""
        items = []
        for child in parent_elem:
            ctag = strip_ns(child.tag)
            text = ""

            if ctag == "p":
                # Check if p contains docTitle
                has_doc_title = any(strip_ns(c.tag) == "docTitle" for c in child)
                if has_doc_title:
                    for sub in child:
                        if strip_ns(sub.tag) == "docTitle":
                            dt_text = get_text(sub)
                            if len(dt_text) > 35:
                                dt_text = dt_text[:32] + "..."
                            items.append({"tag": "docTitle", "text": dt_text, "depth": depth + 1})
                else:
                    p_text = get_text(child)
                    if len(p_text) > 35:
                        p_text = p_text[:32] + "..."
                    items.append({"tag": "p", "text": p_text, "depth": depth})

                    # Check for nested authorialNote
                    for sub in child.iter():
                        stag = strip_ns(sub.tag)
                        if stag == "authorialNote":
                            items.append({"tag": "authorialNote", "text": "", "depth": depth + 1})
                            # Check for ref inside
                            for ref in sub.iter():
                                if strip_ns(ref.tag) == "ref":
                                    ref_text = get_text(ref)
                                    if len(ref_text) > 30:
                                        ref_text = ref_text[:27] + "..."
                                    items.append({"tag": "ref", "text": ref_text, "depth": depth + 2})
                        elif stag == "br":
                            pass  # ignore br

            elif ctag == "docTitle":
                dt_text = get_text(child)
                if len(dt_text) > 35:
                    dt_text = dt_text[:32] + "..."
                items.append({"tag": "docTitle", "text": dt_text, "depth": depth})

            elif ctag == "authorialNote":
                items.append({"tag": "authorialNote", "text": "", "depth": depth})
                for ref in child.iter():
                    if strip_ns(ref.tag) == "ref":
                        ref_text = get_text(ref)
                        if len(ref_text) > 30:
                            ref_text = ref_text[:27] + "..."
                        items.append({"tag": "ref", "text": ref_text, "depth": depth + 1})

        return items

    for elem in root.iter():
        tag = strip_ns(elem.tag)
        if tag == "preface":
            data["preface_elements"].append({"tag": "preface", "id": "preface", "depth": 0})
            data["preface_elements"].extend(extract_content_tree(elem, 1))
        elif tag == "preamble":
            data["preface_elements"].append({"tag": "preamble", "id": "preamble", "depth": 0})
            data["preface_elements"].extend(extract_content_tree(elem, 1))

    # Extract body structure
    for elem in root.iter():
        tag = strip_ns(elem.tag)
        if tag == "chapter":
            eid = elem.get("eId", "")
            num = heading = ""
            for sub in elem:
                if strip_ns(sub.tag) == "num":
                    num = get_text(sub)
                elif strip_ns(sub.tag) == "heading":
                    heading = get_text(sub)
            data["body_structure"].append({"type": "chapter", "eId": eid, "label": f"{num} {heading}".strip()})
        elif tag == "section":
            eid = elem.get("eId", "")
            num = heading = ""
            for sub in elem:
                if strip_ns(sub.tag) == "num":
                    num = get_text(sub)
                elif strip_ns(sub.tag) == "heading":
                    heading = get_text(sub)
            data["body_structure"].append({"type": "section", "eId": eid, "label": f"{num} {heading}".strip()})
        elif tag == "article":
            eid = elem.get("eId", "")
            num = heading = ""
            for sub in elem:
                if strip_ns(sub.tag) == "num":
                    num = get_text(sub)
                elif strip_ns(sub.tag) == "heading":
                    heading = get_text(sub)
            data["body_structure"].append({"type": "article", "eId": eid, "label": f"{num} {heading}".strip()})
        elif tag == "paragraph":
            eid = elem.get("eId", "")
            data["body_structure"].append({"type": "paragraph", "eId": eid, "label": eid})
        elif tag == "item":
            eid = elem.get("eId", "")
            if eid:
                data["body_structure"].append({"type": "item", "eId": eid, "label": eid})
        elif tag == "listIntroduction":
            eid = elem.get("eId", "")
            if eid:
                data["body_structure"].append({"type": "listIntro", "eId": eid, "label": eid})

    return data


def build_side_nav(root, title: str) -> str:
    """Build side navigation with filters and element lists."""
    nav_data = extract_side_nav_data(root)

    # Filters section (renamed from FRBR Levels)
    level_filters = """
    <div class="nav-section">
        <div class="nav-section-title">Filters</div>
        <div class="filter-group">
            <label class="filter-item active" data-filter="work">
                <input type="checkbox" checked> Work
            </label>
            <label class="filter-item active" data-filter="expression">
                <input type="checkbox" checked> Expression
            </label>
            <label class="filter-item active" data-filter="manifestation">
                <input type="checkbox" checked> Manifestation
            </label>
        </div>
        <div class="filter-group" style="margin-top: 8px;">
            <label class="filter-item active" data-filter="number">
                <input type="checkbox" checked> FRBRnumber
            </label>
            <label class="filter-item active" data-filter="name">
                <input type="checkbox" checked> FRBRname
            </label>
        </div>
    </div>"""

    # References - show all, not truncated
    all_refs = nav_data["references"]
    refs_html = ""
    if all_refs:
        refs_items = []
        for r in all_refs:
            href_preview = r["href"][:35] + "..." if len(r["href"]) > 35 else r["href"]
            show = r["showAs"] if r["showAs"] else r["tag"]
            refs_items.append(f'<div class="ref-item" data-href="{html_module.escape(r["href"])}"><span class="ref-tag">&lt;{r["tag"]}&gt;</span> {html_module.escape(show)} <span class="ref-href">{html_module.escape(href_preview)}</span></div>')
        refs_html = f"""
    <div class="nav-section">
        <div class="nav-section-title">References <span class="ref-count">{len(all_refs)}</span></div>
        <div class="refs-list">{"".join(refs_items)}</div>
    </div>"""

    # FRBR Elements per level with color coding
    frbr_elements_html = ""
    for level in ["work", "expression", "manifestation"]:
        present_tags = set(e["tag"] for e in nav_data["frbr_levels"][level])

        items = []
        for tag in FRBR_ELEMENTS[level]:
            color = FRBR_COLORS.get(tag, "#546e7a")
            if tag in present_tags:
                # Find values for this tag
                values = [e["value"] for e in nav_data["frbr_levels"][level] if e["tag"] == tag and e["value"]]
                value_preview = values[0] if values else ""
                if len(value_preview) > 30:
                    value_preview = value_preview[:27] + "..."
                items.append(f'<div class="frbr-elem clickable" data-tag="{tag}" data-level="{level}"><span class="frbr-tag" style="color:{color}">&lt;{tag}&gt;</span> <span class="elem-value">{html_module.escape(value_preview)}</span></div>')
            else:
                items.append(f'<div class="frbr-elem absent"><span class="frbr-tag-absent">&lt;{tag}&gt;</span></div>')

        frbr_elements_html += f"""
        <div class="frbr-level-elements" data-level="{level}">
            <div class="level-label">{level.title()}</div>
            {"".join(items)}
        </div>"""

    frbr_section = f"""
    <div class="nav-section">
        <div class="nav-section-title">FRBR Elements</div>
        {frbr_elements_html}
    </div>"""

    # Preface/Preamble elements - styled like FRBR section with <> tags and preview, hierarchical
    PREFACE_COLORS = {
        "preface": "#e65100",
        "preamble": "#e65100",
        "docTitle": "#c41e3a",
        "p": "#5d4037",
        "authorialNote": "#7b1fa2",
        "ref": "#1565c0",
        "br": "#90a4ae",
    }

    preface_items = []
    for e in nav_data["preface_elements"]:
        tag = e["tag"]
        text = e.get("text", "")
        depth = e.get("depth", 0)
        indent = depth * 12
        color = PREFACE_COLORS.get(tag, "#546e7a")

        if tag in ("preface", "preamble"):
            preface_items.append(f'<div class="frbr-elem clickable" data-id="{e.get("id", "")}" style="padding-left:{indent}px"><span class="frbr-tag" style="color:{color}">&lt;{tag}&gt;</span></div>')
        elif text:
            preface_items.append(f'<div class="frbr-elem clickable" data-tag="{tag}" style="padding-left:{indent}px"><span class="frbr-tag" style="color:{color}">&lt;{tag}&gt;</span> <span class="elem-value">{html_module.escape(text)}</span></div>')
        else:
            preface_items.append(f'<div class="frbr-elem clickable" data-tag="{tag}" style="padding-left:{indent}px"><span class="frbr-tag" style="color:{color}">&lt;{tag}&gt;</span></div>')

    preface_html = f"""
    <div class="nav-section">
        <div class="nav-section-title">Preface / Preamble</div>
        <div class="preface-elements">{"".join(preface_items)}</div>
    </div>""" if preface_items else ""

    # Body structure
    body_items = []
    for e in nav_data["body_structure"]:
        t = e["type"]
        eid = e["eId"]
        label = e["label"]
        if t == "chapter":
            body_items.append(f'<div class="struct-item struct-chapter" data-eid="{eid}">{html_module.escape(label)}</div>')
        elif t == "section":
            body_items.append(f'<div class="struct-item struct-section" data-eid="{eid}">{html_module.escape(label)}</div>')
        elif t == "article":
            short_label = label[:50] + "..." if len(label) > 50 else label
            body_items.append(f'<div class="struct-item struct-article" data-eid="{eid}">{html_module.escape(short_label)}</div>')
        elif t == "paragraph":
            body_items.append(f'<div class="struct-item struct-para" data-eid="{eid}">{eid}</div>')
        elif t == "item":
            body_items.append(f'<div class="struct-item struct-item-li" data-eid="{eid}">{eid}</div>')
        elif t == "listIntro":
            body_items.append(f'<div class="struct-item struct-listintro" data-eid="{eid}">{eid}</div>')

    body_html = f"""
    <div class="nav-section">
        <div class="nav-section-title">Body Structure</div>
        <div class="struct-list body-struct">{"".join(body_items[:100])}</div>
        {"<div class='struct-more'>+" + str(len(body_items) - 100) + " more...</div>" if len(body_items) > 100 else ""}
    </div>""" if body_items else ""

    return f"""
    <div class="nav-header">
        <div class="nav-title">{html_module.escape(title)}</div>
    </div>
    {level_filters}
    {refs_html}
    {frbr_section}
    {preface_html}
    {body_html}
    """


# ── XML Tree Rendering ─────────────────────────────────────────────────────────

def render_tree(elem, depth: int = 0) -> str:
    """Recursively render element as indented tree."""
    tag = strip_ns(elem.tag)
    color = get_tag_color(tag)
    indent = "  " * depth

    # Determine FRBR level for filtering
    parent = elem.getparent()
    parent_tag = strip_ns(parent.tag) if parent is not None else ""
    level_attr = ""
    if tag in ("FRBRWork", "FRBRExpression", "FRBRManifestation"):
        level_attr = f' data-frbr-level="{tag.replace("FRBR", "").lower()}"'
    elif parent_tag == "FRBRWork":
        level_attr = ' data-frbr-level="work"'
    elif parent_tag == "FRBRExpression":
        level_attr = ' data-frbr-level="expression"'
    elif parent_tag == "FRBRManifestation":
        level_attr = ' data-frbr-level="manifestation"'

    # Build attributes string
    attrs = []
    for key, val in elem.attrib.items():
        key = strip_ns(key)
        if len(val) > 60:
            val = val[:57] + "..."
        attrs.append(f'<span class="attr-name">{html_module.escape(key)}</span>=<span class="attr-val">"{html_module.escape(val)}"</span>')
    attrs_str = " " + " ".join(attrs) if attrs else ""

    # Get direct text content
    text = ""
    if elem.text and elem.text.strip():
        text = elem.text.strip()
        if len(text) > 80:
            text = text[:77] + "..."
        text = f'<span class="text-content">{html_module.escape(text)}</span>'

    children = list(elem)
    parts = []

    # Data attributes for highlighting
    data_tag = f' data-tag="{tag}"'

    if children:
        parts.append(f'{indent}<details open{level_attr}{data_tag}>')
        parts.append(f'{indent}  <summary><span class="tag" style="color:{color}">&lt;{html_module.escape(tag)}{attrs_str}&gt;</span>{text}</summary>')
        for child in children:
            parts.append(render_tree(child, depth + 2))
            if child.tail and child.tail.strip():
                tail = child.tail.strip()
                if len(tail) > 80:
                    tail = tail[:77] + "..."
                parts.append(f'{indent}    <span class="text-content">{html_module.escape(tail)}</span>')
        parts.append(f'{indent}  <span class="tag" style="color:{color}">&lt;/{html_module.escape(tag)}&gt;</span>')
        parts.append(f'{indent}</details>')
    else:
        if text:
            parts.append(f'{indent}<div class="leaf"{level_attr}{data_tag}><span class="tag" style="color:{color}">&lt;{html_module.escape(tag)}{attrs_str}&gt;</span>{text}<span class="tag" style="color:{color}">&lt;/{html_module.escape(tag)}&gt;</span></div>')
        else:
            parts.append(f'{indent}<div class="leaf"{level_attr}{data_tag}><span class="tag" style="color:{color}">&lt;{html_module.escape(tag)}{attrs_str} /&gt;</span></div>')

    return "\n".join(parts)


# ── Meta View Rendering ────────────────────────────────────────────────────────

@dataclass
class FRBRData:
    """Extracted FRBR metadata."""
    work_uri: str = ""
    work_this: str = ""
    expr_uri: str = ""
    expr_this: str = ""
    manif_uri: str = ""
    manif_this: str = ""
    dates: list = field(default_factory=list)  # [(name, date), ...]
    numbers: list = field(default_factory=list)  # [(lang, value), ...]
    names: list = field(default_factory=list)  # [(lang, value), ...]
    country: str = ""
    language: str = ""
    format: str = ""
    authoritative: str = ""
    tlc_refs: list = field(default_factory=list)  # [(type, showAs, href), ...]
    # Secondary metadata
    authors: list = field(default_factory=list)  # [(href, role), ...]
    subtype: str = ""
    source: str = ""


def extract_frbr(root) -> FRBRData:
    """Extract FRBR metadata from document."""
    data = FRBRData()

    for elem in root.iter():
        tag = strip_ns(elem.tag)

        # URIs
        if tag == "FRBRthis":
            parent_tag = strip_ns(elem.getparent().tag) if elem.getparent() is not None else ""
            val = elem.get("value", "")
            if "Work" in parent_tag:
                data.work_this = val
            elif "Expression" in parent_tag:
                data.expr_this = val
            elif "Manifestation" in parent_tag:
                data.manif_this = val

        elif tag == "FRBRuri":
            parent_tag = strip_ns(elem.getparent().tag) if elem.getparent() is not None else ""
            val = elem.get("value", "")
            if "Work" in parent_tag:
                data.work_uri = val
            elif "Expression" in parent_tag:
                data.expr_uri = val
            elif "Manifestation" in parent_tag:
                data.manif_uri = val

        elif tag == "FRBRdate":
            data.dates.append((elem.get("name", ""), elem.get("date", "")))

        elif tag == "FRBRnumber":
            lang = elem.get("{http://www.w3.org/XML/1998/namespace}lang", "")
            data.numbers.append((lang, elem.get("value", "")))

        elif tag == "FRBRname":
            lang = elem.get("{http://www.w3.org/XML/1998/namespace}lang", "")
            data.names.append((lang, elem.get("value", "")))

        elif tag == "FRBRcountry":
            data.country = elem.get("value", "")

        elif tag == "FRBRlanguage":
            data.language = elem.get("language", "")

        elif tag == "FRBRformat":
            data.format = elem.get("value", "")

        elif tag == "FRBRauthoritative":
            data.authoritative = elem.get("value", "")

        elif tag.startswith("TLC"):
            data.tlc_refs.append((tag, elem.get("showAs", ""), elem.get("href", "")))

        elif tag == "FRBRauthor":
            href = elem.get("href", "")
            role = elem.get("as", "")
            if href and role:
                data.authors.append((href, role))

        elif tag == "FRBRsubtype":
            data.subtype = elem.get("value", "")

        elif tag == "identification":
            data.source = elem.get("source", "")

    return data


def render_meta_view(data: FRBRData) -> str:
    """Render FRBR metadata as tables."""

    # FRBR levels table
    frbr_rows = f"""
    <tr>
        <td class="label">FRBRthis</td>
        <td class="work">{html_module.escape(data.work_this)}</td>
        <td class="expr">{html_module.escape(data.expr_this)}</td>
        <td class="manif">{html_module.escape(data.manif_this)}</td>
    </tr>
    <tr>
        <td class="label">FRBRuri</td>
        <td class="work">{html_module.escape(data.work_uri)}</td>
        <td class="expr">{html_module.escape(data.expr_uri)}</td>
        <td class="manif">{html_module.escape(data.manif_uri)}</td>
    </tr>"""

    # Dates
    seen_dates = {}
    for name, date in data.dates:
        display_name = name.replace("jolux:", "")
        if display_name not in seen_dates:
            seen_dates[display_name] = date
    for name, date in seen_dates.items():
        frbr_rows += f"""
    <tr>
        <td class="label">FRBRdate<br><small>{html_module.escape(name)}</small></td>
        <td colspan="3">{html_module.escape(date)}</td>
    </tr>"""

    # Country, language, format
    if data.country:
        frbr_rows += f"""
    <tr><td class="label">FRBRcountry</td><td colspan="3">{html_module.escape(data.country)}</td></tr>"""
    if data.language:
        frbr_rows += f"""
    <tr><td class="label">FRBRlanguage</td><td colspan="3">{html_module.escape(data.language)}</td></tr>"""
    if data.format:
        frbr_rows += f"""
    <tr><td class="label">FRBRformat</td><td colspan="3">{html_module.escape(data.format)}</td></tr>"""
    if data.authoritative:
        auth_class = "auth-yes" if data.authoritative == "true" else "auth-no"
        frbr_rows += f"""
    <tr><td class="label">FRBRauthoritative</td><td colspan="3" class="{auth_class}">{html_module.escape(data.authoritative)}</td></tr>"""

    # Numbers table - deduplicated by value
    numbers_html = ""
    if data.numbers:
        seen_values = {}
        for lang, val in data.numbers:
            if val not in seen_values:
                seen_values[val] = lang
        rows = "".join(f'<tr><td class="lang">{html_module.escape(lang)}</td><td>{html_module.escape(val)}</td></tr>' for val, lang in seen_values.items())
        numbers_html = f"""
        <h3>FRBRnumber (document identifiers)</h3>
        <table class="meta-table compact">{rows}</table>"""

    # Names table - deduplicated by value
    names_html = ""
    if data.names:
        seen_values = {}
        for lang, val in data.names:
            if val not in seen_values:
                seen_values[val] = lang
        rows = "".join(f'<tr><td class="lang">{html_module.escape(lang)}</td><td>{html_module.escape(val)}</td></tr>' for val, lang in seen_values.items())
        names_html = f"""
        <h3>FRBRname (document titles)</h3>
        <table class="meta-table compact">{rows}</table>"""

    # TLC refs
    tlc_html = ""
    if data.tlc_refs:
        rows = "".join(f'<tr><td class="type">{html_module.escape(t)}</td><td>{html_module.escape(s)}</td><td class="href"><a href="{html_module.escape(h)}">{html_module.escape(h[:60])}...</a></td></tr>' for t, s, h in data.tlc_refs if s)
        if rows:
            tlc_html = f"""
        <h3>TLC References</h3>
        <table class="meta-table compact">{rows}</table>"""

    # Secondary metadata section
    secondary_rows = []

    if data.source:
        secondary_rows.append(f'<tr><td>Source</td><td>{html_module.escape(data.source)}</td></tr>')

    if data.subtype:
        secondary_rows.append(f'<tr><td>FRBRsubtype</td><td>{html_module.escape(data.subtype)}</td></tr>')

    # Deduplicate authors by href+role
    seen_authors = set()
    for href, role in data.authors:
        key = f"{href}|{role}"
        if key not in seen_authors:
            seen_authors.add(key)
            role_display = role.replace("#", "")
            secondary_rows.append(f'<tr><td>FRBRauthor</td><td><span class="author-role">{html_module.escape(role_display)}</span> {html_module.escape(href)}</td></tr>')

    secondary_html = ""
    if secondary_rows:
        secondary_html = f"""
        <div class="secondary-meta">
            <h3>Additional Metadata</h3>
            <table class="meta-table compact secondary">{"".join(secondary_rows)}</table>
        </div>"""

    return f"""
    <h3>FRBR Levels</h3>
    <table class="meta-table frbr">
        <thead>
            <tr>
                <th></th>
                <th class="work">Work</th>
                <th class="expr">Expression</th>
                <th class="manif">Manifestation</th>
            </tr>
        </thead>
        <tbody>{frbr_rows}</tbody>
    </table>
    {numbers_html}
    {names_html}
    {tlc_html}
    {secondary_html}
    """


# ── HTML View Rendering ────────────────────────────────────────────────────────

def get_text(elem) -> str:
    """Get all text content from element."""
    if elem is None:
        return ""
    return re.sub(r'\s+', ' ', "".join(elem.itertext()).strip())


def build_toc(root) -> list:
    """Build table of contents from document structure."""
    toc = []

    # Find preface
    for elem in root.iter():
        if strip_ns(elem.tag) == "preface":
            toc.append({"id": "preface", "type": "preface", "label": "Preface", "level": 0})
            break

    # Find preamble
    for elem in root.iter():
        if strip_ns(elem.tag) == "preamble":
            toc.append({"id": "preamble", "type": "preamble", "label": "Preamble", "level": 0})
            break

    # Find body structure
    for elem in root.iter():
        if strip_ns(elem.tag) == "body":
            toc.append({"id": "body", "type": "body", "label": "Body", "level": 0})
            _build_body_toc(elem, toc)
            break

    return toc


def _build_body_toc(elem, toc: list):
    """Recursively build TOC from body elements."""
    for child in elem:
        tag = strip_ns(child.tag)

        if tag == "chapter":
            eid = child.get("eId", "")
            num = heading = ""
            for sub in child:
                if strip_ns(sub.tag) == "num":
                    num = get_text(sub)
                elif strip_ns(sub.tag) == "heading":
                    heading = get_text(sub)
            toc.append({"id": eid, "type": "chapter", "label": f"{num} {heading}".strip(), "level": 1})
            _build_body_toc(child, toc)

        elif tag == "section":
            eid = child.get("eId", "")
            num = heading = ""
            for sub in child:
                if strip_ns(sub.tag) == "num":
                    num = get_text(sub)
                elif strip_ns(sub.tag) == "heading":
                    heading = get_text(sub)
            toc.append({"id": eid, "type": "section", "label": f"{num} {heading}".strip(), "level": 2})
            _build_body_toc(child, toc)

        elif tag == "article":
            eid = child.get("eId", "")
            num = heading = ""
            for sub in child:
                if strip_ns(sub.tag) == "num":
                    num = get_text(sub)
                elif strip_ns(sub.tag) == "heading":
                    heading = get_text(sub)
            label = f"{num} {heading}".strip() if heading else num
            toc.append({"id": eid, "type": "article", "label": label, "level": 3})


def render_toc_nav(toc: list) -> str:
    """Render TOC as navigation HTML."""
    items = []
    for entry in toc:
        indent = entry["level"] * 12
        type_class = entry["type"]
        items.append(f'<a href="#{entry["id"]}" class="toc-item toc-{type_class}" style="padding-left:{indent + 12}px">{html_module.escape(entry["label"])}</a>')
    return "\n".join(items)


def render_html_view(root) -> str:
    """Render preface and body as HTML."""
    parts = []

    # Find preface
    for elem in root.iter():
        if strip_ns(elem.tag) == "preface":
            parts.append('<div class="preface" id="preface">')
            parts.append('<h2>Preface</h2>')
            parts.append(render_content_element(elem))
            parts.append('</div>')
            break

    # Find preamble
    for elem in root.iter():
        if strip_ns(elem.tag) == "preamble":
            parts.append('<div class="preamble" id="preamble">')
            parts.append('<h2>Preamble</h2>')
            parts.append(render_content_element(elem))
            parts.append('</div>')
            break

    # Find body
    for elem in root.iter():
        if strip_ns(elem.tag) == "body":
            parts.append('<div class="body" id="body">')
            parts.append('<h2>Body</h2>')
            parts.append(render_body_element(elem))
            parts.append('</div>')
            break

    return "\n".join(parts)


def render_content_element(elem) -> str:
    """Render preface/preamble content."""
    parts = []
    for child in elem:
        tag = strip_ns(child.tag)
        if tag == "p":
            text = get_text(child)
            parts.append(f'<p>{html_module.escape(text)}</p>')
        elif tag == "docTitle":
            text = get_text(child)
            parts.append(f'<h1 class="doc-title">{html_module.escape(text)}</h1>')
        elif tag == "authorialNote":
            # Inline footnote
            ref = None
            for sub in child.iter():
                if strip_ns(sub.tag) == "ref":
                    ref = sub
                    break
            if ref is not None:
                href = ref.get("href", "")
                text = get_text(ref)
                parts.append(f'<sup><a href="{html_module.escape(href)}">{html_module.escape(text)}</a></sup>')
    return "\n".join(parts)


def render_body_element(elem) -> str:
    """Render body content with structure."""
    parts = []

    for child in elem:
        tag = strip_ns(child.tag)

        if tag == "chapter":
            num = heading = ""
            for sub in child:
                if strip_ns(sub.tag) == "num":
                    num = get_text(sub)
                elif strip_ns(sub.tag) == "heading":
                    heading = get_text(sub)
            parts.append(f'<div class="chapter">')
            parts.append(f'<h3 class="chapter-title">{html_module.escape(num)} {html_module.escape(heading)}</h3>')
            parts.append(render_body_element(child))
            parts.append('</div>')

        elif tag == "section":
            num = heading = ""
            for sub in child:
                if strip_ns(sub.tag) == "num":
                    num = get_text(sub)
                elif strip_ns(sub.tag) == "heading":
                    heading = get_text(sub)
            parts.append(f'<div class="section">')
            parts.append(f'<h4 class="section-title">{html_module.escape(num)} {html_module.escape(heading)}</h4>')
            parts.append(render_body_element(child))
            parts.append('</div>')

        elif tag == "article":
            eid = child.get("eId", "")
            num = heading = ""
            for sub in child:
                if strip_ns(sub.tag) == "num":
                    num = get_text(sub)
                elif strip_ns(sub.tag) == "heading":
                    heading = get_text(sub)
            parts.append(f'<div class="article" id="{html_module.escape(eid)}">')
            parts.append(f'<div class="article-header"><span class="art-num">{html_module.escape(num)}</span> <span class="art-heading">{html_module.escape(heading)}</span></div>')
            parts.append(render_body_element(child))
            parts.append('</div>')

        elif tag == "paragraph":
            eid = child.get("eId", "")
            num = ""
            content = ""
            for sub in child:
                if strip_ns(sub.tag) == "num":
                    num = get_text(sub)
                elif strip_ns(sub.tag) == "content":
                    content = render_paragraph_content(sub)
            parts.append(f'<div class="paragraph" id="{html_module.escape(eid)}">')
            if num:
                parts.append(f'<span class="para-num">{html_module.escape(num)}</span>')
            parts.append(f'<span class="para-content">{content}</span>')
            parts.append('</div>')

    return "\n".join(parts)


def render_paragraph_content(elem) -> str:
    """Render paragraph content including lists."""
    parts = []

    for child in elem:
        tag = strip_ns(child.tag)

        if tag == "p":
            text = get_text(child)
            parts.append(f'<p>{html_module.escape(text)}</p>')

        elif tag == "blockList":
            intro = ""
            items_html = []
            for sub in child:
                if strip_ns(sub.tag) == "listIntroduction":
                    intro = get_text(sub)
                elif strip_ns(sub.tag) == "item":
                    item_num = ""
                    item_content = []
                    has_nested = False
                    for item_child in sub:
                        item_tag = strip_ns(item_child.tag)
                        if item_tag == "num":
                            item_num = get_text(item_child)
                        elif item_tag == "p":
                            item_content.append(get_text(item_child))
                        elif item_tag == "blockList":
                            has_nested = True
                            item_content.append(render_paragraph_content(sub))

                    item_text = " ".join(item_content) if not has_nested else "".join(item_content)
                    if item_num or item_text:
                        # Inline format: "a. text" or "1. text"
                        items_html.append(f'<div class="list-item"><span class="item-num">{html_module.escape(item_num)}</span>{item_text}</div>')

            if intro:
                parts.append(f'<p class="list-intro">{html_module.escape(intro)}</p>')
            parts.append('<div class="block-list">')
            parts.extend(items_html)
            parts.append('</div>')

    return "\n".join(parts)


# ── Main HTML Generation ───────────────────────────────────────────────────────

def generate_html(xml_content: bytes, source_title: str = "AKN Document") -> str:
    """Generate HTML with three views and side navigation."""
    root = etree.fromstring(xml_content)

    # Build views
    side_nav = build_side_nav(root, source_title)
    tree_html = render_tree(root)
    frbr_data = extract_frbr(root)
    meta_html = render_meta_view(frbr_data)
    html_view = render_html_view(root)
    toc = build_toc(root)
    toc_nav = render_toc_nav(toc)

    # Count elements
    total_tags = sum(1 for _ in root.iter())

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{html_module.escape(source_title)}</title>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      font-size: 14px;
      line-height: 1.5;
      color: #263238;
      background: #f5f5f5;
      display: flex;
      height: 100vh;
    }}

    /* Side Navigation */
    .side-nav {{
      width: 260px;
      background: #263238;
      color: #eceff1;
      overflow-y: auto;
      flex-shrink: 0;
    }}

    .nav-header {{
      padding: 12px 14px;
      border-bottom: 1px solid #37474f;
    }}

    .nav-title {{
      font-size: 13px;
      font-weight: 600;
      word-break: break-word;
    }}

    .nav-section {{
      padding: 12px 14px;
      border-bottom: 1px solid #37474f;
    }}

    .nav-section-title {{
      font-size: 10px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: #78909c;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .ref-count {{
      background: #37474f;
      padding: 1px 5px;
      border-radius: 8px;
      font-size: 9px;
    }}

    /* Filters */
    .filter-group {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }}

    .filter-item {{
      display: flex;
      align-items: center;
      gap: 4px;
      font-size: 11px;
      padding: 4px 8px;
      background: #37474f;
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.15s;
    }}

    .filter-item input {{
      display: none;
    }}

    .filter-item.active {{
      background: #455a64;
    }}

    .filter-item:not(.active) {{
      opacity: 0.5;
    }}

    /* References */
    .refs-list {{
      display: flex;
      flex-direction: column;
      gap: 2px;
      max-height: 200px;
      overflow-y: auto;
    }}

    .ref-item {{
      font-size: 11px;
      padding: 3px 8px;
      background: #37474f;
      border-radius: 3px;
      cursor: pointer;
    }}

    .ref-item:hover {{
      background: #455a64;
    }}

    .ref-tag {{
      font-family: "SF Mono", Monaco, monospace;
      font-size: 10px;
      color: #7b1fa2;
    }}

    .ref-href {{
      display: block;
      font-size: 9px;
      color: #607d8b;
      margin-top: 2px;
      word-break: break-all;
    }}

    /* FRBR Elements */
    .frbr-level-elements {{
      margin-bottom: 10px;
    }}

    .level-label {{
      font-size: 10px;
      color: #78909c;
      margin-bottom: 4px;
      text-transform: uppercase;
    }}

    .frbr-elem {{
      font-size: 11px;
      padding: 3px 8px;
      margin: 2px 0;
      border-radius: 3px;
    }}

    .frbr-elem.clickable {{
      background: #37474f;
      cursor: pointer;
    }}

    .frbr-elem.clickable:hover {{
      background: #455a64;
    }}

    .frbr-elem.absent {{
      color: #455a64;
      opacity: 0.5;
    }}

    .frbr-tag {{
      font-family: "SF Mono", Monaco, monospace;
      font-size: 10px;
    }}

    .frbr-tag-absent {{
      font-family: "SF Mono", Monaco, monospace;
      font-size: 10px;
      color: #546e7a;
    }}

    .elem-value {{
      color: #90a4ae;
      font-size: 10px;
      margin-left: 4px;
    }}

    .preface-elements {{
      display: flex;
      flex-direction: column;
      gap: 2px;
      max-height: 250px;
      overflow-y: auto;
    }}

    /* Structure list */
    .struct-list {{
      display: flex;
      flex-direction: column;
      gap: 2px;
      max-height: 200px;
      overflow-y: auto;
    }}

    .struct-list.body-struct {{
      max-height: 300px;
    }}

    .struct-item {{
      font-size: 11px;
      padding: 3px 8px;
      border-radius: 3px;
      cursor: pointer;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .struct-item:hover {{
      background: #37474f;
    }}

    .struct-top {{
      font-weight: 600;
      color: #e65100;
    }}

    .struct-title {{
      color: #fff;
    }}

    .struct-p {{
      color: #90a4ae;
      padding-left: 16px;
    }}

    .struct-note {{
      color: #78909c;
      padding-left: 16px;
      font-style: italic;
    }}

    .struct-chapter {{
      font-weight: 600;
      color: #c41e3a;
      margin-top: 6px;
    }}

    .struct-section {{
      color: #eceff1;
      padding-left: 12px;
    }}

    .struct-article {{
      color: #90a4ae;
      padding-left: 24px;
    }}

    .struct-para {{
      color: #607d8b;
      padding-left: 36px;
      font-size: 10px;
    }}

    .struct-item-li {{
      color: #546e7a;
      padding-left: 48px;
      font-size: 10px;
    }}

    .struct-listintro {{
      color: #546e7a;
      padding-left: 48px;
      font-size: 10px;
      font-style: italic;
    }}

    .struct-more {{
      font-size: 10px;
      color: #607d8b;
      margin-top: 6px;
      font-style: italic;
    }}

    /* Highlighting */
    .highlighted {{
      background: #ffeb3b !important;
      color: #263238 !important;
    }}

    .greyed-out {{
      opacity: 0.3;
    }}

    /* Main Content */
    .main {{
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }}

    /* Tab Bar */
    .tabs {{
      display: flex;
      background: #fff;
      border-bottom: 1px solid #e0e0e0;
      padding: 0 16px;
    }}

    .tab {{
      padding: 12px 20px;
      cursor: pointer;
      border-bottom: 2px solid transparent;
      font-weight: 500;
      color: #607d8b;
      transition: all 0.15s;
    }}

    .tab:hover {{
      color: #263238;
    }}

    .tab.active {{
      color: #1565c0;
      border-bottom-color: #1565c0;
    }}

    .tab-info {{
      margin-left: auto;
      padding: 12px 0;
      color: #90a4ae;
      font-size: 12px;
    }}

    /* View Panels */
    .view {{
      display: none;
      flex: 1;
      overflow: auto;
      background: #fff;
    }}

    .view.active {{
      display: block;
    }}

    /* Raw View (Tree) */
    .tree {{
      padding: 20px;
      font-family: "SF Mono", Monaco, "Roboto Mono", monospace;
      font-size: 12px;
      line-height: 1.6;
    }}

    details {{
      margin-left: 16px;
    }}

    details > summary {{
      cursor: pointer;
      list-style: none;
      margin-left: -16px;
    }}

    details > summary::-webkit-details-marker {{ display: none; }}

    details > summary::before {{
      content: "▶";
      display: inline-block;
      width: 14px;
      color: #90a4ae;
      font-size: 9px;
    }}

    details[open] > summary::before {{ content: "▼"; }}

    .leaf {{
      margin-left: 16px;
      padding-left: 14px;
    }}

    .tag {{ font-weight: 500; }}
    .attr-name {{ color: #6a1b9a; }}
    .attr-val {{ color: #0277bd; }}

    .text-content {{
      background: #fff9c4;
      padding: 1px 4px;
      border-radius: 2px;
      margin-left: 6px;
    }}

    /* Meta View */
    .meta-view {{
      padding: 24px;
      max-width: 1000px;
    }}

    .meta-view h3 {{
      font-size: 14px;
      color: #263238;
      margin: 24px 0 12px;
      padding-bottom: 6px;
      border-bottom: 1px solid #e0e0e0;
    }}

    .meta-view h3:first-child {{ margin-top: 0; }}

    .meta-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 12px;
    }}

    .meta-table th, .meta-table td {{
      padding: 8px 12px;
      border: 1px solid #e0e0e0;
      text-align: left;
      vertical-align: top;
    }}

    .meta-table th {{
      background: #f5f5f5;
      font-weight: 600;
    }}

    .meta-table .label {{
      background: #fafafa;
      font-weight: 500;
      width: 140px;
    }}

    .meta-table .work {{ background: #e8f5e9; }}
    .meta-table .expr {{ background: #e3f2fd; }}
    .meta-table .manif {{ background: #fff3e0; }}

    .meta-table .lang {{
      font-weight: 600;
      color: #1565c0;
      width: 40px;
    }}

    .meta-table .type {{
      color: #7b1fa2;
      width: 120px;
    }}

    .meta-table .href {{
      font-size: 11px;
      word-break: break-all;
    }}

    .meta-table.compact td {{ padding: 6px 10px; }}

    .auth-yes {{ background: #e8f5e9; color: #2e7d32; font-weight: 600; }}
    .auth-no {{ background: #ffebee; color: #c62828; }}

    .secondary-meta {{
      margin-top: 32px;
      padding-top: 24px;
      border-top: 1px solid #e0e0e0;
    }}

    .secondary-meta h3 {{
      color: #90a4ae;
    }}

    .meta-table.secondary td {{
      color: #78909c;
      background: #fafafa;
    }}

    .author-role {{
      background: #eceff1;
      padding: 1px 6px;
      border-radius: 3px;
      font-size: 10px;
      margin-right: 6px;
    }}

    /* HTML View */
    .html-container {{
      display: flex;
      height: 100%;
    }}

    .html-toc {{
      width: 240px;
      background: #f5f5f5;
      border-right: 1px solid #e0e0e0;
      overflow-y: auto;
      flex-shrink: 0;
      padding: 12px 0;
    }}

    .toc-title {{
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: #607d8b;
      padding: 8px 12px;
      font-weight: 600;
    }}

    .toc-item {{
      display: block;
      padding: 4px 12px;
      color: #37474f;
      text-decoration: none;
      font-size: 12px;
      line-height: 1.4;
      border-left: 2px solid transparent;
    }}

    .toc-item:hover {{
      background: #e8e8e8;
      border-left-color: #90a4ae;
    }}

    .toc-preface, .toc-preamble, .toc-body {{
      font-weight: 600;
      color: #263238;
    }}

    .toc-chapter {{
      font-weight: 600;
      color: #c41e3a;
      margin-top: 8px;
    }}

    .toc-section {{
      color: #37474f;
    }}

    .toc-article {{
      color: #607d8b;
      font-size: 11px;
    }}

    .html-view {{
      flex: 1;
      padding: 24px;
      overflow-y: auto;
      max-width: 800px;
    }}

    .html-view h2 {{
      font-size: 14px;
      color: #607d8b;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin: 24px 0 12px;
      padding-bottom: 6px;
      border-bottom: 1px solid #e0e0e0;
    }}

    .html-view h2:first-child {{ margin-top: 0; }}

    .doc-title {{
      font-size: 20px;
      font-weight: 600;
      line-height: 1.4;
      margin: 0 0 16px;
    }}

    .preface p, .preamble p {{
      margin: 8px 0;
    }}

    .chapter {{
      margin: 24px 0;
    }}

    .chapter-title {{
      font-size: 16px;
      font-weight: 600;
      color: #c41e3a;
      margin: 0 0 16px;
    }}

    .section {{
      margin: 16px 0;
    }}

    .section-title {{
      font-size: 14px;
      font-weight: 600;
      color: #263238;
      margin: 0 0 12px;
    }}

    .article {{
      margin: 12px 0;
      padding: 12px 16px;
      background: #fafafa;
      border-left: 3px solid #1565c0;
      border-radius: 0 4px 4px 0;
    }}

    .article-header {{
      margin-bottom: 8px;
    }}

    .art-num {{
      font-weight: 700;
      color: #1565c0;
    }}

    .art-heading {{
      font-weight: 600;
      margin-left: 8px;
    }}

    .paragraph {{
      display: flex;
      gap: 8px;
      margin: 6px 0;
    }}

    .para-num {{
      font-weight: 600;
      color: #607d8b;
      min-width: 24px;
    }}

    .para-content {{
      flex: 1;
    }}

    .para-content p {{
      margin: 0;
    }}

    .block-list {{
      margin: 8px 0 8px 20px;
    }}

    .list-item {{
      margin: 4px 0;
      display: flex;
      gap: 4px;
    }}

    .item-num {{
      font-weight: 500;
      color: #607d8b;
      flex-shrink: 0;
    }}

    .list-intro {{
      margin: 8px 0 4px;
    }}
  </style>
</head>
<body>
  <nav class="side-nav">
    {side_nav}
  </nav>

  <main class="main">
    <div class="tabs">
      <div class="tab active" data-view="raw">.raw</div>
      <div class="tab" data-view="meta">.meta</div>
      <div class="tab" data-view="html">.html</div>
      <div class="tab-info">{total_tags} elements</div>
    </div>

    <div class="view active" id="view-raw">
      <div class="tree">
{tree_html}
      </div>
    </div>

    <div class="view" id="view-meta">
      <div class="meta-view">
        {meta_html}
      </div>
    </div>

    <div class="view" id="view-html">
      <div class="html-container">
        <nav class="html-toc">
          <div class="toc-title">Contents</div>
          {toc_nav}
        </nav>
        <div class="html-view">
          {html_view}
        </div>
      </div>
    </div>
  </main>

  <script>
    // Tab switching
    document.querySelectorAll('.tab').forEach(tab => {{
      tab.addEventListener('click', () => {{
        document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
        tab.classList.add('active');
        document.getElementById('view-' + tab.dataset.view).classList.add('active');
      }});
    }});

    // FRBR Level filters
    document.querySelectorAll('.filter-item').forEach(filter => {{
      filter.addEventListener('click', () => {{
        filter.classList.toggle('active');
        const level = filter.dataset.filter;
        const isActive = filter.classList.contains('active');

        // Grey out elements in .raw view
        document.querySelectorAll(`[data-frbr-level="${{level}}"]`).forEach(el => {{
          if (isActive) {{
            el.classList.remove('greyed-out');
          }} else {{
            el.classList.add('greyed-out');
          }}
        }});

        // Grey out FRBR elements section
        document.querySelectorAll(`.frbr-level-elements[data-level="${{level}}"]`).forEach(el => {{
          if (isActive) {{
            el.classList.remove('greyed-out');
          }} else {{
            el.classList.add('greyed-out');
          }}
        }});

        // Grey out meta table rows
        const levelClass = level === 'work' ? 'work' : level === 'expression' ? 'expr' : 'manif';
        document.querySelectorAll('.meta-table .' + levelClass).forEach(el => {{
          if (isActive) {{
            el.classList.remove('greyed-out');
          }} else {{
            el.classList.add('greyed-out');
          }}
        }});
      }});
    }});

    // FRBR element highlighting and navigation
    document.querySelectorAll('.frbr-elem.clickable').forEach(elem => {{
      elem.addEventListener('click', () => {{
        const tag = elem.dataset.tag;
        const id = elem.dataset.id;
        const level = elem.dataset.level;

        // Clear previous highlights
        document.querySelectorAll('.highlighted').forEach(el => el.classList.remove('highlighted'));

        // Switch to raw view for FRBR/preface elements
        document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
        document.querySelector('[data-view="raw"]').classList.add('active');
        document.getElementById('view-raw').classList.add('active');

        // Find and highlight matching elements
        let selector = '';
        if (tag) {{
          selector = '[data-tag="' + tag + '"]';
          if (level) {{
            selector = '[data-frbr-level="' + level + '"] [data-tag="' + tag + '"]';
          }}
        }} else if (id) {{
          // For preface/preamble top-level
          selector = '[data-tag="' + id + '"]';
        }}

        if (selector) {{
          document.querySelectorAll(selector).forEach(el => {{
            el.classList.add('highlighted');
          }});

          const first = document.querySelector(selector);
          if (first) {{
            setTimeout(() => {{
              first.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
            }}, 100);
          }}
        }}
      }});
    }});

    // Structure item navigation (body structure)
    document.querySelectorAll('.struct-item').forEach(item => {{
      item.addEventListener('click', () => {{
        const eid = item.dataset.eid || item.dataset.id;
        if (!eid) return;

        // Clear previous highlights
        document.querySelectorAll('.highlighted').forEach(el => el.classList.remove('highlighted'));

        // Try HTML view first
        const htmlTarget = document.getElementById(eid);
        if (htmlTarget) {{
          htmlTarget.classList.add('highlighted');
          // Switch to HTML view
          document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
          document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
          document.querySelector('[data-view="html"]').classList.add('active');
          document.getElementById('view-html').classList.add('active');
          setTimeout(() => {{
            htmlTarget.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
          }}, 100);
        }} else {{
          // Try raw view - look for eId attribute
          document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
          document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
          document.querySelector('[data-view="raw"]').classList.add('active');
          document.getElementById('view-raw').classList.add('active');

          // Find element with matching eId in attributes
          const rawTarget = document.querySelector('[data-tag="' + eid.split('/')[0].split('_')[0] + '"]');
          if (rawTarget) {{
            rawTarget.classList.add('highlighted');
            setTimeout(() => {{
              rawTarget.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
            }}, 100);
          }}
        }}
      }});
    }});

    // Reference item highlighting
    document.querySelectorAll('.ref-item').forEach(item => {{
      item.addEventListener('click', () => {{
        // Clear previous highlights
        document.querySelectorAll('.highlighted').forEach(el => el.classList.remove('highlighted'));

        // Switch to raw view and highlight TLC elements
        document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
        document.querySelector('[data-view="raw"]').classList.add('active');
        document.getElementById('view-raw').classList.add('active');

        document.querySelectorAll('[data-tag^="TLC"]').forEach(el => {{
          el.classList.add('highlighted');
        }});
      }});
    }});
  </script>
</body>
</html>"""


def fetch_url(url: str) -> bytes:
    """Fetch XML content from URL."""
    import requests
    print(f"Fetching: {url}")
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    return resp.content


def main():
    parser = argparse.ArgumentParser(
        description="Generate HTML viewer from AKN XML files",
    )
    parser.add_argument("input", help="XML file path or URL")
    parser.add_argument("output", nargs="?", help="Output HTML file")
    parser.add_argument("--open", "-o", action="store_true", help="Open in browser")

    args = parser.parse_args()

    if args.input.startswith("http://") or args.input.startswith("https://"):
        xml_content = fetch_url(args.input)
        title = args.input.split("/")[-1] or "Fedlex AKN"
        default_output = "fedlex_annotated.html"
    else:
        input_path = Path(args.input)
        if not input_path.exists():
            print(f"Error: File not found: {input_path}", file=sys.stderr)
            sys.exit(1)
        xml_content = input_path.read_bytes()
        title = input_path.name
        default_output = input_path.stem + "_annotated.html"

    output_path = Path(args.output) if args.output else Path(default_output)
    html_content = generate_html(xml_content, title)
    output_path.write_text(html_content, encoding="utf-8")

    print(f"✅ HTML saved: {output_path}")

    if args.open:
        import webbrowser
        webbrowser.open(f"file://{output_path.absolute()}")


if __name__ == "__main__":
    main()
