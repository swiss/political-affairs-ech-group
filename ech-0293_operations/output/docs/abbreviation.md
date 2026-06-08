---
search:
  boost: 5.0
---

# Slot: abbreviation 


_Abbreviation (can be multilingual)._

__



<div data-search-exclude markdown="1">



URI: [mcm:abbreviation](https://ld.ech.ch/schema/0292/meta-common/abbreviation)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GroupReference](GroupReference.md) | Lightweight reference to a group with key identification data at time of link... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MultilingualValue](MultilingualValue.md) |
| Domain Of | [GroupReference](GroupReference.md) |
| Slot URI | [mcm:abbreviation](https://ld.ech.ch/schema/0292/meta-common/abbreviation) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: abbreviation
annotations:
  description_de:
    tag: description_de
    value: 'Abkürzung (kann mehrsprachig sein).

      '
description: 'Abbreviation (can be multilingual).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:abbreviation
domain_of:
- GroupReference
range: MultilingualValue
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>