<!-- tags: akn, eli-ch, frbr -->
# 04-architecture-and-standards

Complete reference for the AKN-CH pipeline: FRBR, ELI-CH, AKN-CH, fragment identifiers, ranges, and the Svelte/ProseMirror frontend architecture.

---

## 1. FRBR — Functional Requirements for Bibliographic Records

FRBR is a conceptual model that distinguishes four levels of identity for any intellectual creation.

| Level | Question | Swiss legal example |
|---|---|---|
| **Work** | What is it? (abstract, version-independent) | The Bundesverfassung as an idea |
| **Expression** | Which version, in which language? | BV in German, as of 2021-03-07 |
| **Manifestation** | In which format? | The XML file, the PDF, the HTML |
| **Item** | Which physical/digital copy? | The specific XML served by Fedlex |

### Why this matters for citation

A reference to "BV Art. 47" is Work-level — it is stable across all versions and languages. A reference to "BV Art. 47 in the German version as of 2021-03-07 in XML format" is Manifestation-level. Legal citation is almost always Work-level or Expression-level; archival and canonical reference systems use Manifestation-level.

### AKN URI structure (AKN-CH profile)

```
Work:          /akn/{jid}/{doctype}/{date}/{number}
Expression:    /akn/{jid}/{doctype}/{date}/{number}/{lang3}@{version}
Manifestation: /akn/{jid}/{doctype}/{date}/{number}/{lang3}@{version}.{format}
Item:          /akn/{jid}/{doctype}/{date}/{number}/{lang3}@{version}.{format}/main
```

**Components:**

| Component | Values | Notes |
|---|---|---|
| `jid` | `ch`, `ch-zh`, `ch-zh-261` | ISO 3166-2:CH + optional BFS |
| `doctype` | `lei` (Gesetz), `ord` (Verordnung), `dec` (Beschluss), `cons` (Verfassung) | AKN document type codes |
| `date` | `YYYY-MM-DD` | Erlassdatum (enactment date) |
| `number` | SR number, LS number, or AS sequence | See identifier priority chain |
| `lang3` | `deu`, `fra`, `ita`, `roh`, `eng` | ISO 639-2/B |
| `version` | `YYYY-MM-DD` | Inkraftsetzungsdatum of this expression |
| `format` | `xml`, `pdf`, `html` | Manifestation format |

**Examples:**
```
Work:      /akn/ch/lei/1907-01-01/220                     ← OR (SR 220)
Expr DE:   /akn/ch/lei/1907-01-01/220/deu@2022-01-01
Expr FR:   /akn/ch/lei/1907-01-01/220/fra@2022-01-01
Manifest:  /akn/ch/lei/1907-01-01/220/deu@2022-01-01.xml

Work:      /akn/ch-zh/lei/2008-05-28/170-41              ← ZH RRG (LS 170.41)
Expr:      /akn/ch-zh/lei/2008-05-28/170-41/deu@2008-10-01

Work:      /akn/ch-zh-261/ord/2023-01-01/2023-5           ← Zürich municipal ordinance
```

---

## 2. ELI — European Legislation Identifier

ELI (Council of the EU, 2017/C 441/05) is a framework for stable, machine-readable legislation identifiers across EU member states. Switzerland participates informally.

### ELI structure

```
http://data.europa.eu/eli/{type}/{year}/{number}[/{version}]
```

Fedlex uses ELI at: `https://fedlex.data.admin.ch/eli/cc/{year}/{number}`

### ELI vs AKN

| Property | ELI | AKN |
|---|---|---|
| Scope | URI/URL identifier | Full XML vocabulary + URI |
| Subdivision URIs | Yes (ELI Subdivisions v2) | Yes (AKN eId + portion refs) |
| Language | In URL path (`/de`, `/fr`) | In URI component (`deu@`) |
| Versioning | Optional (`/{date}/oj`) | Explicit (`@{date}`) |
| Metadata | RDF/Linked Data | XML `<meta>` block |
| Swiss federal | ✓ Fedlex | ✓ AKN-CH (this project) |

### ELI-CH (proposed)

The Swiss federal government uses ELI at Fedlex. The AKN-CH profile translates ELI URIs to AKN URIs as follows:

```
ELI:    https://fedlex.data.admin.ch/eli/cc/1999/404
AKN-CH: /akn/ch/lei/1999-01-01/404

ELI:    https://fedlex.data.admin.ch/eli/cc/1999/404/20210307/de
AKN-CH: /akn/ch/lei/1999-01-01/404/deu@2021-03-07
```

**Key mapping rules:**
- ELI `{year}/{number}` → AKN `{date}/{number}` (date = enactment date, fetched from metadata if not in URL)
- ELI language code `de` → AKN `deu` (ISO 639-1 → ISO 639-2)
- ELI version `YYYYMMDD` → AKN `@YYYY-MM-DD`
- ELI `AS number` (sequential, not SR citation) → AKN number field (Design Decision D4 from `02-url-reverse-engineering.md`)

### ELI Subdivision URIs

ELI Subdivisions v2 (EUR-Lex, 2019) defines slash-separated subdivision paths:
```
http://data.europa.eu/eli/reg/yyyy/nnnn/art_2/unp_1
```

AKN-CH equivalent:
```
/akn/ch/lei/1907-01-01/220/art_11/para_3/lit_b
```

This is the **slash routing** mode (`F13`): each subdivision is treated as a REST resource. See Section 5 for when to use `#` vs `/`.

---

## 3. Swiss Legal Structure — Document Types and Hierarchy

### Federal (Bund)

| Type | DE | FR | IT | AKN doctype | SR prefix |
|---|---|---|---|---|---|
| Bundesverfassung | BV | Cst. | Cost. | `cons` | 101 |
| Bundesgesetz | — | — | — | `lei` | varies |
| Bundesbeschluss | BB | AF | — | `dec` | varies |
| Verordnung des Bundesrats | — | — | — | `ord` | varies |
| Staatsvertrag | — | — | — | `tre` | varies |

### Cantonal (Kanton)

Same structure but scoped by `ch-{canton}`. ZH-Lex uses LS (Loseblatt-Sammlung) numbers instead of SR numbers.

### Municipal (Gemeinde)

Scoped by `ch-{canton}-{bfs}`. No systematic citation numbers — only year + sequential from the municipal gazette.

### Swiss legal citation hierarchy

```
Kapitel (chp)        — optional structural grouping
  Abschnitt (sec)    — optional structural grouping
    Unterabschnitt   — rare
      Artikel (art)  ← mandatory anchor for citation
        Absatz (para)   — numbered Abs. 1, 2, 3
          Ziffer (num)  — numbered list: 1, 2, 3
          Buchstabe (lit) — lettered list: a, b, c
            Satz (sen)    — sentence level (rarely cited, but needed)
        Spiegelstrich (ind) — unnumbered dash list
```

---

## 4. Fragment Identifier System

### Compact display syntax

| Level | Compact prefix | Rule | Example |
|---|---|---|---|
| Kapitel | `chp` | multi-char → hyphenate value | `#chp-3` |
| Abschnitt | `s` | single-char → glue value | `#s2` |
| Artikel | `a` | single-char → glue | `#a47` |
| Absatz | `p` | single-char → glue | `#p2` |
| Ziffer | `num` | multi-char → hyphenate | `#num-3` |
| Buchstabe | `lit` | letter value → always hyphenate | `#lit-a` |
| Doppelbuchstabe | `slit` | | `#slit-aa` |
| Satz | `sen` | multi-char → hyphenate | `#sen-2` |
| Anhang | `anx` | multi-char → hyphenate | `#anx-2` |

**Level separator in standalone refs:** `-`  →  `#a47-p2-lit-a`  
**Level separator in range endpoints:** `_`  →  `#a7_p2~a8_p2`  (F17)

### Canonical AKN eId

Dot-separated, hierarchical: `art_47.para_2.lit_a`

### Three URI forms for subdivisions

| Form | Syntax | Use |
|---|---|---|
| **Hash fragment** | `expression#art_47.para_2.lit_a` | Browser anchor, in-document navigation |
| **Slash path** | `expression/art_47/para_2/lit_a` | REST resource, ELI-style GET endpoint |
| **AKN portion** | `expression~art_7->art_18` | Contiguous range, fetch as AKN Portion doc |

Use **hash** when navigating to a location within a retrieved document (ProseMirror link, ToC link).  
Use **slash** when fetching a subdivision as an independent resource (API, caching, citation).  
Use **portion** when requesting a range for display or export.

---

## 5. Range and Multi-Selection Syntax

### Single reference
```
#a47-p2-lit-a         ← canonical compact
Art. 47 Abs. 2 lit. a ← human (parseable)
art_47.para_2.lit_a   ← AKN eId
```

### Contiguous range (F14-F17)
```
#a7~a18               ← Articles 7 to 18
#a7_p2~a8_p2          ← Art. 7 Abs. 2 through Art. 8 Abs. 2
#a7_lit-a~a28_sen-1   ← Art. 7 lit. a through Art. 28 Satz 1
```

Range endpoints use `_` as level separator (not `-`) to avoid ambiguity with the prefix-value hyphen.

AKN URI: `expression~art_7->art_18`  (AKN portion reference syntax)

### Discrete multi-selection (F15)
```
#a7,a11,a28           ← Articles 7, 11, and 28 (non-contiguous)
#a7_p2,a11_lit-a      ← Art. 7 Abs. 2 and Art. 11 lit. a
```

No single AKN URI exists for disjoint selections — the API returns a list.

---

## 6. Jurisdiction Shorthand

| Input | Resolves to | Notes |
|---|---|---|
| *(empty)* | `ch` | Federal default (F10) |
| `ch` | `ch` | |
| `ZH` | `ch-zh` | ISO 3166-2:CH |
| `261` | `ch-zh-261` | BFS number |
| `ch-zh-261` | `ch-zh-261` | Passthrough |

---

## 7. Document Pointer Priority Chain (F8)

```
1. Official short title    OR, DSG, ZGB, BV, AHV
2. SR / LS number          SR 220, SR 235.1, LS 170.41
3. AS / OS number          AS 2022/491 (year/sequence)
4. Composed fallback       ch-zh-261/2023/5
```

The `display_uri` in the API combines the pointer with the compact fragment:
```
bv#a47-p2-lit-a
sr-220#a11-p3
ch-zh-261-as-2023-5#a3
```

---

## 8. Svelte Frontend Architecture

### State model

```
┌─────────────────────────────────────────────────────────┐
│                    Svelte stores                        │
│                                                         │
│  documentStore   ← URL, resolved FRBR URIs,            │
│                     document pointer, metadata          │
│                                                         │
│  selectionStore  ← current PM selection →              │
│                     SelectionState (compact, human,     │
│                     hash_uri, slash_uri)                │
│                                                         │
│  operationsLog   ← list of backend operations          │
│                     (with timestamps, inputs, outputs)  │
│                                                         │
│  editorStore     ← ProseMirror state, CodeMirror state  │
└─────────────────────────────────────────────────────────┘
```

### Component layout

```
App
├── ToolBar                  URL input, language toggle, fetch button
│
├── LeftPanel  (ProseMirror)
│   ├── DocumentView         Renders the legal text
│   │   ├── ArticleNode      Clickable, marks selection
│   │   ├── ParagraphNode    Sub-selectable
│   │   └── LinkMark         Underlines cross-references to other articles
│   └── SelectionBar         Shows current_url field, updates on PM selection
│
├── RightPanel (CodeMirror)
│   ├── SourceView           Raw AKN XML with syntax highlighting
│   └── AnnotationPanel      Active marks / decorations
│
├── ReferenceBar             Persistent bottom bar:
│   ├── CompactField         Editable: #a47-p2-lit-a (live parse)
│   ├── HumanLabel           "Art. 47 Abs. 2 lit. a"
│   ├── URIField             Full fragment URI (copyable)
│   └── ModeToggle           hash / slash / portion
│
└── OperationsLog            Collapsible: backend ops with status
```

### Svelte state management for ProseMirror + CodeMirror

**Key principle:** ProseMirror and CodeMirror are both imperative editors with their own internal state. Svelte stores act as the bridge — they hold the *serialised* representation, not the editor instances themselves.

```javascript
// stores.js

import { writable, derived } from 'svelte/store';

// --- Document store ---
export const documentUrl   = writable('');
export const resolvedRef   = writable(null);   // LegalReference from API
export const fetchedMeta   = writable(null);   // FetchedMetadata

// --- Selection store ---
// Updated by ProseMirror plugin on every selectionchange
export const selectionRaw  = writable('');     // '#a47-p2-lit-a' or ''
export const selectionState = writable(null);  // SelectionState from API

// Derived: the "current URL" field shown in the UI
export const currentDisplayUri = derived(
  [resolvedRef, selectionState],
  ([$ref, $sel]) => {
    if (!$ref) return '';
    if ($sel?.compact_display) {
      const ptr = $ref.document_pointer?.akn_pointer ?? '';
      return `${ptr}${$sel.compact_display}`;
    }
    return $ref.uris?.display_uri ?? '';
  }
);

// --- Operations log ---
export const operations = writable([]);

export function logOp(op) {
  operations.update(ops => [{
    id: crypto.randomUUID(),
    ts: new Date().toISOString(),
    ...op,
  }, ...ops].slice(0, 100));
}

// --- Editor store (serialised only, not editor instances) ---
export const aknXmlSource  = writable('');    // CodeMirror content
export const docJson        = writable(null); // ProseMirror doc JSON
```

**ProseMirror → store bridge (plugin):**

```javascript
// pm-selection-plugin.js
import { Plugin } from 'prosemirror-state';
import { selectionRaw } from './stores.js';

export const selectionPlugin = new Plugin({
  view(editorView) {
    return {
      update(view, prevState) {
        if (view.state.selection === prevState.selection) return;
        const { from, to } = view.state.selection;
        if (from === to) {
          // Cursor: find enclosing article/paragraph node
          const compact = resolvePositionToCompact(view.state, from);
          selectionRaw.set(compact);
        } else {
          // Range selection: build range ref
          const startCompact = resolvePositionToCompact(view.state, from);
          const endCompact   = resolvePositionToCompact(view.state, to);
          if (startCompact && endCompact && startCompact !== endCompact) {
            selectionRaw.set(`${startCompact}~${endCompact}`);
          } else {
            selectionRaw.set(startCompact);
          }
        }
      }
    };
  }
});
```

**Store → API call (reactive):**

```javascript
// In the top-level component or a dedicated watcher
import { selectionRaw, selectionState, resolvedRef, logOp } from './stores.js';

let debounceTimer;
selectionRaw.subscribe(async (raw) => {
  if (!raw) { selectionState.set(null); return; }
  clearTimeout(debounceTimer);
  debounceTimer = setTimeout(async () => {
    const $ref = get(resolvedRef);
    const res = await fetch('/selection', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        raw,
        base_expression_uri: $ref?.uris?.expression ?? '',
        document_pointer: $ref?.document_pointer?.preferred_id ?? '',
      }),
    });
    const data = await res.json();
    selectionState.set(data);
    logOp({
      type: 'selection',
      input: raw,
      output: data.compact_display,
      status: data.errors.length ? 'error' : 'ok',
    });
  }, 80);   // debounce 80ms — fast enough for smooth live update
});
```

### ProseMirror schema for legal text

```javascript
// schema.js
import { Schema } from 'prosemirror-model';

export const legalSchema = new Schema({
  nodes: {
    doc:         { content: 'block+' },
    chapter:     { attrs: { n: {} }, content: 'section+|article+', group: 'block' },
    section:     { attrs: { n: {} }, content: 'article+', group: 'block' },
    article:     { attrs: { n: {}, eId: {} }, content: 'paragraph+', group: 'block' },
    paragraph:   { attrs: { n: {}, eId: {} }, content: 'inline*', group: 'block' },
    number_item: { attrs: { n: {}, eId: {} }, content: 'inline*', group: 'block' },
    litera_item: { attrs: { n: {}, eId: {} }, content: 'inline*', group: 'block' },
    sentence:    { attrs: { n: {}, eId: {} }, content: 'inline*', group: 'block' },
    text:        { group: 'inline' },
  },
  marks: {
    // Cross-reference link: underlines text pointing to an article/paragraph
    ref: {
      attrs: { href: {}, compact: {}, human: {} },
      inclusive: false,
      toDOM: node => ['a', {
        'href': node.attrs.href,
        'data-compact': node.attrs.compact,
        'data-human': node.attrs.human,
        'class': 'akn-ref',
        'title': node.attrs.human,
      }, 0],
      parseDOM: [{ tag: 'a[data-compact]', getAttrs: dom => ({
        href: dom.getAttribute('href'),
        compact: dom.getAttribute('data-compact'),
        human: dom.getAttribute('data-human'),
      })}],
    },
    highlight: { toDOM: () => ['mark', 0], parseDOM: [{ tag: 'mark' }] },
    underline:  { toDOM: () => ['u', 0],    parseDOM: [{ tag: 'u' }] },
  }
});
```

### CodeMirror (right panel) — AKN XML syntax highlighting

```javascript
import { EditorView, basicSetup } from 'codemirror';
import { xml } from '@codemirror/lang-xml';
import { aknXmlSource, logOp } from './stores.js';

// AKN-specific token highlighting via custom extension
const aknHighlight = /* custom lezer grammar or highlight override */;

const cmView = new EditorView({
  extensions: [
    basicSetup,
    xml(),
    EditorView.updateListener.of(update => {
      if (update.docChanged) {
        aknXmlSource.set(update.state.doc.toString());
        logOp({ type: 'edit', status: 'ok', input: 'xml-change' });
      }
    }),
  ],
  parent: document.getElementById('cm-container'),
});

// Sync from store → CM (when document loads)
aknXmlSource.subscribe(src => {
  if (cmView.state.doc.toString() !== src) {
    cmView.dispatch({
      changes: { from: 0, to: cmView.state.doc.length, insert: src }
    });
  }
});
```

### Operations log

The operations log shows what the backend does in real time — essential for understanding what's happening when generating documents from annotated legal text.

```svelte
<!-- OperationsLog.svelte -->
<script>
  import { operations } from './stores.js';
</script>

<aside class="ops-log">
  {#each $operations as op (op.id)}
    <div class="op op--{op.status}">
      <span class="op__ts">{op.ts.slice(11,19)}</span>
      <span class="op__type">{op.type}</span>
      <span class="op__detail">{op.input} → {op.output ?? ''}</span>
    </div>
  {/each}
</aside>
```

Operations to log:
- `url-resolve` — URL pasted, API call made, FRBRUris returned
- `selection` — PM selection changed, `/selection` API called
- `fragment-parse` — manual entry in compact field
- `fetch-metadata` — page fetcher called, metadata returned
- `annotation` — user annotates a span in PM as a cross-reference
- `xml-export` — AKN XML generated from annotated PM doc
- `xml-edit` — CodeMirror source edited

---

## 9. File Structure

```
akn-pipeline/
│
├── api/
│   ├── main.py              ← FastAPI: /resolve, /fragment, /selection, /jurisdiction
│   └── tests/
│       └── test_api.py
│
├── packages/
│   └── frbr_uri/
│       ├── resolver.py      ← FRBRResolver: builds Work/Expression/Manifestation URIs
│       ├── fragment.py      ← FragmentRef, compact syntax, jurisdiction resolution
│       ├── ranges.py        ← RangeRef, MultiSelectionRef, SelectionState
│       ├── reference.py     ← LegalReferenceBuilder (high-level API)
│       ├── parsers/
│       │   ├── url_parser.py    ← Fedlex + ZH-Lex URL → ParsedDocumentUrl
│       │   └── page_fetcher.py  ← HTTP → FetchedMetadata
│       └── profiles/
│           ├── ch.json          ← Federal profile
│           ├── ch-zh.json       ← Zürich canton
│           └── ...
│
├── ui/                      ← Svelte frontend (next step)
│   ├── src/
│   │   ├── stores.js        ← Svelte writable/derived stores
│   │   ├── schema.js        ← ProseMirror node/mark schema
│   │   ├── pm-plugin.js     ← Selection → store bridge
│   │   ├── App.svelte
│   │   ├── ToolBar.svelte
│   │   ├── LeftPanel.svelte     ← ProseMirror
│   │   ├── RightPanel.svelte    ← CodeMirror
│   │   ├── ReferenceBar.svelte  ← compact field + human label + URI
│   │   └── OperationsLog.svelte
│   ├── package.json
│   └── vite.config.js
│
├── 01-frbr-uri-resolver.md
├── 02-url-reverse-engineering.md
├── 02-fragment-identifiers-and-jurisdiction.md
├── 03-api.md
└── 04-architecture-and-standards.md   ← this file
```

---

## 10. Open Questions

| # | Question | Current decision | Needs eCH review |
|---|---|---|---|
| Q1 | AS number format for municipal bylaws | `{jid}-as-{year}-{seq}` | Yes |
| Q2 | `num` vs `pnt` for Ziffer | `num` (matches DE/CH practice) | Yes |
| Q3 | Sentence level in AKN | `sen` prefix, `sen_{n}` eId | Yes — AKN NC doesn't specify |
| Q4 | Slash vs hash for single subdivision | Both supported; slash = REST, hash = anchor | Document as convention |
| Q5 | Short title registry | No authoritative source; use Fedlex SPARQL | Build registry JSON |
| Q6 | BFS registry integration | Static range table now; replace with official CSV | Yes |
| Q7 | Range URI for disjoint selections | No standard; return list | Accept as implementation detail |
