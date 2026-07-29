---
search:
  boost: 5.0
---

# Slot: weight 


_The number of votes held by the individual, if applicable (e.g., in cases where a person has multiple votes)._




<div data-search-exclude markdown="1">



URI: [ops:weight](https://ch.paf.link/schema/operations/weight)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IndividualVote](IndividualVote.md) | An individual vote cast by a member during a voting procedure |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [IndividualVote](IndividualVote.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: weight
annotations:
  description_de:
    tag: description_de
    value: 'Die Anzahl der Stimmen, die die Einzelperson hat, falls zutreffend (z.B.
      in Fällen, in denen eine Person mehrere Stimmen hat).

      '
  description_fr:
    tag: description_fr
    value: 'Le nombre de voix dont dispose la personne, le cas échéant (p. ex. lorsqu''une
      personne détient plusieurs voix).

      '
description: 'The number of votes held by the individual, if applicable (e.g., in
  cases where a person has multiple votes).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IndividualVote
range: integer

```
</details></div>