---
search:
  boost: 5.0
---

# Slot: majority_count 


_Number of votes required for the relevant majority threshold._




<div data-search-exclude markdown="1">



URI: [ops:majority_count](https://ch.paf.link/schema/operations/majority_count)
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
name: majority_count
annotations:
  description_de:
    tag: description_de
    value: 'Anzahl der Stimmen, die für die relevante Mehrheitsschwelle erforderlich
      sind.

      '
  description_fr:
    tag: description_fr
    value: 'Nombre de voix requis pour atteindre le seuil de majorité déterminant.

      '
description: 'Number of votes required for the relevant majority threshold.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
- Election
range: integer

```
</details></div>