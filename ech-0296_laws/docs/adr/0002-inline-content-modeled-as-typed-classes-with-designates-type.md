# Inline/mixed content is modeled as typed classes discriminated by `designates_type`

**Context.** ADR-0001 requires the real SR-101 to validate against the generated XSD, so inline content (`akn:ref`, `b`, `i`, `sup`, `authorialNote`, …) must be modeled faithfully, not as an opaque string. LinkML has no native mixed-content (text interleaved with elements in document order).

**Decision.** Mixed elements (`p`, `heading`, `num`, `item`, `listIntroduction`, `td`) carry a single **ordered, multivalued, inlined `inline_content` slot** whose range is an **abstract `InlineElement`** base. Concrete subclasses cover the Fedlex inline subset: `TextRun` (a plain run of text), `Ref`, `B`, `I`, `Sup`, `Span`, `AuthorialNote`, `Inline`, `Placeholder`, `Br`, plus `Mod`/`Ins`/`Del` for amendments. `AuthorialNote` recurses into block content; `Ref` recurses into `inline_content`. Each member is discriminated by a **`designates_type` slot** (`element_type`), not by an `any_of: [string, class]` union.

**Considered options.**
- `any_of: [string, InlineElement]` (bare strings for text runs) — rejected: cleaner YAML, but `any_of` mixing a primitive with inlined polymorphic classes is fragile across `gen-json-schema` / `gen-owl` / `gen-doc` and forces a converter special-case.

**Consequences.**
- LinkML data is verbose (even a bare text run is an object with `element_type: TextRun`), but unambiguous, round-trippable, and safe across the standard LinkML generators.
- The converter maps each `InlineElement` subclass to a member of an `xs:choice` inside a `mixed="true"` complexType, and `TextRun` to the text node.
- Document order is carried by list order, so the converter must preserve it.
