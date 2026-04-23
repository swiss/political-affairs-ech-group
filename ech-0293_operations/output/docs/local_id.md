

# Slot: local_id 


_[de] Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem._

_[en] Local identifier. For example, a UUID from the council information system._

__





URI: [mcm:localId](https://ld.ech.ch/schema/0292/meta-common/localId)
Alias: local_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Motion](Motion.md) | [en] A formal proposal or motion submitted during proceedings |  no  |
| [HasIdentification](HasIdentification.md) | [de] Eine Mixin-Klasse, die Slots für die Identifikation einer Entität zur Ve... |  no  |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |
| [IndividualAttendance](IndividualAttendance.md) | [en] Individual attendance record for a specific person |  no  |
| [TextSegment](TextSegment.md) | [en] A text segment such as cross-references or subtitles in meeting protocol... |  no  |
| [Media](Media.md) | [en] Media files or documents (including protocols in PDF/HTML/WORD or links ... |  no  |
| [Speech](Speech.md) | [en] A speech or statement made during a meeting (also called Votum or speake... |  no  |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |
| [IndividualVote](IndividualVote.md) | [en] An individual vote cast by a member during a voting procedure |  no  |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |
| [AgendaItem](AgendaItem.md) | [en] An agenda item of a meeting |  no  |
| [Attendance](Attendance.md) | [en] Attendance record for a meeting or voting session |  no  |
| [Session](Session.md) | [en] A parliamentary session that groups multiple meetings and spans a specif... |  no  |
| [Container](Container.md) |  |  no  |
| [Legislature](Legislature.md) | [en] Term of office of a parliament as a legislative assembly |  no  |






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
alias: local_id
domain_of:
- HasIdentification
range: string

```
</details>