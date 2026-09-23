# eCH-0296 Legal Texts (Erlasse und Gesetzestexte)

The context for modeling Swiss federal legal texts as LinkML, targeting the Fedlex Akoma Ntoso 3.0 profile. The LinkML schema is the source of truth from which a Fedlex-subset XSD and Schematron are generated (see `docs/adr/0001`).

## Language

**Akoma Ntoso (AKN)**:
The OASIS XML standard for legislative documents. We target version 3.0. Namespace `http://docs.oasis-open.org/legaldocml/ns/akn/3.0`.
_Avoid_: LegalDocML (the OASIS technical-committee name; use AKN for the vocabulary).

**Fedlex profile**:
The subset of AKN 3.0 actually used by the Swiss Federal publication platform Fedlex, further constrained by the `AKN-fedlex-*.sch` Schematron. eCH-0296 targets this profile, not full AKN.

**FRBR block**:
The `Work / Expression / Manifestation` three-level identification inside `akn:meta/akn:identification`. Work = the abstract law, Expression = a language version, Manifestation = a file format.

**eId**:
The `@eId` attribute — a hierarchical, path-style element identifier (e.g. `art_5/para_2`). Deterministic, not a random GUID. Required on every hierarchy element, article, paragraph, subdivision. **Not guaranteed unique**: real Fedlex files (SR-101) contain duplicate eIds, so the profile enforces presence but not uniqueness (`docs/adr/0006`).
_Avoid_: id, GUID, wId.

**ELI**:
European Legislation Identifier — the URI identity scheme for the FRBR block (e.g. `https://fedlex.data.admin.ch/eli/cc/1999/404/...`). AKN-native identity; distinct from the eCH commons `global_uri` CURIE.

**TLC reference**:
A "Top Level Class" reference in `akn:references` (`TLCOrganization`, `TLCRole`, `TLCReference`) defining a named entity that document elements point at by intra-document anchor (`@href='#ch.bk'`).

**Hierarchy element**:
Any of the nested structural containers of a law: `book, title, part, chapter, subchapter, section, subsection, level, article`. In OASIS AKN all share one recursive `hierarchy` type; the Fedlex profile constrains which may nest in which.

**Transparent level**:
`akn:level` — a hierarchy element whose *allowed children are those of its nearest non-level ancestor*. Cannot be expressed in XSD; enforced by Schematron (`FLX-HR-001-lv`).

**Inline content (mixed content)**:
Text interleaved in document order with inline markup elements inside `p, heading, num, item, listIntroduction, td`. Modeled faithfully as real classes (see `docs/adr/0002`), not an opaque string.

**InlineElement**:
The abstract base for a modeled inline markup element: `Ref, B, I, Sup, Span, AuthorialNote, Inline, Placeholder, Br` (+ `Mod, Ins, Del` for amendments). `AuthorialNote` recurses back into block content.

**TextRun**:
An `InlineElement` subclass carrying a plain run of text, so that a run of characters and a markup element can sit as ordered siblings in one `inline_content` list.

## References

- Marius Roth: [Aktuelle Anforderungen an amtliche Sammlungen](https://leges.weblaw.ch/legesissues/2013/1/2013133-62.html). LeGes 24 (2013) 1, pp. 33–62. Background on the systematic (consolidated) and chronological collections of federal and cantonal law and on what electronic publication and consolidation require of them.
