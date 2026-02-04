

# Slot: authorized_to_vote 


_[en] Indicates if the person is authorized to vote._

_[de] Gibt an, ob die Person stimmberechtigt ist._

__





URI: [act:authorizedToVote](https://ch.paf.link/schema/actors/authorizedToVote)
Alias: authorized_to_vote

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Membership](Membership.md) | [en] A membership relationship between a person and a group |  no  |






## Properties

* Range: [Boolean](Boolean.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:authorizedToVote |
| native | act:authorized_to_vote |




## LinkML Source

<details>
```yaml
name: authorized_to_vote
description: '[en] Indicates if the person is authorized to vote.

  [de] Gibt an, ob die Person stimmberechtigt ist.

  '
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: act:authorizedToVote
alias: authorized_to_vote
domain_of:
- Membership
range: boolean

```
</details>