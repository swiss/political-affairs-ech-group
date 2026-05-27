---
search:
  boost: 5.0
---

# Slot: group_type 


_[de] Klasse der Gruppierung, wie z.B. Partei, Kommission, Parlament oder ähnliches. Die genaue Bennenung und Beschreibung der Gruppierung wird über `name` gemacht._

_[en] Link to the group type._

__



<div data-search-exclude markdown="1">



URI: [act:groupType](https://ld.ech.ch/schema/0294/actors/groupType)
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
| Range | [GroupType](GroupType.md) |
| Domain Of | [Group](Group.md), [GroupReference](GroupReference.md) |
| Slot URI | [act:groupType](https://ld.ech.ch/schema/0294/actors/groupType) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: group_type
description: '[de] Klasse der Gruppierung, wie z.B. Partei, Kommission, Parlament
  oder ähnliches. Die genaue Bennenung und Beschreibung der Gruppierung wird über
  `name` gemacht.

  [en] Link to the group type.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:groupType
domain_of:
- Group
- GroupReference
range: GroupType

```
</details></div>