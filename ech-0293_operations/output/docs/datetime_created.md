

# Slot: datetime_created 


_The time this record was created_





URI: [ops:datetime_created](https://ch.paf.link/schema/operations/datetime_created)
Alias: datetime_created

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |
| [IndividualAttendance](IndividualAttendance.md) | [en] Individual attendance record for a specific person |  no  |
| [AgendaItem](AgendaItem.md) | [en] An agenda item of a meeting |  no  |
| [Legislature](Legislature.md) | [en] Term of office of a parliament as a legislative assembly |  no  |
| [Attendance](Attendance.md) | [en] Attendance record for a meeting or voting session |  no  |
| [Speech](Speech.md) | [en] A speech or statement made during a meeting (also called Votum or speake... |  no  |
| [IndividualVote](IndividualVote.md) | [en] An individual vote cast by a member during a voting procedure |  no  |
| [Session](Session.md) | [en] A parliamentary session that groups multiple meetings and spans a specif... |  no  |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |






## Properties

* Range: [Datetime](Datetime.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:datetime_created |
| native | ops:datetime_created |




## LinkML Source

<details>
```yaml
name: datetime_created
description: The time this record was created
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: datetime_created
domain_of:
- Legislature
- Session
- Meeting
- AgendaItem
- Voting
- IndividualVote
- Election
- Attendance
- IndividualAttendance
- Speech
range: datetime

```
</details>