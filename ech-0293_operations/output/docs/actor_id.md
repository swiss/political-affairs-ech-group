---
search:
  boost: 5.0
---

# Slot: actor_id 


_[en] Reference to the acting person (lightweight snapshot at time of linking)._

_[de] Referenz auf die handelnde Person (leichtgewichtiger Snapshot zum Zeitpunkt der Verknüpfung)._

__



<div data-search-exclude markdown="1">



URI: [ops:actor_id](https://ch.paf.link/schema/operations/actor_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | [en] Term of office of a parliament as a legislative assembly |  yes  |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  yes  |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  yes  |
| [IndividualVote](IndividualVote.md) | [en] An individual vote cast by a member during a voting procedure |  no  |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  yes  |
| [Attendance](Attendance.md) | [en] Aggregated attendance record for a meeting (number of members present, a... |  yes  |
| [IndividualAttendance](IndividualAttendance.md) | [en] Individual attendance record for a specific person at a meeting (linked ... |  no  |
| [Speech](Speech.md) | [en] A speech or statement made during a meeting (also called Votum or speake... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PersonReference](PersonReference.md) |
| Domain Of | [Legislature](Legislature.md), [Meeting](Meeting.md), [Voting](Voting.md), [IndividualVote](IndividualVote.md), [Election](Election.md), [Attendance](Attendance.md), [IndividualAttendance](IndividualAttendance.md), [Speech](Speech.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










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
description: '[en] Reference to the acting person (lightweight snapshot at time of
  linking).

  [de] Referenz auf die handelnde Person (leichtgewichtiger Snapshot zum Zeitpunkt
  der Verknüpfung).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Legislature
- Meeting
- Voting
- IndividualVote
- Election
- Attendance
- IndividualAttendance
- Speech
range: PersonReference
inlined: true

```
</details></div>