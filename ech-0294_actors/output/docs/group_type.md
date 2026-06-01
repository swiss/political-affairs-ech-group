---
search:
  boost: 5.0
---

# Slot: group_type 


_Link to the group type._

__



<div data-search-exclude markdown="1">



URI: [act:groupType](https://ld.ech.ch/schema/0294/actors/groupType)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Group](Group.md) | A political group, organization, or body (e |  no  |
| [GroupReference](GroupReference.md) | Lightweight reference to a group with key identification data at time of link... |  no  |






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
annotations:
  description_de:
    tag: description_de
    value: 'Klasse der Gruppierung, wie z.B. Partei, Kommission, Parlament oder ähnliches.
      Die genaue Bennenung und Beschreibung der Gruppierung wird über `name` gemacht.

      '
description: 'Link to the group type.

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