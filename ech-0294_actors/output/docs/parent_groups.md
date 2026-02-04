

# Slot: parent_groups 


_[en] Parent group IDs (to model party hierarchy or bind parties to parliaments)._

_[de] Übergeordnete Gruppen-IDs (um Parteihierarchie oder Bindung an Parlamente abzubilden)._

__





URI: [act:parentGroup](https://ch.paf.link/schema/actors/parentGroup)
Alias: parent_groups

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Group](Group.md) | [en] A political group, organization, or body (e |  no  |






## Properties

* Range: [String](String.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:parentGroup |
| native | act:parent_groups |




## LinkML Source

<details>
```yaml
name: parent_groups
description: '[en] Parent group IDs (to model party hierarchy or bind parties to parliaments).

  [de] Übergeordnete Gruppen-IDs (um Parteihierarchie oder Bindung an Parlamente abzubilden).

  '
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: act:parentGroup
alias: parent_groups
domain_of:
- Group
range: string
multivalued: true
inlined: true
inlined_as_list: true

```
</details>