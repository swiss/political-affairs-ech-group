---
search:
  boost: 5.0
---

# Slot: parent_meeting 


_Identifier of the meeting this record belongs to. On a meeting it names the superordinate meeting; on a voting, election, speech, attendance list or protocol it names the meeting in which the record arose. Agenda items do not carry it: they are embedded in their meeting._




<div data-search-exclude markdown="1">



URI: [ops:parent_meeting](https://ch.paf.link/schema/operations/parent_meeting)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | The individual sitting of a body — the level at which agenda items are delibe... |  no  |
| [Protocol](Protocol.md) | The minutes of a meeting, recorded after the meeting and kept exactly once pe... |  no  |
| [Voting](Voting.md) | A voting on a substantive question: the subject (question), the procedure, th... |  no  |
| [Election](Election.md) | An election in which a parliamentary body appoints one or several persons to ... |  no  |
| [Attendance](Attendance.md) | Aggregated attendance record for a meeting (number of members present, absent... |  no  |
| [Speech](Speech.md) | A speech or statement made during a meeting (also called Votum or speaker seg... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Meeting](Meeting.md), [Protocol](Protocol.md), [Voting](Voting.md), [Election](Election.md), [Attendance](Attendance.md), [Speech](Speech.md) |

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
      bezeichnet er die übergeordnete Sitzung, bei Abstimmung, Wahl, Wortmeldung,
      Anwesenheitsliste oder Protokoll die Sitzung, in der der Eintrag entstanden
      ist. Traktanden führen ihn nicht: Sie sind in ihre Sitzung eingebettet.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant de la séance à laquelle cet enregistrement se rattache. Pour
      une séance, il désigne la séance supérieure ; pour un vote, une élection, une
      intervention, une liste de présence ou un procès-verbal, la séance au cours
      de laquelle l''enregistrement est né. Les points de l''ordre du jour ne le portent
      pas : ils sont imbriqués dans leur séance.

      '
description: 'Identifier of the meeting this record belongs to. On a meeting it names
  the superordinate meeting; on a voting, election, speech, attendance list or protocol
  it names the meeting in which the record arose. Agenda items do not carry it: they
  are embedded in their meeting.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
- Protocol
- Voting
- Election
- Attendance
- Speech
range: string

```
</details></div>