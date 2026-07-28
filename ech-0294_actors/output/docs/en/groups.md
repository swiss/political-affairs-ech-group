---
search:
  boost: 5.0
---

# Slot: groups 


_Collection of groups._

__



<div data-search-exclude markdown="1">



URI: [act:group](https://ld.ech.ch/schema/0294/actors/group)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) | Container for political actors, groups, and relationships |  no  |






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












## LinkML Source

<details>
```yaml
name: groups
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung von Gruppen.

      '
  description_fr:
    tag: description_fr
    value: 'Collection de groupes.

      '
description: 'Collection of groups.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:group
domain_of:
- Container
range: Group
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>