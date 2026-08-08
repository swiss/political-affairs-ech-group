---
search:
  boost: 5.0
---

# Slot: actor_id 


_Reference to the acting person (lightweight snapshot at time of linking)._




<div data-search-exclude markdown="1">



URI: [ops:actor_id](https://ch.paf.link/schema/operations/actor_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | Term of office of a parliament as a legislative assembly |  yes  |
| [Meeting](Meeting.md) | A general meeting class used for Sessions, Comittee Meetings, individual sess... |  yes  |
| [Voting](Voting.md) | A voting procedure with individual votes and results |  yes  |
| [IndividualVote](IndividualVote.md) | An individual vote cast by a member during a voting procedure |  no  |
| [Election](Election.md) | An election procedure for selecting persons to positions |  yes  |
| [Attendance](Attendance.md) | Aggregated attendance record for a meeting (number of members present, absent... |  yes  |
| [IndividualAttendance](IndividualAttendance.md) | Individual attendance record for a specific person at a meeting (linked via t... |  no  |
| [Speech](Speech.md) | A speech or statement made during a meeting (also called Votum or speaker seg... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PersonReference](PersonReference.md) |
| Domain Of | [Legislature](Legislature.md), [Meeting](Meeting.md), [Voting](Voting.md), [IndividualVote](IndividualVote.md), [Election](Election.md), [Attendance](Attendance.md), [IndividualAttendance](IndividualAttendance.md), [Speech](Speech.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: actor_id
annotations:
  description_de:
    tag: description_de
    value: 'Referenz auf die handelnde Person (Momentaufnahme zum Zeitpunkt der Verknüpfung).

      '
  description_fr:
    tag: description_fr
    value: 'Référence à la personne agissante (instantané au moment de la mise en
      relation).

      '
description: 'Reference to the acting person (lightweight snapshot at time of linking).

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