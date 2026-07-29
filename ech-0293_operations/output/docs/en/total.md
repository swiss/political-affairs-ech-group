---
search:
  boost: 5.0
---

# Slot: total 


_Total number of votes, excluding absent and president's vote._




<div data-search-exclude markdown="1">



URI: [ops:total](https://ch.paf.link/schema/operations/total)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | A voting procedure with individual votes and results |  no  |
| [Election](Election.md) | An election procedure for selecting persons to positions |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Voting](Voting.md), [Election](Election.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: total
annotations:
  description_de:
    tag: description_de
    value: 'Gesamtzahl der Stimmen, ohne abwesende und Präsidiumsstimmen.

      '
  description_fr:
    tag: description_fr
    value: 'Nombre total de voix, sans les absents ni la voix de la présidence.

      '
description: 'Total number of votes, excluding absent and president''s vote.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
- Election
range: integer

```
</details></div>