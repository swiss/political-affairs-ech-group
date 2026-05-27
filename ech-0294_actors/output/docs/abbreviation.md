---
search:
  boost: 5.0
---

# Slot: abbreviation 


_[de] Abkürzung (kann mehrsprachig sein)._

_[en] Abbreviation (can be multilingual)._

__



<div data-search-exclude markdown="1">



URI: [act:abbreviation](https://ld.ech.ch/schema/0294/actors/abbreviation)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Group](Group.md) | [de] Eine politische Gruppe, Organisation oder Körperschaft (z |  no  |
| [GroupReference](GroupReference.md) | [de] Leichtgewichtige Referenz auf eine Gruppe mit den wichtigsten Identifika... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MultilingualValue](MultilingualValue.md) |
| Domain Of | [Group](Group.md), [GroupReference](GroupReference.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: abbreviation
description: '[de] Abkürzung (kann mehrsprachig sein).

  [en] Abbreviation (can be multilingual).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
domain_of:
- Group
- GroupReference
range: MultilingualValue
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>