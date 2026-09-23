# eId uniqueness is deliberately NOT enforced in the generated XSD

**Context.** OASIS Akoma Ntoso declares an `xs:unique` on `@eId` (and `@GUID`) at the `act`/`bill` level, and Phase 2 of our converter initially did the same. But validating the real `SR-101-01012029-DE.xml` against the generated XSD revealed **four elements sharing the eId `disp_u2/lvl_M/list_u6/lbl_tab`** — the real Fedlex file is not eId-unique. The Fedlex Schematron (`AKN-fedlex-*.sch`) only ever checks eId **presence** (`not(@eId)`), never uniqueness.

**Decision.** The generated XSD does **not** emit an `xs:unique` on `@eId`. eId presence stays enforced (required attribute where the profile demands it); uniqueness is not, because enforcing it would reject valid Fedlex documents — directly violating the ADR-0001 acceptance test.

**Consequences.**
- Matches Fedlex reality and keeps the ADR-0001 north star (real SR-101 validates) intact.
- Diverges from OASIS AKN, which is stricter here. If a future consumer needs eId uniqueness, it must be an opt-in check outside the baseline profile.
- The converter's `xs:unique` support was removed; the coverage report no longer lists a `UNIQUE` feature.
