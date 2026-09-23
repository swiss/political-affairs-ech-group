---
search:
  boost: 5.0
---

# Slot: global_uri 


_A unique, globally valid URI for the entity._




<div data-search-exclude markdown="1">



URI: [mcm:globalURI](https://ld.ech.ch/schema/0292/meta-common/globalURI)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HasIdentification](HasIdentification.md) | A mixin class that provides slots for the identification of an entity |  no  |
| [IsProcessStep](IsProcessStep.md) | A mixin class for a single step in a multi-stage process (e |  no  |
| [Container](Container.md) | Container for the records of public council operations: legislatures, session... |  no  |
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
| [TextSegment](TextSegment.md) | A text segment such as cross-references or subtitles |  no  |
| [Motion](Motion.md) | A formal proposal submitted during the proceedings, such as an amendment to a... |  no  |
| [Media](Media.md) | Media files or documents (including protocols in PDF/HTML/WORD or links to au... |  no  |
| [HasReferenceIdentification](HasReferenceIdentification.md) | A mixin class that provides the slots with which a reference names the entity... |  no  |
| [PersonReference](PersonReference.md) | Lightweight reference to a person with key identification data at time of lin... |  no  |
| [GroupReference](GroupReference.md) | Lightweight reference to a group with key identification data at time of link... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [HasIdentification](HasIdentification.md), [HasReferenceIdentification](HasReferenceIdentification.md), [IsProcessStep](IsProcessStep.md) |
| Slot URI | [mcm:globalURI](https://ld.ech.ch/schema/0292/meta-common/globalURI) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |














## LinkML Source

<details>
```yaml
name: global_uri
annotations:
  description_de:
    tag: description_de
    value: 'Eine eindeutige, global gültige URI für die Entität.

      '
  description_fr:
    tag: description_fr
    value: 'Une URI unique et globalement valide pour l''entité.

      '
description: 'A unique, globally valid URI for the entity.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:globalURI
identifier: true
domain_of:
- HasIdentification
- HasReferenceIdentification
- IsProcessStep
range: uriorcurie
required: true

```
</details></div>