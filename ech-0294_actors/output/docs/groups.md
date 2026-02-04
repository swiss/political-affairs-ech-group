

# Slot: groups 


_[en] Collection of groups._

_[de] Sammlung von Gruppen._

__





URI: [act:group](https://ch.paf.link/schema/actors/group)
Alias: groups

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) | [en] Root container holding all political actors, groups, and relationships |  no  |






## Properties

* Range: [Group](Group.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:group |
| native | act:groups |




## LinkML Source

<details>
```yaml
name: groups
description: '[en] Collection of groups.

  [de] Sammlung von Gruppen.

  '
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: act:group
alias: groups
domain_of:
- Container
range: Group
multivalued: true
inlined: true
inlined_as_list: true

```
</details>