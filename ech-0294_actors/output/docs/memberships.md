

# Slot: memberships 


_[en] Collection of memberships._

_[de] Sammlung von Mitgliedschaften._

__





URI: [act:membership](https://ch.paf.link/schema/actors/membership)
Alias: memberships

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) | [en] Root container holding all political actors, groups, and relationships |  no  |






## Properties

* Range: [Membership](Membership.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:membership |
| native | act:memberships |




## LinkML Source

<details>
```yaml
name: memberships
description: '[en] Collection of memberships.

  [de] Sammlung von Mitgliedschaften.

  '
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: act:membership
alias: memberships
domain_of:
- Container
range: Membership
multivalued: true
inlined: true
inlined_as_list: true

```
</details>