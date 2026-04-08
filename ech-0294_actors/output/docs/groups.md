---
search:
  boost: 5.0
---

# Slot: groups 


_[de] Sammlung von Gruppen._

_[en] Collection of groups._

__



<div data-search-exclude markdown="1">



URI: [act:group](https://ld.ech.ch/schema/0294/actors/group)
Alias: groups

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) | [de] Container für politische Akteure, Gruppen und Beziehungen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Group](Group.md) |
| Domain Of | [Container](Container.md) |
| Slot URI | [act:group](https://ld.ech.ch/schema/0294/actors/group) |

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
| self | act:group |
| native | act:groups |




## LinkML Source

<details>
```yaml
name: groups
description: '[de] Sammlung von Gruppen.

  [en] Collection of groups.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
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
</details></div>