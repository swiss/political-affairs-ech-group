---
search:
  boost: 5.0
---

# Slot: parent_meeting 


_Identifier of the meeting this record belongs to. On a meeting it names the superordinate meeting; on an agenda item, voting, election, speech or protocol it names the meeting in which the record arose._




<div data-search-exclude markdown="1">



URI: [ops:parent_meeting](https://ch.paf.link/schema/operations/parent_meeting)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | The individual sitting of a body — the level at which agenda items are delibe... |  no  |
| [IsAgendaItem](IsAgendaItem.md) | A mixin class that provides the elements of an agenda item: designation, type... |  no  |
| [Protocol](Protocol.md) | The minutes of a meeting, recorded after the meeting and kept exactly once pe... |  no  |
| [Voting](Voting.md) | A voting on a substantive question: the subject (question), the procedure, th... |  no  |
| [Election](Election.md) | An election in which a parliamentary body appoints one or several persons to ... |  no  |
| [Attendance](Attendance.md) | Aggregated attendance record for a meeting (number of members present, absent... |  no  |
| [Speech](Speech.md) | A speech or statement made during a meeting (also called Votum or speaker seg... |  no  |
| [AgendaItem](AgendaItem.md) | An agenda item of a meeting as planned beforehand |  no  |
| [ProtocolItem](ProtocolItem.md) | An agenda item as actually recorded in the protocol |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Meeting](Meeting.md), [IsAgendaItem](IsAgendaItem.md), [Protocol](Protocol.md), [Voting](Voting.md), [Election](Election.md), [Attendance](Attendance.md), [Speech](Speech.md) |

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
    value: 'Identifikator der Sitzung, zu der dieser Eintrag gehört. Bei einer Sitzung
      bezeichnet er die übergeordnete Sitzung, bei Traktandum, Abstimmung, Wahl, Wortmeldung
      oder Protokoll die Sitzung, in der der Eintrag entstanden ist.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant de la séance à laquelle cet enregistrement se rattache. Pour
      une séance, il désigne la séance supérieure ; pour un point de l''ordre du jour,
      un vote, une élection, une intervention ou un procès-verbal, la séance au cours
      de laquelle l''enregistrement est né.

      '
description: 'Identifier of the meeting this record belongs to. On a meeting it names
  the superordinate meeting; on an agenda item, voting, election, speech or protocol
  it names the meeting in which the record arose.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
- IsAgendaItem
- Protocol
- Voting
- Election
- Attendance
- Speech
range: string

```
</details></div>