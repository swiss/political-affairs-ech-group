<!-- tags: akn, frbr, resolver -->
# 01-frbr-uri-resolver

## What this is

A standalone Python package (`frbr_uri`) that resolves **Akoma Ntoso 3.0 FRBR URIs** for Swiss jurisdictions. It loads jurisdiction profiles from JSON files and builds all four FRBR levels (Work, Expression, Manifestation, Item) for any legal document.

## File layout

```
packages/
  frbr_uri/
    __init__.py            ← public API
    resolver.py            ← FRBRResolver, FRBRUris, ResolvedProfile
    profiles/
      profile.schema.json  ← JSON Schema for community profiles
      ch.json              ← Swiss federal government
      ch-zh.json           ← Kanton Zürich
      ch-zg.json           ← Kanton Zug
      ch-zh-261.json       ← Stadt Zürich  (BFS 261)
      ch-be-351.json       ← Stadt Bern    (BFS 351)
      ch-vd-5586.json      ← Ville de Lausanne (BFS 5586)
    tests/
      test_resolver.py     ← 19 passing tests (pytest)
```

## Jurisdiction ID convention

| Level       | Pattern              | Example          |
|-------------|----------------------|------------------|
| Federal     | `ch`                 | `ch`             |
| Canton      | `ch-{canton}`        | `ch-zh`, `ch-zg` |
| Municipality| `ch-{canton}-{bfs}`  | `ch-zh-261`      |

BFS numbers are from the Federal Statistical Office (OFS/BFS) municipality register.

## URI structure (FRBR levels)

```
Work:          /akn/ch-zh/gesetz/2024-01-15/LS-170.4
Expression:    /akn/ch-zh/gesetz/2024-01-15/LS-170.4/deu@2024-01-15
Manifestation: /akn/ch-zh/gesetz/2024-01-15/LS-170.4/deu@2024-01-15.xml
Item:          /akn/ch-zh/gesetz/2024-01-15/LS-170.4/deu@2024-01-15.xml/main
```

## Usage

```python
from frbr_uri.resolver import FRBRResolver

r = FRBRResolver()

# Federal act in three languages
uris = r.resolve("ch", "act", "2024-01-01", "170.4", lang="de")
uris_fr = r.resolve("ch", "act", "2024-01-01", "170.4", lang="fr")

# Canton Zürich decree
uris = r.resolve("ch-zh", "decree", "2023-09-15", "OS 2023-5")

# Ville de Lausanne (French default)
uris = r.resolve("ch-vd-5586", "decision", "2024-02-01", "2024-3")

print(uris.work)           # /akn/...
print(uris.expression)
print(uris.manifestation)
```

## Loading community profiles

Any community can drop a JSON file in any directory and pass it on init:

```python
r = FRBRResolver(extra_profile_dirs=["/path/to/my/profiles"])
uris = r.resolve("ch-zg-1702", "regulation", "2024-01-01", "2024-1")
```

The profile format is documented in `profiles/profile.schema.json`.  
Key required fields: `jurisdiction`, `level`, `name`, `country`, `akn_prefix`, `language_codes`, `default_language`, `document_types`, `uri_templates`.

## Running tests

```bash
cd packages
PYTHONPATH=. python -m pytest frbr_uri/tests/ -v
```

## Next steps

- [ ] `02-akn-builder` — XML generation from internal document model using this resolver
- [ ] `03-html-parser` — HTML → internal model (law structure detection)
- [ ] `04-api` — FastAPI wrapper exposing the resolver and builder
- [ ] `05-frontend` — Svelte UI for metadata input and element annotation
