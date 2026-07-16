---
search:
  boost: 5.0
---

# Slot: district 


_Electoral district or region._

__



<div data-search-exclude markdown="1">



URI: [act:district](https://ld.ech.ch/schema/0294/actors/district)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ElectoralDistrict](ElectoralDistrict.md) | Electoral district or region where a person is politically active; with tempo... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ElectoralDistrict](ElectoralDistrict.md) |
| Slot URI | [act:district](https://ld.ech.ch/schema/0294/actors/district) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| Basel-Stadt |





## LinkML Source

<details>
```yaml
name: district
annotations:
  description_de:
    tag: description_de
    value: 'Wahlkreis oder Wahlregion.

      '
description: 'Electoral district or region.

  '
examples:
- value: Basel-Stadt
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:district
domain_of:
- ElectoralDistrict
range: string

```
</details></div>