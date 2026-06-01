---
search:
  boost: 5.0
---

# Slot: authorized_to_vote 


_Indicates if the person is authorized to vote._

__



<div data-search-exclude markdown="1">



URI: [act:authorizedToVote](https://ld.ech.ch/schema/0294/actors/authorizedToVote)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Membership](Membership.md) | A membership relationship between a person and a group |  no  |






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












## LinkML Source

<details>
```yaml
name: authorized_to_vote
annotations:
  description_de:
    tag: description_de
    value: 'Gibt an, ob die Person stimmberechtigt ist.

      '
description: 'Indicates if the person is authorized to vote.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:authorizedToVote
domain_of:
- Membership
range: boolean

```
</details></div>