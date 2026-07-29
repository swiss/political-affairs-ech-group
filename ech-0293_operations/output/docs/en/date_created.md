---
search:
  boost: 5.0
---

# Slot: date_created 


_The date when an entity was created._




<div data-search-exclude markdown="1">



URI: [mcm:dateCreated](https://ld.ech.ch/schema/0292/meta-common/dateCreated)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HasCreationModificationDates](HasCreationModificationDates.md) | A mixin class that provides slots for modeling creation and modification date... |  no  |
| [Legislature](Legislature.md) | Term of office of a parliament as a legislative assembly |  no  |
| [Session](Session.md) | A parliamentary session that groups multiple meetings and spans a specific ti... |  no  |
| [Meeting](Meeting.md) | A general meeting class used for Sessions, Comittee Meetings, individual sess... |  no  |
| [AgendaItem](AgendaItem.md) | An agenda item of a meeting |  no  |
| [Protocol](Protocol.md) | The minutes of a meeting, recorded after the meeting |  no  |
| [ProtocolItem](ProtocolItem.md) | An agenda item as actually recorded in the protocol |  no  |
| [Voting](Voting.md) | A voting procedure with individual votes and results |  no  |
| [IndividualVote](IndividualVote.md) | An individual vote cast by a member during a voting procedure |  no  |
| [Election](Election.md) | An election procedure for selecting persons to positions |  no  |
| [Attendance](Attendance.md) | Aggregated attendance record for a meeting (number of members present, absent... |  no  |
| [IndividualAttendance](IndividualAttendance.md) | Individual attendance record for a specific person at a meeting (linked via t... |  no  |
| [Speech](Speech.md) | A speech or statement made during a meeting (also called Votum or speaker seg... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [HasCreationModificationDates](HasCreationModificationDates.md) |
| Slot URI | [mcm:dateCreated](https://ld.ech.ch/schema/0292/meta-common/dateCreated) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: date_created
annotations:
  description_de:
    tag: description_de
    value: 'Das Datum, an dem eine Entität erstellt wurde.

      '
  description_fr:
    tag: description_fr
    value: 'La date à laquelle une entité a été créée.

      '
description: 'The date when an entity was created.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:dateCreated
domain_of:
- HasCreationModificationDates
range: date

```
</details></div>