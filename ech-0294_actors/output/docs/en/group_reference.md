---
search:
  boost: 5.0
---

# Slot: group_reference 


_Reference to a group with snapshot data at time of linking._

__



<div data-search-exclude markdown="1">



URI: [act:groupReference](https://ld.ech.ch/schema/0294/actors/groupReference)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Membership](Membership.md) | A membership relationship between a person and a group, representing formal a... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GroupReference](GroupReference.md) |
| Domain Of | [Membership](Membership.md) |
| Slot URI | [act:groupReference](https://ld.ech.ch/schema/0294/actors/groupReference) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: group_reference
annotations:
  description_de:
    tag: description_de
    value: 'Referenz auf eine Gruppe mit Snapshot-Daten zum Zeitpunkt der Verknüpfung.

      '
  description_fr:
    tag: description_fr
    value: 'Référence à un groupe avec des données instantanées au moment de la mise
      en relation.

      '
description: 'Reference to a group with snapshot data at time of linking.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:groupReference
domain_of:
- Membership
range: GroupReference
inlined: true

```
</details></div>