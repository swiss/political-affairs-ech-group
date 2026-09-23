# LinkML is the source of truth; the generated XSD + Schematron must validate the real SR-101

**Context.** eCH-0296 models Swiss federal legal texts. Fedlex already publishes them as Akoma Ntoso 3.0 XML, governed by the OASIS `akomantoso30.xsd` and the Fedlex `AKN-fedlex-*.sch` Schematron. We are building a LinkML schema (`ech-0296_laws/input/schema.yaml`) and extending the `linkml-to-xsd` converter (`/Users/christian/Bitbucket/linkml`).

**Decision.** The LinkML schema is the single source of truth. From it we generate (a) a Fedlex-subset XSD and (b) a Schematron. The binding acceptance test is: **the real, unmodified `SR-101-01012029-DE.xml` must validate against the generated XSD and pass the generated Schematron.** The generated XSD need not be byte-identical to OASIS `akomantoso30.xsd` — only functionally equivalent over the Fedlex subset.

**Consequences.**
- Inline/mixed content (`akn:ref`, `b`, `i`, `sup`, `authorialNote`, …) cannot be modeled as an opaque string; the real file interleaves text and markup, so a `xs:string` content model would reject it. Mixed content must be handled for real. See ADR-0002.
- The converter must gain: XML attributes, mixed content, namespaces/`xml:` import, element-name ≠ slot-name, and `xs:choice`. These are currently all absent.
- SR-101 becomes a permanent regression fixture: every converter/schema change is checked by re-validating it.
