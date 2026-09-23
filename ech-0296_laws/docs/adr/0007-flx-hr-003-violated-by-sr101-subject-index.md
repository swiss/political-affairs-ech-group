# The generated Schematron reproduces all three residual Fedlex rules; SR-101 violates FLX-HR-003 in its own subject index

**Context.** ADR-0005 kept three Fedlex rules out of the XSD and in a Schematron: `FLX-HR-003` (content in a `level` implies a `//mod`), `FLX-XF-002b` (`fedlex:generator` implies `@value='xml'`), and `FLX-HR-001-lv` (transparent `level`). The converter now generates these from LinkML via the AKN profile (`profile/akn.py` `schematron_patterns`), rendered as **XPath 1.0** so lxml's ISO Schematron can execute them. The real Fedlex `.sch` is XSLT 2.0 (with `xsl:function`) and cannot run under lxml, so we transcribe the rules faithfully into XPath 1.0.

**Finding.** Running the generated Schematron against the real `SR-101-01012029-DE.xml`: `FLX-XF-002` and the transparent-level `FLX-HR-001-lv` **hold**, but `FLX-HR-003` fails **26 times** — once per `level` (A–Z) inside the alphabetical **subject index** (`proviso eId="disp_u2"`). Those levels carry `content` full of `<p>`/`<blockList>` and **no `<mod>`**. So the official, unmodified Fedlex reference file **violates Fedlex's own active Schematron rule** — the same result the real `.sch` would produce.

**Decision.** Keep `FLX-HR-003` in the generated Schematron unchanged (it is a real, useful rule for amending acts). Do **not** relax it to force SR-101 to pass. Instead, treat the 26 index-level hits as a documented, expected divergence — parallel to the eId-uniqueness finding in [[0006-eid-uniqueness-not-enforced]]. The north-star acceptance test asserts SR-101 satisfies the other two rules and that `FLX-HR-003`'s only failures are inside a `proviso` (the final-provisions register), never in the operative article body.

**Consequences.**
- Refines the ADR-0001 north star: SR-101 validates fully against the **XSD**; against the **Schematron** it satisfies every rule except `FLX-HR-003` in the subject index, which is a property of the reference file, not a converter defect.
- The tooling's ability to surface this ("Fedlex's file breaks Fedlex's rule") is a feature — it is exactly the kind of conformance gap the generated Schematron exists to catch.
- If a future profile wants a clean pass, `FLX-HR-003` would need scoping to exclude content-leaf index levels — an explicit deviation from the published Fedlex rule, deferred until a real consumer needs it.
