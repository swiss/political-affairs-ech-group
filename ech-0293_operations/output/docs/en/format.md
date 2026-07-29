---
search:
  boost: 5.0
---

# Slot: format 


_The file format of the manifestation (e.g., pdf, html)._




<div data-search-exclude markdown="1">



URI: [meta:format](https://ch.paf.link/schema/meta/format)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Manifestation](Manifestation.md) | FRBR Manifestation: a concrete file format of an Expression, addressable via ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Manifestation](Manifestation.md) |
| Slot URI | [meta:format](https://ch.paf.link/schema/meta/format) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: format
annotations:
  description_de:
    tag: description_de
    value: 'Das Dateiformat der Manifestation (z.B. pdf, html).

      '
  description_fr:
    tag: description_fr
    value: 'Le format de fichier de la manifestation (p. ex. pdf, html).

      '
description: 'The file format of the manifestation (e.g., pdf, html).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:format
domain_of:
- Manifestation
range: string

```
</details></div>