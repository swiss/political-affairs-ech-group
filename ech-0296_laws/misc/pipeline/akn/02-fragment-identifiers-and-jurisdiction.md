<!-- tags: akn, fragment, jurisdiction -->
# 02-fragment-identifiers-and-jurisdiction

## Purpose

Documents the fragment identifier system for Swiss legal documents in the AKN pipeline: the subdivision hierarchy, compact display syntax, document pointer resolution (short title / SR / AS), and jurisdiction shorthand resolution (canton codes / BFS numbers). These are the design decisions for the standard being written with eCH.

---

## 1. Swiss Legal Document Hierarchy

Swiss federal law (Bund) and cantonal law share a common hierarchical structure. Levels above the article are optional — they appear only in longer statutes.

```
Teil / Partie / Parte                   (part)       — optional
  Titel / Titre / Titolo               (title)      — optional
    Kapitel / Chapitre / Capitolo      (chapter)    — optional
      Abschnitt / Section / Sezione    (section)    — optional
        Unterabschnitt                 (subsection) — optional
          Artikel / Article / Articolo (article)    ← mandatory anchor
            Absatz / Alinéa / Capoverso (paragraph) — if numbered
            Ziffer / Chiffre / Cifra    (number)    — list with arabic numerals
            Buchstabe / Lettre / Lettera (litera)   — list with letters
              Doppelbuchstabe          (sublitera)  — double-letter subdivision
```

**Design decision F6:** Kapitel and Abschnitt are OPTIONAL wrappers. A reference without them is valid: `OR Art. 11 Abs. 3 lit. a`.

---

## 2. AKN Subdivision Codes

Per the AKN Naming Convention (OASIS 2019) and ELI Subdivisions v2 (EUR-Lex):

| Swiss term (DE) | Swiss term (FR) | Swiss term (IT) | AKN code | eId example |
|---|---|---|---|---|
| Teil | Partie | Parte | `part` | `part_3` |
| Titel | Titre | Titolo | `tit` | `tit_2` |
| Kapitel | Chapitre | Capitolo | `chp` | `chp_4` |
| Abschnitt | Section | Sezione | `sec` | `sec_1` |
| Unterabschnitt | Sous-section | Sottosezione | `subsec` | `subsec_2` |
| Artikel / Art. | Article / Art. | Articolo / Art. | `art` | `art_47` |
| Absatz / Abs. | Alinéa / Al. | Capoverso / cpv. | `para` | `para_2` |
| (unnumbered Absatz) | — | — | `unp` | `unp_1` |
| Ziffer / Ziff. | Chiffre / ch. | Cifra / n. | `num` | `num_3` |
| Buchstabe / lit. | Lettre / let. | Lettera / lett. | `lit` | `lit_a` |
| Doppelbuchstabe | — | — | `sublit` | `sublit_aa` |
| Spiegelstrich | tiret | trattino | `ind` | `ind_1` |
| Anhang | Annexe | Allegato | `anx` | `anx_2` |

**Design decision F4:** Ziffer uses `num` (not EU `pnt`) — matching DE/CH citation practice (`Ziff.` / `ch.`) and German LegalDocML.de.

**Design decision F3:** Numbered Absatz uses `para`; unnumbered uses `unp` (per AKN4EU practice for EU consolidated acts).

### Hierarchical eId (F7)

eIds are dot-separated from outermost to innermost:

```
art_47.para_2.lit_a
chp_3.sec_1.art_5.para_1.lit_b
art_11.num_3.lit_b
```

The full fragment URI appends `#eId` to the expression URI:

```
/akn/ch/lei/1999-01-01/404/deu@2021-03-07#art_47.para_2.lit_a
```

The ELI-style subdivision path (for API routing) uses slashes:

```
/akn/ch/lei/1999-01-01/404/art_47/para_2/lit_a
```

---

## 3. Compact Display Syntax (F11)

For UI display fields and short citations, a compact prefix system is defined. This is **display-only** — the canonical form is always the AKN eId.

### Prefix table

| Kind | Compact prefix | Example | Expansion |
|---|---|---|---|
| chapter (Kapitel) | `chp` | `#chp-2` | `chp_2` |
| section (Abschnitt) | `s` | `#s3` | `sec_3` |
| subsection | `sub` | `#sub-1` | `subsec_1` |
| article (Artikel) | `a` | `#a47` | `art_47` |
| paragraph (Absatz) | `p` | `#p2` | `para_2` |
| number (Ziffer) | `num` | `#num-3` | `num_3` |
| litera (Buchstabe) | `lit` | `#lit-a` | `lit_a` |
| sublitera | `slit` | `#slit-aa` | `sublit_aa` |
| annex (Anhang) | `anx` | `#anx-2` | `anx_2` |

### Formatting rules

- Single-letter prefixes (`a`, `s`, `p`) are glued to the value: `#a47`, `#p2`, `#s3`
- Multi-character prefixes are separated with `-`: `#chp-3`, `#num-3`, `#lit-a`, `#anx-2`
- Multiple levels are separated with `-`: `#a47-p2-lit-a`
- The `#` is always present; omitting it is accepted on input

### Examples

```
#a47                  → Art. 47
#a47-p2               → Art. 47 Abs. 2
#a47-p2-lit-a         → Art. 47 Abs. 2 lit. a
#a11-num-3-lit-b      → Art. 11 Ziff. 3 lit. b
#chp-3-s2-a5          → Kap. 3 Abschn. 2 Art. 5
#anx-2                → Anhang 2
```

### Relationship to AKN eId and FRBR URI

```
User display field:   BV#a47-p2-lit-a
Full fragment URI:    /akn/ch/lei/1999-01-01/404/deu@2021-03-07#art_47.para_2.lit_a
ELI subdivision URI:  /akn/ch/lei/1999-01-01/404/art_47/para_2/lit_a
Human citation (de):  BV Art. 47 Abs. 2 lit. a
Human citation (fr):  Cst. Art. 47 Al. 2 let. a
```

---

## 4. Document Pointer — Short Title / SR / AS Fallback Chain (F8)

When pointing to a whole document (no subdivision), a human-meaningful identifier is used. Priority order:

| Priority | Source | Example | AKN pointer |
|---|---|---|---|
| 1 | Official short title / abbreviation | `OR`, `DSG`, `ZGB`, `BV` | `or`, `dsg` |
| 2 | SR / LS citation number | `SR 220`, `LS 170.41` | `sr-220`, `sr-170-41` |
| 3 | AS / OS publication number (year/sequence) | `AS 2022/491` | `as-2022-491` |
| 4 | Composed: jurisdiction + year + seq | `ch/1999/404` | `ch-1999-404` |

**Rationale for F8:** Short titles (`OR`, `DSG`) are universally recognised by practitioners and stable. SR numbers are the next-best stable identifier. AS numbers are machine-readable but not human-recognisable; they are a fallback for communities that only have access to the AS (Official Compilation) — typically municipalities dealing with cantonal adoption notices.

**ZH-Lex:** The LS Ordnungsnummer (`170.41`) functions as the SR-equivalent for cantonal law and is used at priority 2.

**Communities without SR number:** Municipal bylaws (Gemeindereglemente) often have no systematic citation number — only a year and sequential number from the municipal gazette. The AS-number fallback `as-{year}-{seq}` covers this case, scoped by the BFS-based jurisdiction id: `ch-zh-261-as-2023-5`.

---

## 5. Jurisdiction Shorthand Resolution (F9, F10)

Any of these forms resolve to a canonical AKN jurisdiction id:

| Input | Resolves to | Notes |
|---|---|---|
| *(empty)* | `ch` | **F10: federal default** |
| `ch` | `ch` | Federal government |
| `ZH` | `ch-zh` | Canton code (ISO 3166-2:CH, case-insensitive) |
| `zh` | `ch-zh` | Lowercase accepted |
| `ZG` | `ch-zg` | — |
| `BE` | `ch-be` | — |
| `VD` | `ch-vd` | — |
| `261` | `ch-zh-261` | BFS number → KNOWN_BFS lookup |
| `351` | `ch-be-351` | — |
| `5586` | `ch-vd-5586` | — |
| `1702` | `ch-zg-1702` | — |
| `4001` | `ch-ag-4001` | Range-based: 4001–4500 → AG |
| `5100` | `ch-ti-5100` | Range-based: 5001–5400 → TI |
| `ch-zh` | `ch-zh` | Passthrough (canonical) |
| `ch-zh-261` | `ch-zh-261` | Passthrough |

### BFS number resolution

BFS (Bundesamt für Statistik) municipality numbers are permanent identifiers assigned by the Federal Statistical Office. They do not change even if the municipality is renamed; they are retired only on merger.

Resolution uses two mechanisms:
1. **Known BFS table** (KNOWN_BFS): hard-coded entries for well-known municipalities
2. **Range table** (_BFS_RANGES): approximate canton assignment by numeric range

The range table is an approximation — the precise BFS allocation is available from the official BFS Amtliches Gemeindeverzeichnis. For production use, a full BFS → canton mapping CSV should replace the range table.

### All canton codes

| Canton | Code | AKN id |
|---|---|---|
| Zürich | ZH | ch-zh |
| Bern | BE | ch-be |
| Luzern | LU | ch-lu |
| Uri | UR | ch-ur |
| Schwyz | SZ | ch-sz |
| Obwalden | OW | ch-ow |
| Nidwalden | NW | ch-nw |
| Glarus | GL | ch-gl |
| Zug | ZG | ch-zg |
| Fribourg | FR | ch-fr |
| Solothurn | SO | ch-so |
| Basel-Stadt | BS | ch-bs |
| Basel-Landschaft | BL | ch-bl |
| Schaffhausen | SH | ch-sh |
| Appenzell AR | AR | ch-ar |
| Appenzell AI | AI | ch-ai |
| St. Gallen | SG | ch-sg |
| Graubünden | GR | ch-gr |
| Aargau | AG | ch-ag |
| Thurgau | TG | ch-tg |
| Ticino | TI | ch-ti |
| Vaud | VD | ch-vd |
| Valais / Wallis | VS | ch-vs |
| Neuchâtel | NE | ch-ne |
| Genève | GE | ch-ge |
| Jura | JU | ch-ju |

---

## 6. Page Fetcher Metadata

The `fetch_metadata(url)` function enriches a parsed URL with data from the actual HTML page. It supports:

- **Fedlex:** Strategy A (OG/meta tags) + Strategy B (JSON-LD) + Strategy C (Fedlex data API JSON at `fedlex.data.admin.ch`). Fedlex is a JS SPA; the data API is the most reliable source.
- **ZH-Lex legacy** (`zhlex.zh.ch`): Static HTML with labeled fields (Erlassdatum, Inkraftsetzungsdatum, Abkürzung).
- **ZH.ch portal** (`zh.ch/zhlex-ls/`): Structured HTML with OG tags.

Fields extracted:

| Field | Source | Notes |
|---|---|---|
| `title_de/fr/it` | OG tag / JSON-LD / API | Multilingual title |
| `short_title` | API `abbreviation` / page text `Abkürzung` | e.g. `OR`, `DSG` |
| `sr_number` | API taxonomy URI / page label | e.g. `220`, `235.1` |
| `enactment_date` | API `dateDocument` / `Erlassdatum` | ISO 8601 |
| `entry_into_force` | API `dateEntryInForce` / `Inkraftsetzungsdatum` | ISO 8601 |
| `repeal_date` | API `dateNoLongerInForce` / `Aufhebungsdatum` | ISO 8601 |
| `publication_date` | API / `Publikationsdatum` | ISO 8601 |
| `status` | Derived from dates | `current`, `repealed`, `future`, `unknown` |

---

## 7. Complete Reference Object

A `LegalReference` produced by `LegalReferenceBuilder.from_url()` exposes:

```python
ref.fragment_uri        # Full expression URI + AKN fragment
                        # /akn/ch/lei/1999-01-01/404/deu@2021-03-07#art_47.para_2.lit_a

ref.work_fragment_uri   # Version-independent work URI + fragment
                        # /akn/ch/lei/1999-01-01/404#art_47.para_2.lit_a

ref.eli_subdivision_uri # ELI-style slash path (for API routing)
                        # /akn/ch/lei/1999-01-01/404/art_47/para_2/lit_a

ref.display_uri         # Compact human URI (for UI display field)
                        # bv#art_47.para_2.lit_a

ref.human_citation("de") # "BV Art. 47 Abs. 2 lit. a"
ref.human_citation("fr") # "Cst. Art. 47 Al. 2 let. a"
ref.human_citation("it") # "Cost. Art. 47 cpv. 2 lett. a"
```

The compact display syntax for the UI field:
```python
from frbr_uri.fragment import compact_fragment
compact_fragment(ref.fragment)   # "#a47-p2-lit-a"
```

---

## 8. Open Questions for Standard Discussion

These items require community evaluation before standardisation:

**Q1: AS number format for municipal bylaws.** Communities with only AS/OS numbers typically use year + sequential number. Proposed: `{jurisdiction}-as-{year}-{seq}`, e.g. `ch-zh-261-as-2023-5`. Alternative: include parliamentary affair number if available.

**Q2: Ziffer (`num`) vs `pnt`.** The EU ELI spec uses `pnt` for numbered list items. Swiss law uses Ziffer (arabic) distinct from Buchstabe (alphabetical) and Spiegelstrich (dash). Decision F4 uses `num` — confirm with eCH working group.

**Q3: BFS number scope.** The BFS Amtliches Gemeindeverzeichnis should be integrated as a downloadable data source rather than a static range table. Suggest periodic sync from the official API.

**Q4: Short title registry.** No authoritative machine-readable list of Swiss law short titles exists. Fedlex provides abbreviations in its RDF graph (accessible via SPARQL). A community-maintained registry JSON file in the profiles directory would cover gaps.

---

## 9. Implementation Files

| File | Purpose |
|---|---|
| `packages/frbr_uri/fragment.py` | SubdivisionRef, FragmentRef, compact syntax, jurisdiction resolution |
| `packages/frbr_uri/reference.py` | LegalReferenceBuilder, LegalReference |
| `packages/frbr_uri/parsers/url_parser.py` | URL → ParsedDocumentUrl |
| `packages/frbr_uri/parsers/page_fetcher.py` | HTTP fetch → FetchedMetadata |
| `packages/frbr_uri/tests/test_fragment_and_reference.py` | 97 tests |
| `packages/frbr_uri/tests/test_url_parser.py` | 25 URL parser tests |
| `packages/frbr_uri/tests/test_resolver.py` | 19 FRBR resolver tests |
