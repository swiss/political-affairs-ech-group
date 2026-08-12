"""
frbr_uri/fragment.py
tags: akn, fragment, subdivision

Swiss AKN Fragment Identifier Builder
======================================

Builds #fragment identifiers and full subdivision URIs for parts of legal
documents according to the AKN Naming Convention (OASIS, 2019) and the
ELI Subdivisions specification (EUR-Lex, v2).

Swiss legal hierarchy (German / French / Italian):
  Kapitel / Chapitre / Capitolo       → chp_{n}         (optional)
  Abschnitt / Section / Sezione       → sec_{n}         (optional)
  Artikel / Article / Articolo        → art_{n}
  Absatz / Alinéa / Capoverso        → para_{n}  or unp_{n} if unnumbered
  Ziffer / Chiffre / Cifra            → num_{n}         (numbered list item)
  Buchstabe / Lettre / Lettera        → lit_{a}         (lettered list item)

Short-title / abbreviation identifier:
  If a law has an official short title (OR, DSG, ZGB, etc.) that is used
  as the document-level pointer when no subdivision is specified.
  If not available, fallback order: SR number → AS number → BFS-scoped number.

Jurisdiction shorthand resolution:
  "ch"         → federal (default if omitted)
  "ZH"         → ch-zh  (ISO 3166-2 canton code, case-insensitive)
  "ZG"         → ch-zg
  "BE"         → ch-be  etc.
  "261"        → ch-zh-261  (BFS number → look up canton then compose)
  "1702"       → ch-zg-1702
  Full form:   "ch-zh-261" passthrough

Design decisions recorded here (referenced in standard doc):
  F1  Fragment syntax uses # per RFC 3986; AKN eId is the target
  F2  Subdivision codes follow AKN NC + ELI Subdivisions v2 table
  F3  Swiss Absatz uses `para` (numbered), `unp` if unnumbered (AKN4EU practice)
  F4  Ziffer uses `num` (not `pnt`) to match DE/FR citation tradition
  F5  Buchstabe uses `lit` – standard across all AKN profiles
  F6  Kapitel/Abschnitt are OPTIONAL structural wrappers; omitted if not present
  F7  eId is hierarchical and dot-separated: art_3.para_2.lit_a
  F8  Short title takes precedence as document pointer; SR if none
  F9  BFS number alone resolves via canton lookup table
  F10 Jurisdiction defaults to "ch" (federal) when omitted entirely
  F11 Compact display syntax: #a47 (article), #s3 (section/Abschnitt),
      #chp2 (chapter), #p2 (paragraph/Absatz), #lit-a (Buchstabe),
      #num-3 (Ziffer). Designed for UI display fields and short URLs.
      The compact form is DISPLAY-ONLY; canonical form is AKN eId.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Optional


# ── Subdivision codes ────────────────────────────────────────────────────────

# AKN element name → ELI/AKN subdivision code
# Sources: AKN NC §5.4, ELI Subdivisions v2 Table 13.2, LegalDocML.de
SUBDIVISION_CODES = {
    # Structural groupings (optional)
    "part":      "part",    # Teil
    "title":     "tit",     # Titel
    "chapter":   "chp",     # Kapitel / Chapitre
    "section":   "sec",     # Abschnitt / Section
    "subsection":"subsec",  # Unterabschnitt

    # Core provisions
    "article":   "art",     # Artikel / Article / Articolo
    "paragraph": "para",    # Absatz / Alinéa (numbered)
    "subparagraph": "unp",  # Absatz without number (unnumbered paragraph)
    "number":    "num",     # Ziffer / Chiffre  (F4: use `num` not `pnt`)
    "litera":    "lit",     # Buchstabe / Lettre
    "sublitera": "sublit",  # Doppelbuchstabe (double letter)
    "sentence":  "sen",     # Satz / Phrase / Frase       (F12)
    "indent":    "ind",     # Spiegelstrich (bullet/dash list item)
    "point":     "pnt",     # Point (EU terminology, maps to AKN <point>)

    # Special
    "annex":     "anx",     # Anhang / Annexe
    "schedule":  "sch",     # Beilage
}

# German legal term → subdivision key (for display label generation)
DE_TERMS = {
    "Kapitel":        "chapter",
    "Abschnitt":      "section",
    "Unterabschnitt": "subsection",
    "Teil":           "part",
    "Titel":          "title",
    "Artikel":        "article",
    "Art.":           "article",
    "§":              "article",   # Paragraph (German-law style)
    "Absatz":         "paragraph",
    "Abs.":           "paragraph",
    "Ziffer":         "number",
    "Ziff.":          "number",
    "Buchstabe":      "litera",
    "lit.":           "litera",
    "Buchst.":        "litera",
    "Doppelbuchstabe":"sublitera",
    "Spiegelstrich":  "indent",
    "Anhang":         "annex",
    "Satz":           "sentence",
    "S.":             "sentence",
}


FR_TERMS = {
    "Chapitre":   "chapter",
    "Section":    "section",
    "Article":    "article",
    "Art.":       "article",
    "Alinéa":     "paragraph",
    "Al.":        "paragraph",
    "Chiffre":    "number",
    "ch.":        "number",
    "Lettre":     "litera",
    "let.":       "litera",
    "Annexe":     "annex",
}

IT_TERMS = {
    "Capitolo":   "chapter",
    "Sezione":    "section",
    "Articolo":   "article",
    "Art.":       "article",
    "Capoverso":  "paragraph",
    "cpv.":       "paragraph",
    "Cifra":      "number",
    "Lettera":    "litera",
    "lett.":      "litera",
    "Allegato":   "annex",
}


# ── Canton code → jurisdiction prefix ────────────────────────────────────────

# ISO 3166-2:CH codes (uppercase) → AKN jurisdiction prefix
CANTON_CODES: dict[str, str] = {
    "AG": "ch-ag", "AI": "ch-ai", "AR": "ch-ar", "BE": "ch-be",
    "BL": "ch-bl", "BS": "ch-bs", "FR": "ch-fr", "GE": "ch-ge",
    "GL": "ch-gl", "GR": "ch-gr", "JU": "ch-ju", "LU": "ch-lu",
    "NE": "ch-ne", "NW": "ch-nw", "OW": "ch-ow", "SG": "ch-sg",
    "SH": "ch-sh", "SO": "ch-so", "SZ": "ch-sz", "TG": "ch-tg",
    "TI": "ch-ti", "UR": "ch-ur", "VD": "ch-vd", "VS": "ch-vs",
    "ZG": "ch-zg", "ZH": "ch-zh",
}

# BFS number prefix → canton code (first 1-2 digits of BFS number)
# Rough mapping; actual BFS numbers follow canton-specific ranges
BFS_CANTON_PREFIX: dict[str, str] = {
    "1":    "ZH",    # 0001-0999: ZH
    "2":    "BE",    # 0301-0999: BE
    "3":    "LU",
    "4":    "UR",
    "5":    "SZ",
    "6":    "OW",
    "7":    "NW",
    "8":    "GL",
    "9":    "ZG",
    "10":   "FR",
    "11":   "SO",
    "12":   "BS",
    "13":   "BL",
    "14":   "SH",
    "15":   "AR",
    "16":   "AI",
    "17":   "SG",
    "18":   "GR",
    "19":   "AG",
    "20":   "TG",
    "21":   "TI",
    "22":   "VD",
    "23":   "VS",
    "24":   "NE",
    "25":   "GE",
    "26":   "JU",
}

# Well-known BFS numbers → jurisdiction (for municipalities we know)
KNOWN_BFS: dict[str, str] = {
    "261":  "ch-zh-261",   # Stadt Zürich
    "351":  "ch-be-351",   # Stadt Bern
    "5586": "ch-vd-5586",  # Ville de Lausanne
    "1702": "ch-zg-1702",  # Gemeinde Cham
}


def resolve_jurisdiction(raw: str) -> str:
    """
    Resolve a shorthand jurisdiction reference to a canonical AKN jurisdiction id.

    Accepts:
      ""         → "ch"  (federal default, F10)
      "ch"       → "ch"
      "ZH"       → "ch-zh"
      "zh"       → "ch-zh"  (case-insensitive)
      "261"      → "ch-zh-261"
      "1702"     → "ch-zg-1702"
      "ch-zh"    → "ch-zh"  (passthrough)
      "ch-zh-261"→ "ch-zh-261"
    """
    if not raw or raw.strip() == "":
        return "ch"

    s = raw.strip()

    # Already canonical (contains hyphen)
    if "-" in s:
        return s.lower()

    # Pure BFS number (digits only)
    if s.isdigit():
        if s in KNOWN_BFS:
            return KNOWN_BFS[s]
        # Try range-based canton lookup
        canton = _bfs_to_canton(int(s))
        if canton:
            canton_jid = CANTON_CODES[canton]
            return f"{canton_jid}-{s}"
        raise ValueError(f"Cannot resolve BFS number '{s}' to a jurisdiction")

    # Canton code (2 uppercase letters)
    upper = s.upper()
    if upper in CANTON_CODES:
        return CANTON_CODES[upper]

    # "ch" as-is
    if s.lower() == "ch":
        return "ch"

    raise ValueError(
        f"Cannot resolve jurisdiction shorthand '{raw}'. "
        f"Use 'ch', a canton code (ZH, ZG, BE…), a BFS number (261, 1702…), "
        f"or a full id (ch-zh-261)."
    )


# ── Fragment / eId building ───────────────────────────────────────────────────

@dataclass
class SubdivisionRef:
    """
    A single level in a subdivision reference, e.g. art=47, para=2, lit="a".
    """
    kind: str          # key from SUBDIVISION_CODES, e.g. "article", "paragraph"
    value: str         # number or letter, e.g. "47", "2", "a"

    @property
    def code(self) -> str:
        """AKN/ELI subdivision code, e.g. 'art', 'para', 'lit'."""
        return SUBDIVISION_CODES[self.kind]

    @property
    def segment(self) -> str:
        """Single eId segment, e.g. 'art_47', 'para_2', 'lit_a'."""
        return f"{self.code}_{self.value}"


@dataclass
class FragmentRef:
    """
    A complete fragment reference for a point in a legal document.

    Levels are ordered from outermost to innermost:
      [chp_2, sec_1, art_47, para_3, lit_a]

    Structural levels (chapter, section) are optional (F6).
    """
    subdivisions: list[SubdivisionRef] = field(default_factory=list)

    def eid(self) -> str:
        """
        Return the hierarchical eId string per AKN NC §5.4.
        Dot-separated from outermost to innermost: art_47.para_3.lit_a
        """
        return ".".join(s.segment for s in self.subdivisions)

    def fragment(self) -> str:
        """Return the #fragment string for use in URIs: #art_47.para_3.lit_a"""
        return f"#{self.eid()}"

    def eli_path(self) -> str:
        """
        Return the ELI-style path suffix (slash-separated) for use in
        subdivision URIs: /art_47/para_3/lit_a
        (ELI Subdivisions v2 §5.1)
        """
        return "/" + "/".join(s.segment for s in self.subdivisions)

    def human_readable(self, lang: str = "de") -> str:
        """
        Return a human-readable citation string in the given language.
        e.g. de → "Art. 47 Abs. 3 lit. a"
             fr → "Art. 47 al. 3 let. a"
        """
        labels = _HUMAN_LABELS.get(lang, _HUMAN_LABELS["de"])
        parts = []
        for s in self.subdivisions:
            label = labels.get(s.kind, s.code)
            parts.append(f"{label} {s.value}")
        return " ".join(parts)

    def is_empty(self) -> bool:
        return len(self.subdivisions) == 0


_HUMAN_LABELS: dict[str, dict[str, str]] = {
    "de": {
        "part": "Teil", "title": "Titel", "chapter": "Kap.",
        "section": "Abschn.", "subsection": "Unterabschn.",
        "article": "Art.", "paragraph": "Abs.", "subparagraph": "Abs.",
        "number": "Ziff.", "litera": "lit.", "sublitera": "sublit.",
        "indent": "Spiegelstr.", "annex": "Anhang", "sentence": "Satz",
    },
    "fr": {
        "part": "Partie", "title": "Titre", "chapter": "Chap.",
        "section": "Section", "subsection": "Sous-section",
        "article": "Art.", "paragraph": "Al.", "subparagraph": "Al.",
        "number": "ch.", "litera": "let.", "sublitera": "sublet.",
        "indent": "tiret", "annex": "Annexe", "sentence": "phr.",
    },
    "it": {
        "part": "Parte", "title": "Titolo", "chapter": "Cap.",
        "section": "Sezione", "subsection": "Sottosezione",
        "article": "Art.", "paragraph": "cpv.", "subparagraph": "cpv.",
        "number": "n.", "litera": "lett.", "sublitera": "sublitt.",
        "indent": "trattino", "annex": "Allegato", "sentence": "frase",
    },
}


# ── Document-level pointer (short title / SR number / AS number) ─────────────

@dataclass
class DocumentPointer:
    """
    Points to a whole document using the most human-meaningful identifier
    available, in priority order (F8):
      1. Official short title / abbreviation (OR, DSG, ZGB, SR 101)
      2. SR / LS / RS citation number
      3. AS / OS publication sequence number (year-based)
      4. Composed from jurisdiction + BFS + year + sequential
    """
    short_title: Optional[str] = None    # e.g. "OR", "DSG", "ZGB"
    sr_number: Optional[str] = None      # e.g. "220", "235.1", "170.41"
    as_number: Optional[str] = None      # e.g. "2022/491"
    jurisdiction: str = "ch"
    year: Optional[str] = None
    seq: Optional[str] = None

    def preferred_id(self) -> str:
        """Return the most meaningful identifier for the document."""
        if self.short_title:
            return self.short_title
        if self.sr_number:
            return f"SR {self.sr_number}"
        if self.as_number:
            jid = self.jurisdiction.upper().replace("-", "/")
            return f"AS {jid}/{self.as_number}"
        if self.year and self.seq:
            return f"{self.jurisdiction}/{self.year}/{self.seq}"
        return self.jurisdiction

    def akn_pointer(self) -> str:
        """
        Return a compact AKN-style document pointer.
        Short titles become the pointer directly (lowercase).
        SR numbers use sr-{number} with dots as hyphens.
        """
        if self.short_title:
            return self.short_title.lower()
        if self.sr_number:
            return "sr-" + self.sr_number.replace(".", "-")
        if self.as_number:
            return "as-" + self.as_number.replace("/", "-")
        return self.preferred_id().lower().replace(" ", "-")


# ── Fragment parser ───────────────────────────────────────────────────────────

def parse_fragment(raw: str) -> FragmentRef:
    """
    Parse a human-readable citation string or AKN eId into a FragmentRef.

    Accepts:
      "Art. 47 Abs. 2 lit. a"   → [art_47, para_2, lit_a]
      "art_47.para_2.lit_a"     → [art_47, para_2, lit_a]
      "#art_47.para_2.lit_a"    → [art_47, para_2, lit_a]
      "Art. 47"                 → [art_47]
      "Kap. 2 Abschn. 3 Art. 5"→ [chp_2, sec_3, art_5]
    """
    s = raw.strip().lstrip("#")

    # AKN eId format (contains _ and/or .)
    if re.match(r"^[a-z]+_[\w.]+$", s):
        return _parse_eid(s)

    # Human-readable format
    return _parse_human(s)


def _parse_eid(eid: str) -> FragmentRef:
    """Parse a dot-separated eId like art_47.para_2.lit_a"""
    # Reverse lookup from code to kind
    code_to_kind = {v: k for k, v in SUBDIVISION_CODES.items()}
    refs = []
    for segment in eid.split("."):
        m = re.match(r"^([a-z]+)_(.+)$", segment)
        if not m:
            raise ValueError(f"Invalid eId segment: '{segment}'")
        code, value = m.groups()
        if code not in code_to_kind:
            raise ValueError(f"Unknown subdivision code '{code}' in eId '{eid}'")
        refs.append(SubdivisionRef(kind=code_to_kind[code], value=value))
    return FragmentRef(subdivisions=refs)


def _parse_human(text: str) -> FragmentRef:
    """
    Parse a human citation like 'Art. 47 Abs. 2 lit. a'
    Tries German terms, then French, then Italian.
    """
    # Build combined term→kind map, longest first to avoid prefix shadowing
    all_terms: dict[str, str] = {}
    for d in (DE_TERMS, FR_TERMS, IT_TERMS):
        all_terms.update(d)

    tokens = text.split()
    refs: list[SubdivisionRef] = []
    i = 0
    while i < len(tokens):
        # Try 2-token match first (e.g. "Abs." alone won't consume "2")
        matched = False
        for term_len in (2, 1):
            if i + term_len > len(tokens):
                continue
            term = " ".join(tokens[i:i + term_len])
            if term in all_terms:
                kind = all_terms[term]
                # Next token should be the number/letter
                val_idx = i + term_len
                if val_idx < len(tokens):
                    value = tokens[val_idx].rstrip(",;.")
                    refs.append(SubdivisionRef(kind=kind, value=value))
                    i = val_idx + 1
                    matched = True
                    break
        if not matched:
            i += 1  # skip unrecognized token

    return FragmentRef(subdivisions=refs)


# ── Convenience builder ───────────────────────────────────────────────────────

def build_fragment(
    *,
    chapter: Optional[str] = None,
    section: Optional[str] = None,
    subsection: Optional[str] = None,
    article: Optional[str] = None,
    paragraph: Optional[str] = None,
    number: Optional[str] = None,
    litera: Optional[str] = None,
    sublitera: Optional[str] = None,
    sentence: Optional[str] = None,
    indent: Optional[str] = None,
    annex: Optional[str] = None,
) -> FragmentRef:
    """
    Build a FragmentRef from keyword arguments — the primary API for the frontend.

    Structural levels (chapter, section) are optional (F6).
    At least one of article, annex should be provided for a meaningful reference.

    Example:
        build_fragment(article="47", paragraph="2", litera="a")
        → FragmentRef([art_47, para_2, lit_a])
    """
    levels = [
        ("part",       None),   # not exposed as kwarg here; use parse_fragment
        ("chapter",    chapter),
        ("section",    section),
        ("subsection", subsection),
        ("annex",      annex),
        ("article",    article),
        ("paragraph",  paragraph),
        ("number",     number),
        ("litera",     litera),
        ("sublitera",  sublitera),
        ("sentence",   sentence),
        ("indent",     indent),
    ]
    refs = [SubdivisionRef(kind=k, value=v) for k, v in levels if v is not None]
    return FragmentRef(subdivisions=refs)


# ── Compact display syntax (F11) ──────────────────────────────────────────────
#
# Compact prefixes for UI display fields and short URLs.
# These are DISPLAY-ONLY – never stored as canonical identifiers.
#
# Mapping: compact prefix → subdivision kind
_COMPACT_PREFIX_TO_KIND: dict[str, str] = {
    "chp":  "chapter",       # #chp-2   → Kapitel 2
    "s":    "section",       # #s3      → Abschnitt 3   (glued: single-char)
    "sub":  "subsection",    # #sub-1   → Unterabschnitt 1
    "a":    "article",       # #a47     → Art. 47        (glued: single-char)
    "p":    "paragraph",     # #p2      → Abs. 2         (glued: single-char)
    "num":  "number",        # #num-3   → Ziff. 3
    "lit":  "litera",        # #lit-a   → lit. a
    "slit": "sublitera",     # #slit-aa → Doppelbuchstabe aa
    "anx":  "annex",         # #anx-2   → Anhang 2
    "sen":  "sentence",      # #sen-2   → Satz 2  (F12)
}

# Reverse: kind → compact prefix (for display generation)
_KIND_TO_COMPACT: dict[str, str] = {v: k for k, v in _COMPACT_PREFIX_TO_KIND.items()}

# Compact form uses "-" separator between prefix and value when value starts
# with a letter (to avoid ambiguity): #lit-a, #num-3, but #a47, #p2, #s3
_LETTER_VALUE_KINDS = {"litera", "sublitera"}


def compact_fragment(fragment: FragmentRef) -> str:
    """
    Convert a FragmentRef to compact display syntax (F11).

    Examples:
        [art_47]                    → "#a47"
        [art_47, para_2]            → "#a47-p2"
        [art_47, para_2, lit_a]     → "#a47-p2-lit-a"
        [chp_3, sec_2, art_5]       → "#chp3-s2-a5"
        [art_11, num_3, lit_b]      → "#a11-num-3-lit-b"

    Segments are joined with "-". Values that are letters use an extra "-"
    separator after the prefix for readability (#lit-a not #lita).
    """
    if fragment.is_empty():
        return ""
    parts = []
    for sub in fragment.subdivisions:
        prefix = _KIND_TO_COMPACT.get(sub.kind, sub.code)
        if sub.kind in _LETTER_VALUE_KINDS:
            # #lit-a, #slit-aa  — always hyphenated
            parts.append(f"{prefix}-{sub.value}")
        elif len(prefix) == 1:
            # Single-letter prefix: glue directly  #a47, #p2, #s3
            parts.append(f"{prefix}{sub.value}")
        else:
            # Multi-char prefix: always hyphenate  #chp2, #num-3, #anx-1
            parts.append(f"{prefix}-{sub.value}")
    return "#" + "-".join(parts)


def parse_compact_fragment(compact: str) -> FragmentRef:
    """
    Parse a compact display fragment back to a FragmentRef (F11).

    Examples:
        "#a47"               → [art_47]
        "#a47-p2-lit-a"      → [art_47, para_2, lit_a]
        "#chp3-s2-a5"        → [chp_3, sec_2, art_5]
        "#a11-num-3-lit-b"   → [art_11, num_3, lit_b]
        "a47"                → [art_47]   (# optional)

    Parsing strategy:
      Scan tokens left to right. When a token matches a known prefix,
      consume it and the next numeric/alpha value.
    """
    s = compact.strip().lstrip("#")
    if not s:
        return FragmentRef()

    # Sort prefixes longest-first to avoid "s" matching before "sub", "slit"
    sorted_prefixes = sorted(_COMPACT_PREFIX_TO_KIND.keys(), key=len, reverse=True)

    refs: list[SubdivisionRef] = []
    # Split on "-" but re-join prefix+value pairs
    # Strategy: scan character by character matching prefixes
    tokens = s.split("-")
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        matched = False
        for prefix in sorted_prefixes:
            if tok.lower() == prefix:
                # Next token is the value (e.g. "a" after "lit")
                if i + 1 < len(tokens):
                    value = tokens[i + 1]
                    refs.append(SubdivisionRef(
                        kind=_COMPACT_PREFIX_TO_KIND[prefix],
                        value=value
                    ))
                    i += 2
                    matched = True
                    break
            elif tok.lower().startswith(prefix):
                # Value is glued: "a47" → prefix="a", value="47"
                value = tok[len(prefix):]
                if value:
                    refs.append(SubdivisionRef(
                        kind=_COMPACT_PREFIX_TO_KIND[prefix],
                        value=value
                    ))
                    i += 1
                    matched = True
                    break
        if not matched:
            i += 1  # skip unrecognised token

    return FragmentRef(subdivisions=refs)


# ── Enhanced BFS canton range lookup ─────────────────────────────────────────
#
# Full BFS number range → canton code
# Source: BFS Amtliches Gemeindeverzeichnis ranges (approximate)
# Used when KNOWN_BFS dict does not have an exact match.

_BFS_RANGES: list[tuple[int, int, str]] = [
    (1,    230,  "ZH"),
    (231,  400,  "BE"),
    (401,  600,  "LU"),
    (601,  700,  "UR"),
    (701,  900,  "SZ"),
    (901,  1000, "OW"),
    (1001, 1100, "NW"),
    (1101, 1200, "GL"),
    (1201, 1400, "ZG"),
    (1401, 1700, "FR"),
    (1701, 1900, "SO"),
    (1901, 2100, "BS"),
    (2101, 2400, "BL"),
    (2401, 2500, "SH"),
    (2401, 2600, "AR"),
    (2601, 2700, "AI"),
    (2701, 3400, "SG"),
    (3401, 4000, "GR"),
    (4001, 4500, "AG"),
    (4501, 4900, "TG"),
    (5001, 5400, "TI"),
    (5401, 6000, "VD"),
    (6001, 6500, "VS"),
    (6401, 6700, "NE"),
    (6601, 6900, "GE"),
    (6701, 7000, "JU"),
]


def _bfs_to_canton(bfs: int) -> Optional[str]:
    """Look up canton code from BFS number using range table."""
    # Exact lookup first
    str_bfs = str(bfs)
    if str_bfs in KNOWN_BFS:
        # already resolved
        return KNOWN_BFS[str_bfs].split("-")[1].upper()  # e.g. "zh"→"ZH"
    for lo, hi, canton in _BFS_RANGES:
        if lo <= bfs <= hi:
            return canton
    return None
