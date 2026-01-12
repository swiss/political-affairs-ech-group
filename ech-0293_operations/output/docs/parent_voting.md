

# Slot: parent_voting 


_[en] The ID of the voting associated with the individual vote._

_[de] Die ID der Abstimmung, die mit der Einzelstimme verbunden ist._

__





URI: [ops:parentVoting](https://ch.paf.link/schema/operations/parentVoting)
Alias: parent_voting

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IndividualVote](IndividualVote.md) | [en] An individual vote cast by a member during a voting procedure |  no  |
| [IndividualAttendance](IndividualAttendance.md) | [en] Individual attendance record for a specific person |  no  |






## Properties

* Range: [Voting](Voting.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:parentVoting |
| native | ops:parent_voting |




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
alias: parent_voting
domain_of:
- IndividualVote
- IndividualAttendance
range: Voting

```
</details>