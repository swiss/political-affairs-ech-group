---
search:
  boost: 5.0
---

# Slot: individual_vote_type 


_[en] Type of vote cast (yes, no, abstention, no vote, etc.)._

_[de] Art der abgegebenen Stimme (Ja, Nein, Enthaltung, nicht abgestimmt, etc.)._

__



<div data-search-exclude markdown="1">



URI: [ops:individual_vote_type](https://ch.paf.link/schema/operations/individual_vote_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IndividualVote](IndividualVote.md) | [en] An individual vote cast by a member during a voting procedure |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [IndividualVoteTypeEnum](IndividualVoteTypeEnum.md) |
| Domain Of | [IndividualVote](IndividualVote.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:individual_vote_type |
| native | ops:individual_vote_type |




## LinkML Source

<details>
```yaml
name: individual_vote_type
description: '[en] Type of vote cast (yes, no, abstention, no vote, etc.).

  [de] Art der abgegebenen Stimme (Ja, Nein, Enthaltung, nicht abgestimmt, etc.).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IndividualVote
range: IndividualVoteTypeEnum

```
</details></div>