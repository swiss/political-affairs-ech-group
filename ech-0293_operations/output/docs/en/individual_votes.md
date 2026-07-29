---
search:
  boost: 5.0
---

# Slot: individual_votes 


_Collection of individual vote records._




<div data-search-exclude markdown="1">



URI: [ops:individualVote](https://ch.paf.link/schema/operations/individualVote)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) | Container for the records of public council operations: legislatures, session... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [IndividualVote](IndividualVote.md) |
| Domain Of | [Container](Container.md) |
| Slot URI | [ops:individualVote](https://ch.paf.link/schema/operations/individualVote) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: individual_votes
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der Einzelstimmen.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des voix individuelles.

      '
description: 'Collection of individual vote records.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:individualVote
domain_of:
- Container
range: IndividualVote
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>