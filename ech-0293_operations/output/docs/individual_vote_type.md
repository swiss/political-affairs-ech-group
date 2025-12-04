

# Slot: individual_vote_type 


_[en] Type of vote cast (yes, no, abstention, absent, etc.)._

_[de] Art der abgegebenen Stimme (ja, nein, Enthaltung, abwesend, etc.)._

__





URI: [ops:individual_vote_type](https://ch.paf.link/schema/operations/individual_vote_type)
Alias: individual_vote_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IndividualVote](IndividualVote.md) | [en] An individual vote cast by a member during a voting procedure |  no  |






## Properties

* Range: [IndividualVoteTypeEnum](IndividualVoteTypeEnum.md)




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
description: '[en] Type of vote cast (yes, no, abstention, absent, etc.).

  [de] Art der abgegebenen Stimme (ja, nein, Enthaltung, abwesend, etc.).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: individual_vote_type
domain_of:
- IndividualVote
range: individual_vote_type_enum

```
</details>