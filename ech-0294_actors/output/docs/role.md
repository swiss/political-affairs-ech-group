

# Slot: role 


_[en] Role of the person in the membership or function._

_[de] Rolle der Person in der Mitgliedschaft oder Funktion._

__





URI: [act:role](https://ch.paf.link/schema/actors/role)
Alias: role

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Membership](Membership.md) | [en] A membership relationship between a person and a group |  no  |
| [GroupReference](GroupReference.md) | Reference to a group acting in a specific role |  no  |
| [PersonReference](PersonReference.md) | Reference to a person acting in a specific role or function |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:role |
| native | act:role |




## LinkML Source

<details>
```yaml
name: role
description: '[en] Role of the person in the membership or function.

  [de] Rolle der Person in der Mitgliedschaft oder Funktion.

  '
from_schema: https://ch.paf.link/schema/actors
rank: 1000
alias: role
domain_of:
- Membership
- PersonReference
- GroupReference
range: string

```
</details>