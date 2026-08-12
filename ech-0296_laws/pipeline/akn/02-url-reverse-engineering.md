<!-- tags: akn, uri-patterns, fedlex, zh-lex -->
# 02-url-reverse-engineering

## Purpose

This document reverse-engineers the URL/URI structures of two authoritative Swiss legal publication platforms — **Fedlex** (federal) and **ZH-Lex** (Kanton Zürich) — and maps each segment to its FRBR and Akoma Ntoso equivalent. It serves as the evidentiary basis for the URI design decisions recorded in the FRBR URI profile standard (`profile.schema.json`).

---

## 1. Fedlex (federal.admin.ch)

### 1.1 Platform Architecture

Fedlex operates two distinct URL namespaces:

| Namespace | Base | Purpose |
|---|---|---|
| **Data URI** | `https://fedlex.data.admin.ch/eli/…` | Stable identifier for linked data, metadata (RDF/JOLux) |
| **Web URL** | `https://www.fedlex.admin.ch/eli/…` | Human-readable frontend (redirects from data URI) |
| **Filestore** | `https://fedlex.data.admin.ch/filestore/…` | Binary and structured file downloads |

The **data URI** and **web URL** differ only by subdomain (`fedlex.data.` vs `www.`). Putting a data URI in a browser redirects to the web URL. The data URI is the canonical stable identifier.

### 1.2 Publication Types and Path Roots

| Collection | German | French | Italian | Path | Approx. count |
|---|---|---|---|---|---|
| Classified Compilation | SR (Systematische Rechtssammlung) | RS | RS | `/eli/cc/` | ~17,000 acts + ~50,000 consolidated versions |
| Official Compilation | AS (Amtliche Sammlung) | RO | RU | `/eli/oc/` | ~45,000 |
| Federal Gazette | BBl (Bundesblatt) | FF | FF | `/eli/fga/` | ~146,000 |
| Treaties | — | — | — | `/eli/treaty/` | ~18,500 |
| Consultation procedures | Vernehmlassungen | — | — | `/eli/dl/proj/` | ~2,000 |

**Decision for AKN mapping:** The path root (`cc`, `oc`, `fga`) maps to the FRBR **Work type** identifier. `cc` = consolidated classified law → AKN `act` with `consolidation` subtype. `oc` = official compilation entry → AKN `act` with `originalVersion` subtype.

### 1.3 Classified Compilation (SR) URI Anatomy

```
https://fedlex.data.admin.ch/eli/cc/{pub_year}/{sr_number}
```

**Work level** (identifies the law, independent of language or version):

```
https://fedlex.data.admin.ch/eli/cc/1999/404
                              ─── ── ──── ───
                              eli  cc  year  SR-internal-number
```

- `cc` = Classified Compilation
- `1999` = year of first publication in the AS/Official Compilation (not the enactment year)
- `404` = sequential publication number within that year (not the SR/RS citation number)

**Example — Swiss Federal Constitution:**
- SR citation: `SR 101`
- Work URI: `https://fedlex.data.admin.ch/eli/cc/1999/404`
- Web URL: `https://www.fedlex.admin.ch/eli/cc/1999/404/de`

⚠️ **Important:** The number `404` in the URI is the **AS publication number**, not the SR number `101`. The SR number is carried in metadata (RDF), not the URI.

**Expression level** (language + consolidated version):

```
https://fedlex.data.admin.ch/eli/cc/{pub_year}/{pub_number}/{version_date}/{lang}
```

```
https://fedlex.data.admin.ch/eli/cc/1999/404/20210307/de
                                              ──────── ──
                                              YYYYMMDD  lang (2-letter ISO 639-1)
```

- `20210307` = consolidation date (the state of law as of that date), in `YYYYMMDD` format (no hyphens)
- `de` = 2-letter language code (de, fr, it, rm, en)

**Manifestation level** (format):

```
https://fedlex.data.admin.ch/eli/cc/{year}/{number}/{version}/{lang}/{format-type}/{filename}
```

```
https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1999/404/20210307/de/html/fedlex-data-admin-ch-eli-cc-1999-404-20210307-de-html-1.html
```

Format types observed: `html`, `pdf-a`, `xml` (AKN XML since 2022-05-30)

**Filename convention:**
```
fedlex-data-admin-ch-eli-cc-{year}-{number}-{version}-{lang}-{format}-{seq}.{ext}
```
All path separators become `-` in the filename. The `{seq}` is typically `1` for single-part documents.

### 1.4 Official Compilation (AS) URI Anatomy

```
https://fedlex.data.admin.ch/eli/oc/{year}/{pub_number}
```

Example:
```
https://fedlex.data.admin.ch/eli/oc/2022/491
```
- `year` = publication year in the AS
- `pub_number` = sequential number within that year

### 1.5 Federal Gazette (BBl) URI Anatomy

```
https://fedlex.data.admin.ch/eli/fga/{year}/{pub_number}/{lang}
```

Example observed:
```
https://www.fedlex.admin.ch/eli/fga/2009/876/de
```
The BBl includes the language at work level (unlike CC which puts it at expression level), reflecting that BBl articles are language-specific publications.

### 1.6 Observed Language Codes

| Code | Language |
|---|---|
| `de` | German |
| `fr` | French |
| `it` | Italian |
| `rm` | Romansh |
| `en` | English (translations only, non-authoritative) |

Note: Fedlex uses 2-letter ISO 639-1 codes at the URL level. AKN requires 3-letter ISO 639-2 codes in `xml:lang` attributes and FRBR URIs. The resolver handles this mapping.

### 1.7 Fedlex → AKN FRBR URI Mapping Table

| Fedlex segment | Meaning | AKN/FRBR equivalent |
|---|---|---|
| `eli` | ELI namespace | part of AKN prefix `/akn/ch` |
| `cc` | Classified Compilation | Work subtype = `lei` (consolidated law) |
| `oc` | Official Compilation | Work subtype = `as` (original publication) |
| `fga` | Federal Gazette | Work subtype = `bbl` |
| `{year}` | Publication year in AS | `{date}` component (year part) |
| `{number}` | Pub sequence number | `{number}` component |
| `{version_date}` | `YYYYMMDD` consolidation date | `@{version}` expression component (convert to ISO 8601) |
| `{lang}` (2-letter) | Language | `/{lang3}` (mapped to 3-letter) |
| `html`/`xml`/`pdf-a` | Format | `.{format}` manifestation extension |

**Conversion decisions:**
1. Fedlex `YYYYMMDD` dates → AKN `YYYY-MM-DD` (insert hyphens)
2. Fedlex 2-letter lang codes → AKN 3-letter: `de→deu`, `fr→fra`, `it→ita`, `rm→roh`, `en→eng`
3. Fedlex has no explicit Work-level date separate from pub year; AKN Work URI uses `{year}-01-01` as placeholder unless OS enactment date is known from metadata
4. The SR citation number (e.g. `101`, `235.1`) is recorded in AKN `<FRBRnumber>` element, not in the FRBR URI path

---

## 2. ZH-Lex (Kanton Zürich)

### 2.1 Platform Architecture

ZH-Lex operates two URL styles with a transition between old and new systems:

| System | Base URL | Status |
|---|---|---|
| **ZHlex legacy** | `http://www.zhlex.zh.ch/Erlass.html` | Still used for stable deep-links |
| **ZH.ch portal** | `https://www.zh.ch/de/politik-staat/gesetze-beschluesse/gesetzessammlung/zhlex-ls/` | Current web frontend |

Unlike Fedlex, ZH-Lex does **not** implement ELI-conformant URIs. The stable links are query-string based, not path-based.

### 2.2 Legacy zhlex.zh.ch Link Structure

**Current version (Loseblattsammlung, LS):**
```
http://www.zhlex.zh.ch/Erlass.html?Open&Ordnr={ls_number}
```

Examples:
```
http://www.zhlex.zh.ch/Erlass.html?Open&Ordnr=101          ← KV (Kantonsverfassung)
http://www.zhlex.zh.ch/Erlass.html?Open&Ordnr=170.41       ← IDV
http://www.zhlex.zh.ch/Erlass.html?Open&Ordnr=415.11       ← UniG
http://www.zhlex.zh.ch/Erlass.html?Open&Ordnr=551.1        ← POG
```

**Specific version (versioned LS link):**
```
http://www.zhlex.zh.ch/Erlass.html?Open&Ordnr={ls_number},{erlass_date},{inkraft_date},{bandnr}
```

Parameters:
| Parameter | Description | Example |
|---|---|---|
| `Ordnr` | LS Ordnungsnummer (systematic classification number) | `170.41` |
| `{erlass_date}` | Date of enactment (DD.MM.YYYY) | `28.05.2008` |
| `{inkraft_date}` | Date entry into force (DD.MM.YYYY) | `01.10.2008` |
| `{bandnr}` | Band/volume number (3-digit zero-padded) | `108` |

Full example — IDV, specific version:
```
http://www.zhlex.zh.ch/Erlass.html?Open&Ordnr=170.41,28.05.2008,01.10.2008,108
```

### 2.3 ZH.ch Portal URL Structure

The portal page URL encodes the same data in path segments, but is **not** intended as a stable link (the ZH.ch documentation explicitly says to use the zhlex.zh.ch links for citation purposes):

```
https://www.zh.ch/de/politik-staat/gesetze-beschluesse/gesetzessammlung/zhlex-ls/erlass-{ordnr_encoded}-{erlass_date_encoded}-{inkraft_date_encoded}-{band}.html
```

Date encoding: `DD.MM.YYYY` → `YYYY_MM_DD` with `_` separators; `.` in LS number → `_`

Example:
```
/erlass-170_41-2008_05_28-2008_10_01-108.html
         ──────  ──────────  ──────────  ───
         Ordnr   Erlassdatum  Inkraft     Band
```

### 2.4 LS Ordnungsnummer (Classification Number)

The LS Ordnungsnummer is the systematic citation number, equivalent to the SR number at federal level. Examples:

| LS Number | Law |
|---|---|
| `101` | Kantonsverfassung |
| `131.1` | Gemeindegesetz |
| `170.1` | Haftungsgesetz |
| `170.41` | IDV |
| `171.1` | Kantonsratsgesetz |
| `175.2` | VRG |
| `415.11` | Universitätsgesetz |
| `551.1` | Polizeiorganisationsgesetz |

The numbering scheme mirrors the federal SR scheme: first digits indicate the subject area (1xx = State & People, 4xx = Education, 5xx = Police & Justice, etc.).

### 2.5 ZH-Lex → AKN FRBR URI Mapping Table

| ZH-Lex element | Source system | AKN/FRBR equivalent |
|---|---|---|
| `Ordnr` parameter | zhlex query string | `{number}` in Work URI; also `<FRBRnumber>` |
| `erlass_date` (DD.MM.YYYY) | zhlex query string | `{date}` in Work URI (convert to ISO 8601) |
| `inkraft_date` (DD.MM.YYYY) | zhlex query string | `<FRBRdate name="entryIntoForce">` |
| `bandnr` (3-digit) | Version identifier | `{version}` in Expression URI (map to date) |
| Language (implicit: `de`) | No encoding — monolingual | `deu` in Expression URI |
| No format segment | Not present in zhlex links | Derived from request/content negotiation |

**Conversion decisions:**
1. `DD.MM.YYYY` → `YYYY-MM-DD` for all date fields
2. `bandnr` (e.g. `108`) is a sequential update counter, not a date — for AKN `@{version}` the actual publication/update date from the metadata record is preferred; use `band-{bandnr}` as fallback identifier
3. LS Ordnungsnummer replaces dots with underscores in portal URLs but is used as-is (with dots) in the AKN `{number}` field

---

## 3. Structural Comparison

| Dimension | Fedlex (federal) | ZH-Lex (Kanton ZH) |
|---|---|---|
| URI scheme | ELI-conformant, path-based | Query-string based, not ELI |
| Stable link type | Data URI (path) | `?Open&Ordnr=` query link |
| Version identification | Consolidation date (YYYYMMDD) | Band number (sequential integer) |
| Language encoding | 2-letter code in path | Implicit (monolingual German) |
| Format variants | html / pdf-a / xml in path | Not distinguished in URL |
| SPARQL/linked data | Full JOLux RDF graph + SPARQL | Not available |
| AKN XML publication | Since 2022-05-30 | Not published |
| Number/citation alignment | URI number ≠ SR citation number | Ordnr = LS citation number (aligned) |

---

## 4. AKN URI Design Decisions

These decisions arise directly from the reverse engineering above and are encoded in the `profile.schema.json` and resolver:

### D1: Use AKN prefix, not ELI prefix
**Rationale:** AKN `/akn/ch/…` is the authoritative namespace for Akoma Ntoso documents. Fedlex uses `/eli/…` for its own system. Our URIs are AKN documents derived from Fedlex/cantonal sources, not Fedlex URIs themselves. The profiles store a `base_uri` for linking back to the source.

### D2: Date in `YYYY-MM-DD`, not `YYYYMMDD`
**Rationale:** ISO 8601 with hyphens is the AKN standard. Fedlex uses `YYYYMMDD` (no hyphens) for consolidation dates in URIs. Conversion is mandatory.

### D3: 3-letter ISO 639-2 language codes
**Rationale:** AKN requires ISO 639-2 in FRBR URIs. Fedlex uses ISO 639-1 (2-letter). ZH-Lex encodes no language. The resolver maps 2→3 letter codes per profile.

### D4: LS/SR citation number in `{number}`, not publication sequence
**Rationale:** The Fedlex AS publication sequence number (e.g. `404` for SR 101) is an opaque identifier. For communities reading these URIs, the SR/LS citation number is the meaningful identifier. **Exception:** When producing URIs that must round-trip to Fedlex, the AS number is recorded in a separate `source_uri` field.

### D5: Band numbers (ZH-Lex) → date-based versions when possible
**Rationale:** AKN `@{version}` is designed for dates. ZH-Lex `bandnr` is a sequential counter. The parser extracts the `Publikationsdatum` from the page metadata and uses it as `@{version}`. If unavailable, `band-{bandnr}` is used as a named version.

### D6: Municipality identifier uses BFS number, not name
**Rationale:** Names change (e.g. municipal mergers); BFS numbers are stable identifiers assigned by the Federal Statistical Office. URIs should be permanent. `ch-zh-261` (BFS 261 = Zürich) is stable even if the city were renamed.

---

## 5. Source References

| Source | URL | Notes |
|---|---|---|
| Fedlex JOLux documentation | https://swiss.github.io/fedlex-jolux/introduction.html | Official ontology docs |
| Fedlex crawled JSON repo | https://github.com/droid-f/fedlex | File paths = URI paths |
| Fedlex ELI register (EUR-Lex) | https://eur-lex.europa.eu/eli-register/switzerland.html | ELI registration |
| ZH-Lex portal | https://www.zh.ch/de/politik-staat/gesetze-beschluesse/gesetzessammlung.html | Official portal |
| ZHlex legacy links | http://www.zhlex.zh.ch/Erlass.html?Open&Ordnr=… | Stable citation format |
| Fedlex SPARQL endpoint | https://fedlex.data.admin.ch/sparqlendpoint | Live RDF queries |
