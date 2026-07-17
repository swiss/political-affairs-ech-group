---
search:
  boost: 5.0
---

# Slot: memberships 


_Collection of memberships._

__



<div data-search-exclude markdown="1">



URI: [act:membership](https://ld.ech.ch/schema/0294/actors/membership)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) | Container for political actors, groups, and relationships |  no  |






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












## LinkML Source

<details>
```yaml
name: memberships
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung von Mitgliedschaften.

      '
  description_fr:
    tag: description_fr
    value: 'Collection d''affiliations.

      '
description: 'Collection of memberships.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:membership
domain_of:
- Container
range: Membership
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>