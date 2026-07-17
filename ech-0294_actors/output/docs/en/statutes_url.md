---
search:
  boost: 5.0
---

# Slot: statutes_url 


_URL to party statutes (PDF or webpage; optional for parties)._

__



<div data-search-exclude markdown="1">



URI: [act:statutesURL](https://ld.ech.ch/schema/0294/actors/statutesURL)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Group](Group.md) | A political group, organization, or body (e |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Group](Group.md) |
| Slot URI | [act:statutesURL](https://ld.ech.ch/schema/0294/actors/statutesURL) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: statutes_url
annotations:
  description_de:
    tag: description_de
    value: 'URL zu Parteistatuten (PDF oder Webseite; optional für Parteien).

      '
  description_fr:
    tag: description_fr
    value: 'URL vers les statuts du parti (PDF ou page web ; facultatif pour les partis).

      '
description: 'URL to party statutes (PDF or webpage; optional for parties).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:statutesURL
domain_of:
- Group
range: string

```
</details></div>