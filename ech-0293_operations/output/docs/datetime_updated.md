

# Slot: datetime_updated 


_The last time this record was updated_





URI: [ops:datetime_updated](https://ch.paf.link/schema/operations/datetime_updated)
Alias: datetime_updated

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AgendaItem](AgendaItem.md) | [en] An agenda item of a meeting |  no  |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |
| [IndividualVote](IndividualVote.md) | [en] An individual vote cast by a member during a voting procedure |  no  |
| [Speech](Speech.md) | [en] A speech or statement made during a meeting (also called Votum or speake... |  no  |
| [IndividualAttendance](IndividualAttendance.md) | [en] Individual attendance record for a specific person |  no  |
| [Session](Session.md) | [en] A parliamentary session that groups multiple meetings and spans a specif... |  no  |
| [Attendance](Attendance.md) | [en] Attendance record for a meeting or voting session |  no  |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |
| [Legislature](Legislature.md) | [en] Term of office of a parliament as a legislative assembly |  no  |






## Properties

* Range: [Datetime](Datetime.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:datetime_updated |
| native | ops:datetime_updated |




## LinkML Source

<details>
```yaml
name: datetime_updated
description: The last time this record was updated
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: datetime_updated
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