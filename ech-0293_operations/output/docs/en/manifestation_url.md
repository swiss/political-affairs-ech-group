---
search:
  boost: 5.0
---

# Slot: manifestation_url 


_URL under which the file form can be retrieved._




<div data-search-exclude markdown="1">



URI: [meta:url](https://ch.paf.link/schema/meta/url)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Manifestation](Manifestation.md) | FRBR Manifestation: a concrete file format of an Expression, addressable via ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [Manifestation](Manifestation.md) |
| Slot URI | [meta:url](https://ch.paf.link/schema/meta/url) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: manifestation_url
annotations:
  description_de:
    tag: description_de
    value: 'URL, unter der die Dateiform abgerufen werden kann.

      '
  description_fr:
    tag: description_fr
    value: 'URL sous laquelle la forme de fichier peut être consultée.

      '
description: 'URL under which the file form can be retrieved.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:url
domain_of:
- Manifestation
range: uri

```
</details></div>