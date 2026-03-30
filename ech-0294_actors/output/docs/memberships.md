

# Slot: memberships 


_[de] Sammlung von Mitgliedschaften._

_[en] Collection of memberships._

__





URI: [act:membership](https://ld.ech.ch/schema/0294/actors/membership)
Alias: memberships

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) | [de] Container für politische Akteure, Gruppen und Beziehungen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Membership](Membership.md) |
| Domain Of | [Container](Container.md) |
| Slot URI | [act:membership](https://ld.ech.ch/schema/0294/actors/membership) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:membership |
| native | act:memberships |




## LinkML Source

<details>
```yaml
name: memberships
description: '[de] Sammlung von Mitgliedschaften.

  [en] Collection of memberships.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
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