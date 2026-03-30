

# Slot: concerned_group 


_[de] Link zu einer Gruppe, auf die sich die Zugehörigkeit bezieht._

_[en] Link to a group that the affiliation concerns._

__





URI: [act:concernedGroup](https://ld.ech.ch/schema/0294/actors/concernedGroup)
Alias: concerned_group

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Membership](Membership.md) | [de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Group](Group.md) |
| Domain Of | [Membership](Membership.md) |
| Slot URI | [act:concernedGroup](https://ld.ech.ch/schema/0294/actors/concernedGroup) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:concernedGroup |
| native | act:concerned_group |




## LinkML Source

<details>
```yaml
name: concerned_group
description: '[de] Link zu einer Gruppe, auf die sich die Zugehörigkeit bezieht.

  [en] Link to a group that the affiliation concerns.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:concernedGroup
alias: concerned_group
domain_of:
- Membership
range: Group

```
</details>