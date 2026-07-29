---
search:
  boost: 5.0
---

# Slot: individual_vote_type 


_Type of vote cast (yes, no, abstention, no vote, etc.)._




<div data-search-exclude markdown="1">



URI: [ops:individual_vote_type](https://ch.paf.link/schema/operations/individual_vote_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IndividualVote](IndividualVote.md) | An individual vote cast by a member during a voting procedure |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [IndividualVoteTypeEnum](IndividualVoteTypeEnum.md) |
| Domain Of | [IndividualVote](IndividualVote.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| abstention |
| no |
| not_voted |





## LinkML Source

<details>
```yaml
name: individual_vote_type
annotations:
  description_de:
    tag: description_de
    value: 'Art der abgegebenen Stimme (Ja, Nein, Enthaltung, nicht abgestimmt, etc.).

      '
  description_fr:
    tag: description_fr
    value: 'Type de voix exprimée (oui, non, abstention, n''a pas voté, etc.).

      '
description: 'Type of vote cast (yes, no, abstention, no vote, etc.).

  '
examples:
- value: abstention
- value: 'no'
- value: not_voted
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IndividualVote
range: IndividualVoteTypeEnum

```
</details></div>