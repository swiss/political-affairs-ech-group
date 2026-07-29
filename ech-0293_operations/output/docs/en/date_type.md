---
search:
  boost: 5.0
---

# Slot: date_type 


_Meaning of the date (e.g. first publication, last revision)._




<div data-search-exclude markdown="1">



URI: [meta:dateType](https://ch.paf.link/schema/meta/dateType)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Date](Date.md) | A date with a type indication (e |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DateTypesEnum](DateTypesEnum.md) |
| Domain Of | [Date](Date.md) |
| Slot URI | [meta:dateType](https://ch.paf.link/schema/meta/dateType) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |












## LinkML Source

<details>
```yaml
name: date_type
annotations:
  description_de:
    tag: description_de
    value: 'Bedeutung des Datums (z.B. Erstpublikation, letzte Revision).

      '
  description_fr:
    tag: description_fr
    value: 'Signification de la date (p. ex. première publication, dernière révision).

      '
description: 'Meaning of the date (e.g. first publication, last revision).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:dateType
domain_of:
- Date
range: DateTypesEnum
required: true

```
</details></div>