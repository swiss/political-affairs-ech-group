

# Slot: group_type 


_[en] Type of group (e.g., party, committee, parliament, department)._

_[de] Art der Gruppe (z.B. Partei, Kommission, Parlament, Departement)._

__





URI: [act:groupType](https://ch.paf.link/schema/actors/groupType)
Alias: group_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Group](Group.md) | [en] A political group, organization, or body (e |  no  |






## Properties

* Range: [GroupTypeEnum](GroupTypeEnum.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:groupType |
| native | act:group_type |




## LinkML Source

<details>
```yaml
name: group_type
description: '[en] Type of group (e.g., party, committee, parliament, department).

  [de] Art der Gruppe (z.B. Partei, Kommission, Parlament, Departement).

  '
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: act:groupType
alias: group_type
domain_of:
- Group
range: GroupTypeEnum
required: true

```
</details>