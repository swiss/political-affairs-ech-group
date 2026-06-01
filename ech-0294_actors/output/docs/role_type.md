---
search:
  boost: 5.0
---

# Slot: role_type 


_Role of the person in the membership or function._

__



<div data-search-exclude markdown="1">



URI: [act:roleType](https://ld.ech.ch/schema/0294/actors/roleType)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonReference](PersonReference.md) | Lightweight reference to a person with key identification data at time of lin... |  no  |
| [Membership](Membership.md) | A membership relationship between a person and a group |  no  |






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
annotations:
  description_de:
    tag: description_de
    value: 'Rolle der Person in der Mitgliedschaft oder Funktion.

      '
description: 'Role of the person in the membership or function.

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