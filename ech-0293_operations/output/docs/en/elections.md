---
search:
  boost: 5.0
---

# Slot: elections 


_Collection of election records._




<div data-search-exclude markdown="1">



URI: [ops:election](https://ch.paf.link/schema/operations/election)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) | Container for the records of public council operations: legislatures, session... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Election](Election.md) |
| Domain Of | [Container](Container.md) |
| Slot URI | [ops:election](https://ch.paf.link/schema/operations/election) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: elections
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der Wahlen.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des élections.

      '
description: 'Collection of election records.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:election
domain_of:
- Container
range: Election
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>