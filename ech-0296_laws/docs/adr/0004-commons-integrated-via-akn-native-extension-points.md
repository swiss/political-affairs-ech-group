# eCH commons are integrated through AKN-native extension points, not as free slots

**Context.** The `ech-0296` schema does double duty: it must emit AKN XML that validates against the Fedlex profile (ADR-0001) *and* integrate with the eCH ecosystem (commons in `ech-0292_meta/input/schema_common.yaml`; cross-links to `ech-0294` actors, `ech-0295` affairs). AKN identity is ELI URIs + `eId` + intra-document `@href` anchors; the commons identity is `global_uri` (a CURIE). A commons slot that is not an AKN element would appear in the emitted XML and break validation.

**Decision.** Integrate the commons **selectively, bound to AKN's own extension points** — never as free non-AKN slots on AKN classes:
- Cross-links to actors/affairs use the commons `PersonReference` / `GroupReference` as slot ranges, serialized into AKN's native `FRBRauthor` / `TLCOrganization` `@href` as eCH CURIEs (e.g. `actor:department/CHE/bk`).
- The eCH `global_uri` for the act (and, if needed, articles) is carried inside AKN's `meta/proprietary` foreign-namespace extension, in the eCH namespace — optional in our XSD, so SR-101 (which omits it) still validates.
- Do **not** force `MultilingualValue` or the temporal mixins where AKN already covers the concept (`FRBRname` per language, `FRBRdate`).

**Consequences.**
- Nothing non-AKN leaks into the AKN body; SR-101 validates; our own examples with eCH extensions also validate.
- The converter must support serializing a `proprietary` foreign-namespace block and emitting `@href` CURIE references.
- Requires adding a `Proprietary` class and `PersonReference`/`GroupReference` (from commons) to the schema — the schema will import `schema_common` after all, but only these pieces are used.
