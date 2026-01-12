

# Slot: id 



URI: [dcterm:identifier](http://purl.org/dc/terms/identifier)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AgendaItem](AgendaItem.md) | [en] An agenda item of a meeting |  no  |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |
| [Legislature](Legislature.md) | [en] Term of office of a parliament as a legislative assembly |  no  |
| [Speech](Speech.md) | [en] A speech or statement made during a meeting (also called Votum or speake... |  no  |
| [Media](Media.md) | [en] Media files or documents (including protocols in PDF/HTML/WORD or links ... |  no  |
| [Session](Session.md) | [en] A parliamentary session that groups multiple meetings and spans a specif... |  no  |
| [TextSegment](TextSegment.md) | [en] A text segment such as cross-references or subtitles in meeting protocol... |  no  |
| [Container](Container.md) |  |  no  |
| [IndividualVote](IndividualVote.md) | [en] An individual vote cast by a member during a voting procedure |  no  |
| [Motion](Motion.md) | [en] A formal proposal or motion submitted during proceedings |  no  |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |
| [Attendance](Attendance.md) | [en] Attendance record for a meeting or voting session |  no  |
| [IndividualAttendance](IndividualAttendance.md) | [en] Individual attendance record for a specific person |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterm:identifier |
| native | ops:id |




## LinkML Source

<details>
```yaml
name: id
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: dcterm:identifier
identifier: true
alias: id
domain_of:
- Container
- Legislature
- Session
- Meeting
- AgendaItem
- Voting
- IndividualVote
- Election
- Attendance
- IndividualAttendance
- Speech
- TextSegment
- Motion
- Media
range: string
required: true

```
</details>