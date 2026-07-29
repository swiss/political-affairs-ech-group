---
search:
  boost: 5.0
---

# Slot: tie_breaker 


_Indicates if a tie-breaker was used in the voting._




<div data-search-exclude markdown="1">



URI: [ops:tie_breaker](https://ch.paf.link/schema/operations/tie_breaker)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | A voting procedure with individual votes and results |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [Voting](Voting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: tie_breaker
annotations:
  description_de:
    tag: description_de
    value: 'Gibt an, ob ein Stichentscheid bei der Abstimmung verwendet wurde.

      '
  description_fr:
    tag: description_fr
    value: 'Indique si une voix prépondérante a été utilisée lors du vote.

      '
description: 'Indicates if a tie-breaker was used in the voting.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
range: boolean

```
</details></div>