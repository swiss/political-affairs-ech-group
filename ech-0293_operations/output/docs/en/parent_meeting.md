---
search:
  boost: 5.0
---

# Slot: parent_meeting 


_The linked meeting ID that groups the current meeting._




<div data-search-exclude markdown="1">



URI: [ops:parent_meeting](https://ch.paf.link/schema/operations/parent_meeting)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | A general meeting class used for Sessions, Comittee Meetings, individual sess... |  no  |
| [AgendaItem](AgendaItem.md) | An agenda item of a meeting |  no  |
| [Protocol](Protocol.md) | The minutes of a meeting, recorded after the meeting |  no  |
| [Voting](Voting.md) | A voting procedure with individual votes and results |  no  |
| [Election](Election.md) | An election procedure for selecting persons to positions |  no  |
| [Attendance](Attendance.md) | Aggregated attendance record for a meeting (number of members present, absent... |  no  |
| [ProtocolItem](ProtocolItem.md) | An agenda item as actually recorded in the protocol |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Meeting](Meeting.md), [AgendaItem](AgendaItem.md), [Protocol](Protocol.md), [Voting](Voting.md), [Election](Election.md), [Attendance](Attendance.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: parent_meeting
annotations:
  description_de:
    tag: description_de
    value: 'Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant de la séance liée qui regroupe la séance courante.

      '
description: 'The linked meeting ID that groups the current meeting.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
- AgendaItem
- Protocol
- Voting
- Election
- Attendance
range: string

```
</details></div>