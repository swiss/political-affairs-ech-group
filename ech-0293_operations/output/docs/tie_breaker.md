---
search:
  boost: 5.0
---

# Slot: tie_breaker 


_[en] Indicates if a tie-breaker was used in the voting._

_[de] Gibt an, ob ein Stichentscheid bei der Abstimmung verwendet wurde._

__



<div data-search-exclude markdown="1">



URI: [ops:tie_breaker](https://ch.paf.link/schema/operations/tie_breaker)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [Voting](Voting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:tie_breaker |
| native | ops:tie_breaker |




## LinkML Source

<details>
```yaml
name: tie_breaker
description: '[en] Indicates if a tie-breaker was used in the voting.

  [de] Gibt an, ob ein Stichentscheid bei der Abstimmung verwendet wurde.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
range: boolean

```
</details></div>