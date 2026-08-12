<!-- tags: fastapi, api, akn -->
# 03-api

FastAPI wrapper exposing the AKN pipeline (resolver + URL parser + fragment builder + page fetcher) as HTTP endpoints.

## Start

```bash
cd akn-pipeline
PYTHONPATH=packages uvicorn api.main:app --reload --port 8787
```

Interactive docs: http://localhost:8787/docs  
Redoc: http://localhost:8787/redoc

---

## Endpoints

### `GET /health`
Health check. Returns `{"status": "ok", "version": "0.1.0"}`.

---

### `GET /resolve` — URL → full AKN reference

The primary endpoint for the Svelte live preview field.

**Query params:**

| Param | Type | Required | Description |
|---|---|---|---|
| `url` | string | ✓ | Fedlex or ZH-Lex URL |
| `article` | string | | Artikel number |
| `paragraph` | string | | Absatz number |
| `litera` | string | | Buchstabe |
| `number` | string | | Ziffer |
| `chapter` | string | | Kapitel (optional) |
| `section` | string | | Abschnitt (optional) |
| `short_title` | string | | Override: OR, DSG, BV |
| `sr_number` | string | | Override: SR citation number |
| `fetch` | bool | | Fetch page for title/dates (default false) |
| `lang` | string | | Citation language: de/fr/it (default de) |

**Example:**
```
GET /resolve?url=https://www.fedlex.admin.ch/eli/cc/1999/404/20210307/de
            &article=47&paragraph=2&litera=a&short_title=BV&lang=de
```

**Response (key fields):**
```json
{
  "parsed_url": { "jurisdiction": "ch", "platform": "fedlex-cc", ... },
  "document_pointer": { "short_title": "BV", "preferred_id": "BV", "akn_pointer": "bv" },
  "fragment": {
    "eid": "art_47.para_2.lit_a",
    "compact": "#a47-p2-lit-a",
    "human_de": "Art. 47 Abs. 2 lit. a",
    "human_fr": "Art. 47 Al. 2 let. a",
    "eli_path": "/art_47/para_2/lit_a"
  },
  "uris": {
    "work":               "/akn/ch/lei/1999-01-01/404",
    "expression":         "/akn/ch/lei/1999-01-01/404/deu@2021-03-07",
    "fragment_uri":       "/akn/ch/lei/1999-01-01/404/deu@2021-03-07#art_47.para_2.lit_a",
    "work_fragment_uri":  "/akn/ch/lei/1999-01-01/404#art_47.para_2.lit_a",
    "display_uri":        "bv#art_47.para_2.lit_a",
    "eli_subdivision_uri":"/akn/ch/lei/1999-01-01/404/art_47/para_2/lit_a"
  },
  "human_citation": "BV Art. 47 Abs. 2 lit. a"
}
```

---

### `POST /resolve` — same as GET but as JSON body

Identical response. Use when URLs contain special characters that need escaping.

```json
{
  "url": "https://www.fedlex.admin.ch/eli/cc/1999/404/20210307/de",
  "subdivision": { "article": "47", "paragraph": "2", "litera": "a" },
  "short_title": "BV",
  "lang": "de",
  "fetch": false
}
```

---

### `POST /fragment` — build fragment from subdivision inputs

Use when you have structured inputs but no URL (e.g. standalone citation widget).

```json
{ "subdivision": { "article": "11", "number": "3", "litera": "b" } }
```

Response:
```json
{
  "eid":      "art_11.num_3.lit_b",
  "fragment": "#art_11.num_3.lit_b",
  "compact":  "#a11-num-3-lit-b",
  "human_de": "Art. 11 Ziff. 3 lit. b",
  "human_fr": "Art. 11 ch. 3 let. b",
  "human_it": "Art. 11 n. 3 lett. b",
  "eli_path": "/art_11/num_3/lit_b"
}
```

---

### `GET /fragment/parse?q=` — parse any fragment string

Accepts all four formats:

| Input format | Example |
|---|---|
| Compact display | `#a47-p2-lit-a` |
| AKN eId | `art_47.para_2.lit_a` |
| Human DE | `Art. 47 Abs. 2 lit. a` |
| Human FR | `Art. 47 Al. 2 let. a` |

Returns the same `FragmentResponse` as `POST /fragment`.

---

### `GET /jurisdiction?q=` — resolve jurisdiction shorthand

```
GET /jurisdiction?q=ZH     → {"input":"ZH","jurisdiction":"ch-zh"}
GET /jurisdiction?q=261    → {"input":"261","jurisdiction":"ch-zh-261"}
GET /jurisdiction?q=ch     → {"input":"ch","jurisdiction":"ch"}
```

---

### `GET /parse-url?url=` — inspect URL parsing without FRBR resolution

Returns the raw parsed components: jurisdiction, doc_type, date, number, lang, version, platform, ls_number.

---

## Structure

```
akn-pipeline/
  api/
    __init__.py
    main.py             ← FastAPI app + all endpoints
    tests/
      __init__.py
      test_api.py       ← 44 tests
  packages/
    frbr_uri/           ← core library (imported by API)
```

## Running tests

```bash
cd akn-pipeline
PYTHONPATH=packages pytest api/tests/ packages/frbr_uri/tests/ -v
# 44 API + 97 unit + 44 URL parser/resolver = 185 tests
```

## Docker (future)

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn requests beautifulsoup4
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8787"]
```

Environment variable `PYTHONPATH=packages` must be set.
