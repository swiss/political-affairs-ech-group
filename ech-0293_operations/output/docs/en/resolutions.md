---
search:
  boost: 5.0
---

# Slot: resolutions 


_Collection of resolution records._




<div data-search-exclude markdown="1">



URI: [ops:resolution](https://ch.paf.link/schema/operations/resolution)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) | Container for the records of public council operations: legislatures, session... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Resolution](Resolution.md) |
| Domain Of | [Container](Container.md) |
| Slot URI | [ops:resolution](https://ch.paf.link/schema/operations/resolution) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: resolutions
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der Resolutionen.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des décisions.

      '
description: 'Collection of resolution records.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:resolution
domain_of:
- Container
range: Resolution
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>