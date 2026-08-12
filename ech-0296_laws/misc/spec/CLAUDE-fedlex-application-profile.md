# The Fedlex Akoma Ntoso Profile — and how to extend it for Cantons & Municipalities

This document describes the schema stack in `input/schemas/`, the effective
sub-schema it defines, the Schematron mechanics that enforce it, and a proposed
architecture for extending the model to cantonal / municipal legislation with
dual publication (Akoma Ntoso XML **or** LinkML) and DCAT-AP-CH packaging.

---

## 1. The schema stack

| Layer | File | Role |
|---|---|---|
| Foundation | `xml.xsd` | The `xml:` namespace attributes (`xml:lang`, `xml:space`, `xml:base`, `xml:id`). |
| Grammar | `akomantoso30.xsd` | Full Akoma Ntoso 3.0 (OASIS LegalDocML) vocabulary: **315 elements**, 59 complexTypes, 74 attributeGroups, 33 groups, 28 simpleTypes. Defines what is *structurally possible*. |
| Profile | `AKN-fedlex.sch` | Schematron **restriction layer** (24 rules, `queryBinding="xslt2"`) that narrows the permissive AKN grammar to the subset Fedlex actually allows. |

**Governing principle:** the XSD is *permissive*, the Schematron is *subtractive*.
The Schematron never adds elements — it only forbids or constrains. The effective
allowed set in any context =
`{what the XSD permits there}  −  {what the Schematron rejects there}`.
It clamps **document structure** (the act hierarchy), not the inline text
vocabulary — inline elements (`ref`, `b`, `i`, `span`, `a`, `num` …) stay legal
wherever the base XSD allows them.

Namespaces:
- AKN: `http://docs.oasis-open.org/legaldocml/ns/akn/3.0` (prefix `akn`)
- Fedlex extensions: `http://fedlex.admin.ch/` (prefix `fedlex`)
- Schematron functions: `urn:com:c-moria:fedlex:schematron:functions` (prefix `fun`)

---

## 2. The effective Fedlex sub-schema

### 2.1 Root — only `act` (`FLX-RT-001`)
Base AKN allows 12 document types under `akomaNtoso`
(`act, bill, debate, debateReport, statement, amendment, judgment, portion, doc,
amendmentList, officialGazette, documentCollection`).
**Fedlex allows only `akn:act`.**

### 2.2 Preface (`FLX-PF-001/002`)
Must contain `p/docNumber` **and** `p/docTitle`.

### 2.3 Body top-level children (`FLX-BD-001`)
Direct children of `act/body` may only be:
`book, title, part, chapter, subchapter, section, subsection, level, article,
transitional, proviso`.

### 2.4 Hierarchical containment matrix (`fun:is-legal-hier-child`, `FLX-HR-001-*`)
Each container may contain only these hierarchical children (plus heading
elements, plus `article`, which is always allowed):

| Container | Allowed hierarchical children |
|---|---|
| `book` | title, part, chapter, subchapter, section, subsection, level |
| `title` | book, part, chapter, subchapter, section, subsection, level |
| `part` | chapter, subchapter, section, subsection, level |
| `chapter` | subchapter, section, subsection, level |
| `subchapter` | section, subsection, level |
| `section` | subsection, level |
| `subsection` | level |
| `level` | inherits nearest non-`level` ancestor's rule (`level` is "transparent") |
| `article` | always legal anywhere |

### 2.5 Heading elements (`fun:is-heading-element`, `FLX-HD-001…006`)
`num`, `heading`, `subheading` — allowed on every hierarchical container.
At most one of each; order must be `num` → `heading` → `subheading`.

### 2.6 Article / subdivision / paragraph content models
- `article` (`FLX-ART`): `num` **mandatory**; children ⊆ {heading-elements, `paragraph`, `subdivision`}.
- `subdivision` (`FLX-SD`): children ⊆ {heading-elements, `paragraph`}; must be a direct child of `article`.
- `paragraph` (`FLX-PR`): children ⊆ {heading-elements, `content`}; must be child of `article` or `subdivision`.
- `level` with `content` (`FLX-HR-003`): content allowed **only** if it contains a `mod` (modification).

### 2.7 `eId` required (`FLX-HR-002-*`, `-004`, `FLX-ART-003`, `FLX-SD-003`, `FLX-PR-003`)
On: `title, book, part, chapter, subchapter, section, subsection, level, article,
subdivision, paragraph`.

### 2.8 `br` (`FLX-TXT-001`)
Allowed only inside `docTitle`, `heading`, `subheading`.

### 2.9 Fedlex extension attributes (`@fedlex:*`, `FLX-XF-001…005`)
The only two custom attributes permitted (see §4 for semantics):
- `fedlex:role` — `reference` (only on `subheading`) or `marginal` (only on `level`).
- `fedlex:generator` — only on `FRBRformat[@value='xml']`.
Any other `fedlex:*` attribute is rejected.

---

## 3. Schematron mechanics (XPath 2.0 / XSLT2)

### `except` + sequence logic
XPath 2.0 works on **sequences** with set operators: `|`/`union`, `except`
(difference), `intersect`, and cardinality tests `empty()`/`exists()`. Fedlex
expresses whitelists with one idiom (from `FLX-ART-002`):

```xpath
empty( * except (*[fun:is-heading-element(.)] | akn:paragraph | akn:subdivision) )
```

- `*` = all children
- `(… | … | …)` = the allowed children (unioned)
- `* except (…)` = the *illegal* remainder
- `empty(…)` = assert the remainder is empty

i.e. "every child must be one of the allowed types." A closed-world whitelist by
subtraction.

### Custom `fun:` functions
`queryBinding="xslt2"` lets the schema declare reusable `<xsl:function>`s:
- `fun:is-heading-element($e)` → true for `num`/`heading`/`subheading`.
- `fun:is-legal-hier-child($e, $ln)` → the containment matrix of §2.4 as an
  `<xsl:choose>`, taking the child and the parent's local-name. `article`/`body`
  short-circuit to true; `level` passes its nearest non-level ancestor's name,
  which is what "transparent" means.

### Consequence for format conversion
Neither `except`/sequence set-difference nor imperative `xsl:function` calls have
equivalents in JSON Schema or LinkML. These are **context-sensitive computed
constraints**. A mechanical Schematron→JSON/LinkML converter cannot reproduce
them; they must be **re-authored** as validation logic (LinkML `rules:` with
preconditions, or a validator plugin) or **kept as a separate Schematron step**
in the pipeline. Structural cardinality/containment converts; cross-context
assertions do not.

---

## 4. The two Fedlex extension attributes

Both live in `http://fedlex.admin.ch/` and are the *only* Fedlex additions on top
of stock AKN. They demonstrate the two layers at which any jurisdiction extends:

- **`fedlex:role`** — a **content-semantic** annotation inside the body.
  - `marginal` (only on `<level>`): a marginal note / Randtitel / note marginale.
  - `reference` (only on `<subheading>`): a reference-style subheading.
- **`fedlex:generator`** — a **manifestation/metadata** annotation, only on
  `<FRBRformat value="xml">`: records that this XML manifestation was
  machine-generated rather than hand-authored (an audit marker in the FRBR block).

`FLX-XF-001` rejects any `fedlex:*` attribute other than these two — a deliberately
tiny, closed extension surface. This role/generator split (body-semantic vs
metadata-provenance) is the seam the cantonal/municipal model reuses.

---

## 5. Extension architecture for Cantons & Municipalities

The system separates cleanly into **three independent layers**. Extension happens
per-layer, and a publisher can adopt as many layers as their tooling supports.

```
┌────────────────────────────────────────────────────────────────┐
│ Layer 3  PACKAGING / DISTRIBUTION        DCAT-AP-CH (RDF/JSON-LD)│
│          law + all its versions/languages/formats as a dataset  │
├────────────────────────────────────────────────────────────────┤
│ Layer 2  METADATA (bibliographic)        LinkML, FRBR model     │
│          Work / Expression / Manifestation / Item               │
├────────────────────────────────────────────────────────────────┤
│ Layer 1  CONTENT (the legal text)        AKN 3.0 + Schematron   │
│          Fedlex base profile + cantonal restriction layers      │
└────────────────────────────────────────────────────────────────┘
```

### Layer 1 — Content grammar (Akoma Ntoso XML)
Cantons/municipalities reuse `akomantoso30.xsd` + `AKN-fedlex.sch` **unchanged as
the base**, and extend by *adding* — never editing — a jurisdiction Schematron
layer:

- `AKN-canton-ZH.sch`, `AKN-commune-XYZ.sch`, … each *further restricts* or adds
  jurisdiction rules. Schematron is **additive**: validation runs base rules **and**
  the canton rules; nothing in the base is lost.
- Jurisdiction-specific custom attributes go in the jurisdiction's own namespace
  (`zh:role`, etc.), mirroring exactly how Fedlex added `fedlex:role`/`generator`
  and closed the set with a gatekeeper rule.
- Result: valid AKN XML publishable through the same toolchain as Fedlex.

**Validation pipeline (ground truth):**
```
document.xml
  → xmllint --schema akomantoso30.xsd          # structural (XSD)
  → SchXslt/Saxon AKN-fedlex.sch                # Fedlex profile
  → SchXslt/Saxon AKN-canton-ZH.sch             # jurisdiction layer (optional)
```

### Layer 2 — Metadata (FRBR via LinkML)
This is where publishers **without XML tooling** work. It is the model already
prototyped in
`ech-0292_meta/input/data_fedlex-dl_2024_65.yaml`, which encodes the FRBR
hierarchy directly:

```
Work        fedlex:dl/2024/65            (the law as an abstract intellectual work)
 └ Expression  fedlex:dl/2024/65/de      (a language version)
    └ Manifestation fedlex:dl/2024/65/de/pdf   (a concrete format: xml/pdf/html)
       └ Item     (the actual file / byte stream)
```

- The same FRBR structure already exists **inside every AKN act** in
  `<meta>/<identification>`: `FRBRWork`, `FRBRExpression`, `FRBRManifestation`,
  each with `FRBRuri`, `FRBRdate`, `FRBRlanguage`, `FRBRformat`, `FRBRauthor`.
  So the LinkML metadata schema and the AKN `<identification>` block are two
  serializations of **one** FRBR model — they can be kept in lock-step.
- ech-0292 currently models **meta document types**; the *same* pattern applies to
  **acts (`act`/`bill`)** — one shared LinkML `Work/Expression/Manifestation/Item`
  schema, with `work_types` distinguishing `dl` (draft legislation), `act`, etc.
- Author once in LinkML YAML, then **generate** the artifacts each audience needs:
  - `gen-json-schema` → validation for JSON/YAML authors
  - `gen-jsonld-context` / `gen-rdf` → Linked Data (feeds Layer 3)
  - `gen-owl` / `gen-shacl` → ontology / RDF validation
  - (XSD generation is weak in LinkML; keep the **content** in AKN's own XSD and
    use LinkML only for the **metadata** layer — do not try to regenerate AKN.)
- **Extension = LinkML inheritance.** A canton schema `imports:` the Fedlex base
  LinkML schema and specializes classes via `is_a:` / `mixins:`, adding slots or
  tightening `pattern`/`enum` constraints. This is the LinkML analogue of adding a
  Schematron layer in Layer 1.

**Dual publication.** A municipality can therefore either:
- (a) author full AKN XML like Fedlex (Layer 1), **or**
- (b) author LinkML metadata + lighter content, and a transform emits AKN
  `<identification>` and/or the DCAT distributions.
Both routes converge because both are projections of the same FRBR model.

### Layer 3 — Packaging & distribution (DCAT-AP-CH)
A "law package" = one law (Work) bundled with all its **versions over time**,
**languages** (Expressions) and **formats** (Manifestations) for distribution on
opendata.swiss. DCAT-AP-CH (v3.0.1, RDF / Turtle / JSON-LD) maps onto FRBR almost
one-to-one:

| FRBR (AKN `<identification>` / ech-0292) | DCAT-AP-CH |
|---|---|
| Work (the law, all versions) | `dcat:DatasetSeries` |
| Expression / point-in-time version | `dcat:Dataset` (a version, member of the series) |
| Manifestation (xml / pdf / html file) | `dcat:Distribution` |
| `FRBRformat` | `dcat:mediaType` / `dct:format` on the distribution |
| `FRBRlanguage` | `dct:language` |
| `FRBRuri` / eId | `dct:identifier` |
| `FRBRdate`, lifecycle dates | `dct:issued` / `dct:modified` |
| Catalogue of all laws | `dcat:Catalog` |

Because Layer 2 is LinkML, the DCAT-AP-CH output is **generated**, not hand-kept:
add `class_uri: dcat:Dataset`, `slot_uri: dct:language`, `exact_mappings:` to the
LinkML slots, emit a JSON-LD context, and the same instance YAML serializes to
valid DCAT-AP-CH RDF for opendata.swiss. Versioning is native: each Expression
becomes a dated `dcat:Dataset` within the law's `dcat:DatasetSeries`.

---

## 6. Document-type usage intent (the 12 AKN root types)

Base AKN allows 12 document types under `akomaNtoso`. The Fedlex profile currently
admits only `act` (`FLX-RT-001`), but the cantonal/municipal extension will widen
this by relaxing that root rule per publisher. Planned usage:

| # | AKN type | Status | Intended Swiss use |
|---|---|---|---|
| 1 | `act` | **ACTIVE** | Consolidated enacted law (SR/RS), including the Federal Constitution (SR 101). The one type Fedlex allows today. |
| 2 | `bill` | **ACTIVE** | Draft legislation / Vorlage / Entwurf in the legislative process — the `dl` ("draft legislation") work type already modelled in ech-0292. |
| 3 | `amendment` | PLANNED | Standalone amending instrument (Änderungserlass) when not expressed as `mod`s inside an act. |
| 4 | `amendmentList` | PLANNED | Change-set / list of amendments bundling several amending actions. |
| 5 | `officialGazette` | PLANNED | AS (Amtliche Sammlung) / BBl (Bundesblatt) publication container. |
| 6 | `documentCollection` | PLANNED | Compilation / distribution package — the SR compilation itself, or a cantonal register. Pairs with the DCAT-AP-CH package (Layer 3). |
| 7 | `doc` | PLANNED | Generic catch-all: messages (Botschaft), reports, explanatory notes — anything without a dedicated type. |
| 8 | `portion` | PLANNED | Addressable fragment: a single article/`eId` delivered standalone (point-in-time citation, API responses). |
| 9 | `debate` | RESERVED | Parliamentary debate verbatim (Amtliches Bulletin). Parliamentary domain — future. |
| 10 | `debateReport` | RESERVED | Report of a debate. Future. |
| 11 | `statement` | RESERVED | Ministerial / written / personal statements. Future. |
| 12 | `judgment` | RESERVED | Court decisions / jurisprudence (e.g. BGE). Reserved for a future courts programme. |

The same intent is encoded machine-readably in the `WorkType` enum of
`input/linkml/akn-frbr.yaml` (each value carries ACTIVE/PLANNED/RESERVED and a
`meaning:` mapped to the AKN element).

## 7. Worked examples from SR 101 (Federal Constitution)

Snippets below are from `input/examples/federal/SR-101-03032024-DE.xml` (the
published XML manifestation of the Constitution), one per Schematron rule.

**`FLX-RT-001` — root only `act`** ✅
```xml
<akomaNtoso …>
    <act name="publicLaw">          <!-- the only child of akomaNtoso -->
```

**`FLX-PF-001/002` — preface needs `docNumber` + `docTitle`** ✅
```xml
<preface>
    <p><docNumber>101</docNumber></p>
    <p><docTitle>Bundesverfassung <br />der Schweizerischen Eidgenossenschaft</docTitle></p>
</preface>
```
(also demonstrates **`FLX-TXT-001`** — `<br/>` is legal here because it sits inside `docTitle`.)

**`FLX-BD-001` — body top-level ∈ allowlist** ✅ (`title` is permitted)
**`FLX-HR-002-*` — hierarchy needs `eId`** ✅ · **`FLX-HD-001..003` — `num` before `heading`** ✅
```xml
<body>
    <title eId="tit_1">
        <num>1. Titel: </num>
        <heading>Allgemeine Bestimmungen</heading>
```

**`FLX-HR-001/002` — nested hierarchy + `eId`** ✅ (section inside title/chapter, path-style eId)
```xml
<section eId="tit_3/chap_1/sec_1"> … </section>
```

**`FLX-ART-001/002/003` — `num` mandatory, content ⊆ {heading, paragraph, subdivision}, `eId`** ✅
**`FLX-PR-001/002/003` — paragraph ⊆ {heading, content}, child of article/subdivision, `eId`** ✅
```xml
<article eId="art_1">
    <num><b>Art. 1</b></num>
    <heading>Schweizerische Eidgenossenschaft</heading>
    <paragraph eId="art_1/para">
        <content><p>Das Schweizervolk und die Kantone …</p></content>
    </paragraph>
</article>
```

**`FLX-XF-002` — `fedlex:generator` only on `FRBRformat[@value='xml']`** ✅
```xml
<FRBRformat value="xml" fedlex:generator="2026-q1-rel-1.8.5" />
```

**`FLX-XF-001/003` — VIOLATIONS in the published file** ⚠️
The 2026 published Constitution uses `fedlex:` attributes that the repo's
2023-12 Schematron would **reject**:
```xml
<p fedlex:role="heading">        <!-- FLX-XF-003: role must be 'reference'|'marginal' -->
… fedlex:rs="101" …               <!-- FLX-XF-001: 'rs' is not an allowed fedlex attr -->
… fedlex:message="E40S10-TAB" …   <!-- FLX-XF-001: 'message' is not an allowed fedlex attr -->
```
**Implication:** the Fedlex extension vocabulary has grown since `AKN-fedlex.sch`
was written (it now includes at least `rs`, `message`, and `role='heading'`). Any
cantonal/municipal profile must **track the current Fedlex extension set**, not the
snapshot in this repo — treat `AKN-fedlex.sch` as a versioned baseline to be
re-synced, and confirm the live allowlist before enforcing `FLX-XF-*`.

*(Rules `FLX-SD-*` for `subdivision` and `FLX-HR-003` for `level`-with-`content`
also fire against this file — it contains 32 subdivisions and modification levels —
but the two snippets above already show the pattern.)*

## 8. Recommended build order

1. **Keep Layer 1 as-is.** Validate real acts with `xmllint` + SchXslt/Saxon over
   `akomantoso30.xsd` + `AKN-fedlex.sch`. Add cantonal `.sch` layers as needed.
2. **Lift ech-0292's FRBR YAML into a proper LinkML schema** covering
   `Work/Expression/Manifestation/Item`, generalized from `dl` to `act`/`bill`.
   Add DCAT-AP-CH mappings on the slots from day one.
3. **Generate**, don't hand-write: JSON Schema (validation), JSON-LD/RDF
   (DCAT-AP-CH packaging for opendata.swiss).
4. **Do not** attempt to regenerate the AKN content grammar from LinkML, and **do
   not** expect the Schematron cross-context rules (§3) to survive conversion —
   re-author those as LinkML `rules:` or keep them as the Schematron step.

---

## 9. Complete allowed inventories (base AKN 3.0 grammar)

### Attributes (72 AKN + 4 `xml:` + 2 `fedlex:`)
AKN: `alt alternativeTo as authoritative border breakAt breakWith by cellpadding
cellspacing choice class colspan contains current date dictionary duration eId
empoweredBy end endQuote endTime exclusion for from fromLanguage frozen GUID
height href includedIn incomplete inlineQuote language level marker name normalized
number original originalText originatingExpression outcome period pivot placement
placementBase pos refersTo rowspan shortForm showAs source src start startQuote
startTime status style target time title to type upTo value wId width`
`xml:` → `base id lang space`  ·  `fedlex:` → `role generator`

### Elements (315)
`a abbr act activeModifications activeRef address adjournment administrationOfOath
affectedDocument akomaNtoso alinea alternativeReference amendment amendmentBody
amendmentContent amendmentHeading amendmentJustification amendmentList
amendmentReference analysis answer application applies argument arguments article
attachment attachmentOf attachments authorialNote b background bill block
blockContainer blockList body book br caption change chapter citation citations
classification clause collectionBody communication component componentData
componentInfo componentRef components concept conclusions condition container
content contrasts count courtType coverPage crossHeading date debate debateBody
debateReport debateSection decision declarationOfVote decoration def del derogates
destination dissentsFrom distinguishes div division doc docAuthority docCommittee
docDate docIntroducer docJurisdiction docketNumber docNumber docProponent docPurpose
docStage docStatus docTitle docType documentCollection documentRef domain duration
efficacy efficacyMod embeddedStructure embeddedText entity eol eop event eventRef
extends fillIn force forceMod foreign formula FRBRalias FRBRauthor FRBRauthoritative
FRBRcountry FRBRdate FRBRExpression FRBRformat FRBRItem FRBRlanguage FRBRManifestation
FRBRmasterExpression FRBRname FRBRnumber FRBRportion FRBRprescriptive FRBRsubtype
FRBRthis FRBRtranslation FRBRuri FRBRversionNumber FRBRWork from hasAttachment
hcontainer header heading i identification img implicitReference indent inline ins
interstitial intro introduction isAnalogTo item judge judgment judgmentBody judicial
jurisprudence keyword lawyer legalSystemMod legislature level li lifecycle list
listIntroduction listWrapUp location longTitle mainBody mapping mappings marker
meaningMod meta ministerialStatements mmod mod motivation mref narrative
nationalInterest neutralCitation new note noteRef notes noticesOfMotion num object
officialGazette ol omissis opinion oralStatements organization original other
otherAnalysis otherReferences outcome overrules p papers paragraph parliamentary
part party passiveModifications passiveRef person personalStatements petitions
placeholder point pointOfOrder portion portionBody prayers preamble preface
presentation preservation previous proceduralMotions process proprietary proviso
publication putsInQuestion quantity question questions quorum quorumVerification
quotedStructure quotedText recital recitals recordedTime recount ref references
relatedDocument remark remedies resolutions restriction restrictions restricts
result rmod role rollCall rref rule scene scopeMod section session shortTitle
signature source span speech speechGroup statement step sub subchapter subclause
subdivision subFlow subheading sublist subparagraph subpart subrule subsection
subtitle summary sup supports table tblock td temporalData temporalGroup term
textualMod th time timeInterval title TLCConcept TLCEvent TLCLocation TLCObject
TLCOrganization TLCPerson TLCProcess TLCReference TLCRole TLCTerm toc tocItem tome
tr transitional u ul vote voting workflow wrapUp writtenStatements`
