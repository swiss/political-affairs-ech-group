# Validation is split: XSD 1.0 carries ~90% of the Fedlex rules, a 3-rule Schematron carries the rest

**Context.** We analysed every rule in `AKN-fedlex-2026-07-01.sch`. The overwhelming majority are structural and fall out of a correct XSD content model (sequence/choice ordering, `use="required"` attributes, attribute enums, `xs:unique` for `eId` uniqueness) — expressible in **XSD 1.0**. Two rules are co-occurrence constraints needing **XSD 1.1 `xs:assert`** (`FLX-HR-003`: content in a `level` implies a `//mod`; `FLX-XF-002b`: `fedlex:generator` implies `@value='xml'`). Exactly one rule — `FLX-HR-001-lv`, the *transparent* `level` whose allowed children depend on the nearest non-`level` ancestor — is expressible in **neither XSD (1.0 or 1.1) nor LinkML**, because both are context-free / cannot see ancestors. Notably: there is **no** rule that LinkML can express but XSD cannot.

**Decision.** Keep the current `lxml` / **XSD 1.0** validator (no dependency change). The generated XSD carries all structural rules. A small **generated Schematron carries exactly three rules**: `FLX-HR-003`, `FLX-XF-002b`, and `FLX-HR-001-lv`. The real SR-101 must pass XSD + this Schematron.

**Considered options.**
- Upgrade to XSD 1.1 via the `xmlschema` library and emit `xs:assert`, shrinking Schematron to ≤1 rule — rejected for now to avoid the dependency/validator change.
- Model `level` non-transparently to reach zero Schematron — rejected: loses the exact contextual `level` check.

**Consequences.**
- The converter's biggest job is emitting **real content models** (sequence, `xs:choice`, required attributes, attribute enums, `xs:unique`) — that is where ~90% of Fedlex conformance comes from, not from Schematron.
- A minimal Schematron generator is still needed for the 3 residual rules; two validation artifacts are produced.
- If the `xs:assert` rules later feel worth folding into XSD, the migration path is a straight `lxml`→`xmlschema` swap (revisits this ADR).
