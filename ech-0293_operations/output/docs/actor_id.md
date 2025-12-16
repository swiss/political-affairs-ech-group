

# Slot: actor_id 


_[en] The political body organized by the term of office (e.g., Regierungsrat, Nationalrat, Ständerat)._

_[de] Das politische Organ, das durch die Amtsdauer organisiert wird (z.B. Regierungsrat, Nationalrat, Ständerat)._

__





URI: [ops:actor_id](https://ch.paf.link/schema/operations/actor_id)
Alias: actor_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IndividualAttendance](IndividualAttendance.md) | [en] Individual attendance record for a specific person |  no  |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |
| [Attendance](Attendance.md) | [en] Attendance record for a meeting or voting session |  no  |
| [IndividualVote](IndividualVote.md) | [en] An individual vote cast by a member during a voting procedure |  no  |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |
| [Legislature](Legislature.md) | [en] Term of office of a parliament as a legislative assembly |  no  |
| [Speech](Speech.md) | [en] A speech or statement made during a meeting (also called Votum or speake... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:actor_id |
| native | ops:actor_id |




## LinkML Source

<details>
```yaml
name: actor_id
description: '[en] The political body organized by the term of office (e.g., Regierungsrat,
  Nationalrat, Ständerat).

  [de] Das politische Organ, das durch die Amtsdauer organisiert wird (z.B. Regierungsrat,
  Nationalrat, Ständerat).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: actor_id
domain_of:
- Legislature
- Meeting
- Voting
- IndividualVote
- Election
- Attendance
- IndividualAttendance
- Speech
range: string

```
</details>