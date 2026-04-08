---
search:
  boost: 5.0
---

# Slot: authorized_to_vote 


_[de] Gibt an, ob die Person stimmberechtigt ist._

_[en] Indicates if the person is authorized to vote._

__



<div data-search-exclude markdown="1">



URI: [act:authorizedToVote](https://ld.ech.ch/schema/0294/actors/authorizedToVote)
Alias: authorized_to_vote

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Membership](Membership.md) | [de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [Membership](Membership.md) |
| Slot URI | [act:authorizedToVote](https://ld.ech.ch/schema/0294/actors/authorizedToVote) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:authorizedToVote |
| native | act:authorized_to_vote |




## LinkML Source

<details>
```yaml
name: authorized_to_vote
description: '[de] Gibt an, ob die Person stimmberechtigt ist.

  [en] Indicates if the person is authorized to vote.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:authorizedToVote
alias: authorized_to_vote
domain_of:
- Membership
range: boolean

```
</details></div>