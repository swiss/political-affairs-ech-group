---
search:
  boost: 5.0
---

# Slot: parent_voting 


_[en] The ID of the voting associated with the individual vote._

_[de] Die ID der Abstimmung, die mit der Einzelstimme verbunden ist._

__



<div data-search-exclude markdown="1">



URI: [ops:parentVoting](https://ch.paf.link/schema/operations/parentVoting)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IndividualVote](IndividualVote.md) | [en] An individual vote cast by a member during a voting procedure |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Voting](Voting.md) |
| Domain Of | [IndividualVote](IndividualVote.md) |
| Slot URI | [ops:parentVoting](https://ch.paf.link/schema/operations/parentVoting) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: parent_voting
description: '[en] The ID of the voting associated with the individual vote.

  [de] Die ID der Abstimmung, die mit der Einzelstimme verbunden ist.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:parentVoting
domain_of:
- IndividualVote
range: Voting

```
</details></div>