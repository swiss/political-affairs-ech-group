---
search:
  boost: 5.0
---

# Slot: datetime_created 


_The date and time when an entity was created._




<div data-search-exclude markdown="1">



URI: [mcm:datetimeCreated](https://ld.ech.ch/schema/0292/meta-common/datetimeCreated)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HasCreationModificationDates](HasCreationModificationDates.md) | A mixin class that provides slots for modeling creation and modification date... |  no  |
| [Legislature](Legislature.md) | Term of office of a parliament as a legislative assembly |  no  |
| [Session](Session.md) | A session: a contiguous period of sittings within a legislature |  no  |
| [Meeting](Meeting.md) | The individual sitting of a body — the level at which agenda items are delibe... |  no  |
| [AgendaItem](AgendaItem.md) | An agenda item of a meeting as planned beforehand |  no  |
| [Protocol](Protocol.md) | The minutes of a meeting, recorded after the meeting and kept exactly once pe... |  no  |
| [ProtocolItem](ProtocolItem.md) | An agenda item as actually recorded in the protocol |  no  |
| [Voting](Voting.md) | A voting on a substantive question: the subject (question), the procedure, th... |  no  |
| [IndividualVote](IndividualVote.md) | The vote cast by an individual member in a voting |  no  |
| [Election](Election.md) | An election in which a parliamentary body appoints one or several persons to ... |  no  |
| [Attendance](Attendance.md) | Aggregated attendance record for a meeting (number of members present, absent... |  no  |
| [IndividualAttendance](IndividualAttendance.md) | Individual attendance record for a specific person at a meeting (linked via t... |  no  |
| [Speech](Speech.md) | A speech or statement made during a meeting (also called Votum or speaker seg... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [HasCreationModificationDates](HasCreationModificationDates.md) |
| Slot URI | [mcm:datetimeCreated](https://ld.ech.ch/schema/0292/meta-common/datetimeCreated) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: datetime_created
annotations:
  description_de:
    tag: description_de
    value: 'Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde.

      '
  description_fr:
    tag: description_fr
    value: 'La date et l''heure auxquelles une entité a été créée.

      '
description: 'The date and time when an entity was created.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:datetimeCreated
domain_of:
- HasCreationModificationDates
range: datetime

```
</details></div>