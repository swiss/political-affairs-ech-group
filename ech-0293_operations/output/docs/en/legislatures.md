---
search:
  boost: 5.0
---

# Slot: legislatures 


_Collection of legislature records._




<div data-search-exclude markdown="1">



URI: [ops:legislature](https://ch.paf.link/schema/operations/legislature)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) | Container for the records of public council operations: legislatures, session... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Legislature](Legislature.md) |
| Domain Of | [Container](Container.md) |
| Slot URI | [ops:legislature](https://ch.paf.link/schema/operations/legislature) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: legislatures
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der Legislaturperioden.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des législatures.

      '
description: 'Collection of legislature records.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:legislature
domain_of:
- Container
range: Legislature
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>