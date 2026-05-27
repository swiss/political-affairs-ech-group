---
search:
  boost: 5.0
---

# Slot: local_id 


_[de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem._

_[en] Local identifier. For example, a UUID from the council information system._

__



<div data-search-exclude markdown="1">



URI: [mcm:localId](https://ld.ech.ch/schema/0292/meta-common/localId)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HasIdentification](HasIdentification.md) | [de] Eine Mixin-Klasse, die Slots für die Identifikation einer Entität zur Ve... |  no  |
| [Container](Container.md) |  |  no  |
| [Legislature](Legislature.md) | [en] Term of office of a parliament as a legislative assembly |  no  |
| [Session](Session.md) | [en] A parliamentary session that groups multiple meetings and spans a specif... |  no  |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |
| [AgendaItem](AgendaItem.md) | [en] An agenda item of a meeting |  no  |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |
| [IndividualVote](IndividualVote.md) | [en] An individual vote cast by a member during a voting procedure |  no  |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |
| [Attendance](Attendance.md) | [en] Aggregated attendance record for a meeting (number of members present, a... |  no  |
| [IndividualAttendance](IndividualAttendance.md) | [en] Individual attendance record for a specific person at a meeting (linked ... |  no  |
| [Speech](Speech.md) | [en] A speech or statement made during a meeting (also called Votum or speake... |  no  |
| [TextSegment](TextSegment.md) | [en] A text segment such as cross-references or subtitles in meeting protocol... |  no  |
| [Motion](Motion.md) | [en] A formal proposal or motion submitted during proceedings |  no  |
| [Media](Media.md) | [en] Media files or documents (including protocols in PDF/HTML/WORD or links ... |  no  |
| [IsProcessStep](IsProcessStep.md) | [de] Eine Mixin-Klasse für einen einzelnen Schritt in einem |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [HasIdentification](HasIdentification.md) |
| Slot URI | [mcm:localId](https://ld.ech.ch/schema/0292/meta-common/localId) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:localId |
| native | ops:local_id |




## LinkML Source

<details>
```yaml
name: local_id
description: '[de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem.

  [en] Local identifier. For example, a UUID from the council information system.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:localId
domain_of:
- HasIdentification
range: string

```
</details></div>