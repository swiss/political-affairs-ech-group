---
search:
  boost: 5.0
---

# Slot: total_count_no 


_Total number of 'no' votes._




<div data-search-exclude markdown="1">



URI: [ops:total_count_no](https://ch.paf.link/schema/operations/total_count_no)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | A voting procedure with individual votes and results |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Voting](Voting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: total_count_no
annotations:
  description_de:
    tag: description_de
    value: 'Gesamtzahl der „Nein“-Stimmen.

      '
  description_fr:
    tag: description_fr
    value: 'Nombre total de voix « non ».

      '
description: 'Total number of ''no'' votes.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
range: integer

```
</details></div>