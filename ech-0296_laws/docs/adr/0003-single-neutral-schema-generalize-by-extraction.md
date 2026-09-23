# One publisher-neutral schema now; generalize into core + profiles by extraction later

**Context.** eCH-0296 is meant as a reusable Swiss legal-text standard (cantons and other publishers should be able to use it), which argues for a general AKN core + a Fedlex profile as separate schemas. But the `linkml-to-xsd` converter currently ignores `imports` entirely, and only Fedlex (SR-101) is a concrete target today.

**Decision.** Ship **one** publisher-neutral `schema.yaml`. Name classes/slots neutrally (`LegalText`/`Act`, not `FedlexDocument`), express the general AKN structure as the core, and apply Fedlex-specific constraints (required `eId`, `fedlex:*` attributes, `ELI_URI`, `FLX-*` Schematron bindings) via mixins + `slot_usage` as a clearly-marked profile layer inside the same file. Split into a separate `legal_text_core.yaml` + per-publisher profile files only when a second profile (e.g. a canton) is actually needed.

**Consequences.**
- The converter stays single-file — no cross-schema import/refinement work needed yet.
- The core/profile boundary is a naming + section convention, not enforced by the tooling; discipline required to keep it clean so the later extraction is mechanical.
- SR-101 validates through the Fedlex profile layer.
