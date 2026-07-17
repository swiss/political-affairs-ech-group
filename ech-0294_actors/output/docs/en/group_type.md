---
search:
  boost: 5.0
---

# Slot: group_type 


_Type of group (e.g., party, commission, parliament, or similar). The exact naming and description of the group is provided via `label`._

__



<div data-search-exclude markdown="1">



URI: [act:groupType](https://ld.ech.ch/schema/0294/actors/groupType)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Group](Group.md) | A political group, organization, or body (e |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GroupType](GroupType.md) |
| Domain Of | [Group](Group.md) |
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
      Die genaue Benennung und Beschreibung der Gruppierung wird über `label` gemacht.

      '
  description_fr:
    tag: description_fr
    value: 'Type de groupe (p. ex. parti, commission, parlement ou similaire). La
      désignation et la description exactes du groupe sont fournies via `label`.

      '
description: 'Type of group (e.g., party, commission, parliament, or similar). The
  exact naming and description of the group is provided via `label`.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:groupType
domain_of:
- Group
range: GroupType

```
</details></div>