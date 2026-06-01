---
search:
  boost: 5.0
---

# Slot: spatial 


_Spatial reference (fos-municipality number, fos-canton number, or country). Formats: municipality: ld.admin.ch/municipality/1234, canton: ld.admin.ch/canton/23, country: ld.admin.ch/country/CHE._

__



<div data-search-exclude markdown="1">



URI: [act:spatial](https://ld.ech.ch/schema/0294/actors/spatial)
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

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: spatial
annotations:
  description_de:
    tag: description_de
    value: 'Räumliche Referenz (BFS-Gemeindenummer, BFS-Kantonsnummer oder Land).
      Formate: Gemeinde: ld.admin.ch/municipality/1234, Kanton: ld.admin.ch/canton/23,
      Bund: ld.admin.ch/country/CHE.

      '
description: 'Spatial reference (fos-municipality number, fos-canton number, or country).
  Formats: municipality: ld.admin.ch/municipality/1234, canton: ld.admin.ch/canton/23,
  country: ld.admin.ch/country/CHE.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
domain_of:
- Group
range: string

```
</details></div>