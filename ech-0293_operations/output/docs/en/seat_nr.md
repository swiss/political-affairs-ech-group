---
search:
  boost: 5.0
---

# Slot: seat_nr 


_The seat number of the individual vote, if applicable._




<div data-search-exclude markdown="1">



URI: [ops:seat_nr](https://ch.paf.link/schema/operations/seat_nr)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IndividualVote](IndividualVote.md) | An individual vote cast by a member during a voting procedure |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [IndividualVote](IndividualVote.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: seat_nr
annotations:
  description_de:
    tag: description_de
    value: 'Die Sitznummer der Einzelstimme, falls zutreffend.

      '
  description_fr:
    tag: description_fr
    value: 'Le numéro de siège correspondant à la voix individuelle, le cas échéant.

      '
description: 'The seat number of the individual vote, if applicable.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IndividualVote
range: string

```
</details></div>