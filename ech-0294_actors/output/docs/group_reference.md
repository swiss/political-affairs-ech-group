---
search:
  boost: 5.0
---

# Slot: group_reference 


_[de] Referenz auf eine Gruppe mit Snapshot-Daten zum Zeitpunkt der Verknüpfung._

_[en] Reference to a group with snapshot data at time of linking._

__



<div data-search-exclude markdown="1">



URI: [act:groupReference](https://ld.ech.ch/schema/0294/actors/groupReference)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Membership](Membership.md) | [de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe |  no  |






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
description: '[de] Referenz auf eine Gruppe mit Snapshot-Daten zum Zeitpunkt der Verknüpfung.

  [en] Reference to a group with snapshot data at time of linking.

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