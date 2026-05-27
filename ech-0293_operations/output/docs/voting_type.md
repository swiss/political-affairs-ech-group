---
search:
  boost: 5.0
---

# Slot: voting_type 


_[en] Type of voting procedure (preliminary, final, secret, etc.)._

_[de] Art des Abstimmungsverfahrens (Zwischen-, Schlussabstimmung, geheim, etc.)._

__



<div data-search-exclude markdown="1">



URI: [ops:voting_type](https://ch.paf.link/schema/operations/voting_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [VotingTypeEnum](VotingTypeEnum.md) |
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
| self | ops:voting_type |
| native | ops:voting_type |




## LinkML Source

<details>
```yaml
name: voting_type
description: '[en] Type of voting procedure (preliminary, final, secret, etc.).

  [de] Art des Abstimmungsverfahrens (Zwischen-, Schlussabstimmung, geheim, etc.).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
range: VotingTypeEnum

```
</details></div>