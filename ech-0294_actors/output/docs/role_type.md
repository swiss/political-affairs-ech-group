---
search:
  boost: 5.0
---

# Slot: role_type 


_[en] Role of the person in the membership or function._

_[de] Rolle der Person in der Mitgliedschaft oder Funktion._

__



<div data-search-exclude markdown="1">



URI: [act:roleType](https://ld.ech.ch/schema/0294/actors/roleType)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonReference](PersonReference.md) | [de] Leichtgewichtige Referenz auf eine Person mit den wichtigsten Identifika... |  no  |
| [Membership](Membership.md) | [de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RoleType](RoleType.md) |
| Domain Of | [PersonReference](PersonReference.md), [Membership](Membership.md) |
| Slot URI | [act:roleType](https://ld.ech.ch/schema/0294/actors/roleType) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: role_type
description: '[en] Role of the person in the membership or function.

  [de] Rolle der Person in der Mitgliedschaft oder Funktion.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:roleType
domain_of:
- PersonReference
- Membership
range: RoleType

```
</details></div>