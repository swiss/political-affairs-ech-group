"""
frbr_uri/ranges.py
tags: akn, range, selection, fragment

AKN Range and Multi-Selection Syntax
=====================================

Extends the compact fragment system (fragment.py) with support for:

1. CONTIGUOUS RANGES (portion references, AKN §4.8.4)
   A span of provisions within the same document:
     a7-a18          → Articles 7 to 18
     a7_p2-a8_p2     → Art. 7 Abs. 2 through Art. 8 Abs. 2
     a7_lit-a-a28_s1 → Art. 7 lit. a through Art. 28 Satz 1

   Compact syntax:  {start}~{end}  using TILDE as range separator
   AKN URI:  expression~art_7->art_18      (portion reference)

2. DISCRETE MULTI-SELECTIONS (non-contiguous)
   Multiple disjoint provisions (e.g. for cross-reference sets):
     a7,a11,a28      → Articles 7, 11, and 28
     a7_p2,a11_lit-a → Art. 7 Abs. 2 and Art. 11 lit. a

   Compact syntax: {ref1},{ref2},{ref3}  COMMA separated
   Not a standard AKN construct — represented as a list of independent refs.

3. DOCUMENT-LEVEL SLASH ROUTING (F13)
   When a reference points to a single subdivision as a REST resource:
     /akn/ch/lei/.../art_47           (ELI subdivision path, F13-slash)
   When it's an in-document anchor:
     /akn/ch/lei/...#art_47           (fragment hash, F1)
   Both are valid; use depends on whether the subdivision is being
   fetched as an independent resource or located within a full document.

Design decisions:
  F12  Sentence level uses `sen` compact prefix → AKN `sen_{n}` eId
  F13  Slash routing for single-resource subdivision GET; hash for navigation
  F14  Range separator is `~` in compact syntax (mirrors AKN `~` portion syntax)
  F15  Multi-selection separator is `,` (comma)
  F16  Range in compact form: `#a7~a18` or `#a7_p2~a8_p2`
  F17  Within a range, each endpoint uses `_` as internal separator (not `-`)
       to avoid ambiguity with the inter-segment `-` in compact form.
       Example: a7_p2_lit-a~a28_sen-1  not  a7-p2-lit-a~a28-sen-1
  F18  The `_` vs `-` rule:
         `_`  separates LEVELS within one endpoint:  a7_p2_lit-a
         `-`  separates PREFIX from VALUE:           lit-a, sen-2, num-3
         `~`  separates START from END in a range
         `,`  separates discrete selections
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Optional, Union

from .fragment import (
    FragmentRef, compact_fragment, parse_compact_fragment,
    build_fragment,
)


# ── Range reference ───────────────────────────────────────────────────────────

@dataclass
class RangeRef:
    """
    A contiguous range between two fragment positions in the same document.

    Corresponds to AKN portion reference syntax:
      expression~{start_eId}->{end_eId}

    Compact display:  #a7~a18   #a7_p2~a8_p2   #a7_lit-a~a28_sen-1
    """
    start: FragmentRef
    end: FragmentRef

    def akn_portion(self) -> str:
        """AKN portion range:  art_7->art_18"""
        return f"{self.start.eid()}->{self.end.eid()}"

    def compact(self) -> str:
        """Compact display: #a7~a18  (tilde = range separator, F14)"""
        s = _compact_endpoint(self.start)
        e = _compact_endpoint(self.end)
        return f"#{s}~{e}"

    def human_readable(self, lang: str = "de") -> str:
        return (
            f"{self.start.human_readable(lang)} – "
            f"{self.end.human_readable(lang)}"
        )

    def to_eli_path_range(self) -> str:
        """ELI subdivision path range: /art_7/para_2~art_8/para_2"""
        return f"{self.start.eli_path()}~{self.end.eli_path()}"


@dataclass
class MultiSelectionRef:
    """
    A set of non-contiguous fragment references (discrete selection).

    Compact display:  #a7,a11,a28   #a7_p2,a11_lit-a
    """
    refs: list[FragmentRef]

    def compact(self) -> str:
        """#a7,a11,a28"""
        parts = [_compact_endpoint(r) for r in self.refs]
        return "#" + ",".join(parts)

    def human_readable(self, lang: str = "de") -> str:
        return "; ".join(r.human_readable(lang) for r in self.refs)

    def eids(self) -> list[str]:
        return [r.eid() for r in self.refs]


# A selection can be a single ref, a range, or a multi-selection
Selection = Union[FragmentRef, RangeRef, MultiSelectionRef]


# ── Internal: compact endpoint uses `_` as level separator ───────────────────

def _compact_endpoint(frag: FragmentRef) -> str:
    """
    Compact form for use INSIDE a range/multi-selection (F17).

    Uses `_` as level separator instead of `-` to avoid ambiguity.
    So:  art_47, para_2, lit_a  →  a47_p2_lit-a
                                    ^^^   (underscores between levels)
                                         ^^^^^ (hyphen only within prefix-value)

    Standalone compact uses `-` between levels (#a47-p2-lit-a).
    Endpoint compact uses `_` between levels (a47_p2_lit-a).
    """
    if frag.is_empty():
        return ""
    parts = []
    for sub in frag.subdivisions:
        from .fragment import _KIND_TO_COMPACT, _LETTER_VALUE_KINDS
        prefix = _KIND_TO_COMPACT.get(sub.kind, sub.code)
        if sub.kind in _LETTER_VALUE_KINDS:
            parts.append(f"{prefix}-{sub.value}")
        elif len(prefix) == 1:
            parts.append(f"{prefix}{sub.value}")
        else:
            parts.append(f"{prefix}-{sub.value}")
    return "_".join(parts)


def _parse_endpoint(s: str) -> FragmentRef:
    """
    Parse a range endpoint using `_` as level separator.
    e.g. 'a47_p2_lit-a' → FragmentRef([art_47, para_2, lit_a])
    """
    # Replace `_` level separators with `-` to reuse parse_compact_fragment
    # But we must NOT replace `_` inside prefix-value pairs (there are none —
    # prefixes never contain underscores, values never contain underscores).
    # So a simple replace is safe here.
    normalised = s.replace("_", "-")
    return parse_compact_fragment(normalised)


# ── Parsing ───────────────────────────────────────────────────────────────────

def parse_selection(raw: str) -> Selection:
    """
    Parse any selection string into a FragmentRef, RangeRef, or MultiSelectionRef.

    Formats:
      Single:    "#a47-p2-lit-a"   or  "a47-p2-lit-a"
      Range:     "#a7~a18"         or  "#a7_p2~a8_p2"
      Multi:     "#a7,a11,a28"     or  "#a7_p2,a11_lit-a"
      Human:     "Art. 47 Abs. 2"
      AKN eId:   "art_47.para_2"
    """
    s = raw.strip().lstrip("#")

    # Multi-selection (comma)
    if "," in s and "~" not in s:
        parts = [p.strip() for p in s.split(",")]
        refs = [_parse_endpoint(p) for p in parts if p]
        return MultiSelectionRef(refs=refs)

    # Range (tilde)
    if "~" in s:
        halves = s.split("~", 1)
        start = _parse_endpoint(halves[0].strip())
        end   = _parse_endpoint(halves[1].strip())
        return RangeRef(start=start, end=end)

    # AKN eId (contains `.` and `_`, no spaces)
    if re.match(r"^[a-z]+_[\w.]+$", s):
        from .fragment import _parse_eid
        return _parse_eid(s)

    # Human text (contains spaces)
    if " " in s:
        from .fragment import _parse_human
        return _parse_human(s)

    # Compact single
    return parse_compact_fragment(s)


def compact_selection(sel: Selection) -> str:
    """Convert any Selection back to compact display string."""
    if isinstance(sel, FragmentRef):
        return compact_fragment(sel)
    if isinstance(sel, RangeRef):
        return sel.compact()
    if isinstance(sel, MultiSelectionRef):
        return sel.compact()
    raise TypeError(f"Unknown selection type: {type(sel)}")


def human_selection(sel: Selection, lang: str = "de") -> str:
    """Human-readable string for any selection."""
    if isinstance(sel, FragmentRef):
        return sel.human_readable(lang)
    if isinstance(sel, RangeRef):
        return sel.human_readable(lang)
    if isinstance(sel, MultiSelectionRef):
        return sel.human_readable(lang)
    raise TypeError(f"Unknown selection type: {type(sel)}")


# ── AKN URI helpers ───────────────────────────────────────────────────────────

def selection_to_uri(
    base_expression_uri: str,
    sel: Selection,
    mode: str = "hash",  # "hash" | "slash" | "portion"
) -> str:
    """
    Append a selection to a base AKN expression URI.

    mode="hash"    → base#art_47.para_2        (in-document anchor, F1)
    mode="slash"   → base/art_47/para_2        (REST resource path, F13)
    mode="portion" → base~art_7->art_18        (AKN portion, RangeRef only)

    For MultiSelectionRef, returns a comma-separated list of hash URIs
    (no single standard URI exists for disjoint selections).
    """
    if isinstance(sel, FragmentRef):
        if sel.is_empty():
            return base_expression_uri
        if mode == "slash":
            return base_expression_uri.rstrip("/") + sel.eli_path()
        else:
            return base_expression_uri + sel.fragment()

    if isinstance(sel, RangeRef):
        if mode == "portion":
            return f"{base_expression_uri}~{sel.akn_portion()}"
        elif mode == "slash":
            return f"{base_expression_uri}~{sel.start.eli_path()}~{sel.end.eli_path()}"
        else:
            # Hash: link to start, indicate range in fragment
            return f"{base_expression_uri}~{sel.akn_portion()}"

    if isinstance(sel, MultiSelectionRef):
        # No single URI — return list
        uris = [
            selection_to_uri(base_expression_uri, r, mode)
            for r in sel.refs
        ]
        return ",".join(uris)

    raise TypeError(f"Unknown selection type: {type(sel)}")


# ── Svelte-friendly state ─────────────────────────────────────────────────────

@dataclass
class SelectionState:
    """
    The complete state for a ProseMirror selection → URI mapping.
    This is what gets passed to/from the Svelte store and the API.
    """
    raw_input: str                    # What the user typed / PM selected
    selection: Optional[Selection] = None
    base_expression_uri: str = ""
    document_pointer: str = ""        # "BV", "SR 101", etc.

    # Derived (computed from selection + base)
    hash_uri: str = ""
    slash_uri: str = ""
    compact_display: str = ""
    human_de: str = ""
    human_fr: str = ""

    errors: list[str] = field(default_factory=list)

    @classmethod
    def from_raw(
        cls,
        raw: str,
        base_expression_uri: str = "",
        document_pointer: str = "",
    ) -> "SelectionState":
        state = cls(
            raw_input=raw,
            base_expression_uri=base_expression_uri,
            document_pointer=document_pointer,
        )
        try:
            sel = parse_selection(raw)
            state.selection = sel
            state.compact_display = compact_selection(sel)
            state.human_de = human_selection(sel, "de")
            state.human_fr = human_selection(sel, "fr")
            if base_expression_uri:
                state.hash_uri = selection_to_uri(base_expression_uri, sel, "hash")
                state.slash_uri = selection_to_uri(base_expression_uri, sel, "slash")
        except Exception as e:
            state.errors.append(str(e))
        return state

    def to_dict(self) -> dict:
        return {
            "raw_input": self.raw_input,
            "compact_display": self.compact_display,
            "human_de": self.human_de,
            "human_fr": self.human_fr,
            "hash_uri": self.hash_uri,
            "slash_uri": self.slash_uri,
            "document_pointer": self.document_pointer,
            "errors": self.errors,
        }
