---
search:
  boost: 5.0
---

# Slot: local_id 


_Local identifier. For example, a UUID from the council information system._

__



<div data-search-exclude markdown="1">



URI: [mcm:localId](https://ld.ech.ch/schema/0292/meta-common/localId)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HasIdentification](HasIdentification.md) | A mixin class that provides slots for the identification of an entity |  no  |
| [IsProcessStep](IsProcessStep.md) | A mixin class for a single step in a multi-stage process (e |  no  |
| [Container](Container.md) |  |  no  |
| [Legislature](Legislature.md) | [en] Term of office of a parliament as a legislative assembly |  no  |
| [Session](Session.md) | [en] A parliamentary session that groups multiple meetings and spans a specif... |  no  |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |
| [AgendaItem](AgendaItem.md) | [en] An agenda item of a meeting |  no  |
| [Protocol](Protocol.md) | [en] The minutes of a meeting, recorded after the meeting |  no  |
| [ProtocolItem](ProtocolItem.md) | [en] An agenda item as actually recorded in the protocol |  no  |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |
| [IndividualVote](IndividualVote.md) | [en] An individual vote cast by a member during a voting procedure |  no  |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |
| [Attendance](Attendance.md) | [en] Aggregated attendance record for a meeting (number of members present, a... |  no  |
| [IndividualAttendance](IndividualAttendance.md) | [en] Individual attendance record for a specific person at a meeting (linked ... |  no  |
| [Speech](Speech.md) | [en] A speech or statement made during a meeting (also called Votum or speake... |  no  |
| [TextSegment](TextSegment.md) | [en] A text segment such as cross-references or subtitles in meeting protocol... |  no  |
| [Motion](Motion.md) | [en] A formal proposal or motion submitted during proceedings |  no  |
| [Media](Media.md) | [en] Media files or documents (including protocols in PDF/HTML/WORD or links ... |  no  |
| [PersonReference](PersonReference.md) | Lightweight reference to a person with key identification data at time of lin... |  no  |
| [GroupReference](GroupReference.md) | Lightweight reference to a group with key identification data at time of link... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [HasIdentification](HasIdentification.md), [IsProcessStep](IsProcessStep.md) |
| Slot URI | [mcm:localId](https://ld.ech.ch/schema/0292/meta-common/localId) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: local_id
annotations:
  description_de:
    tag: description_de
    value: 'Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant local. Par exemple, un UUID issu du système d''information
      du conseil.

      '
description: 'Local identifier. For example, a UUID from the council information system.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:localId
domain_of:
- HasIdentification
- IsProcessStep
range: string

```
</details></div>