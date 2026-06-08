

## Class: HasIdentification 


_A mixin class that provides slots for the identification of an entity._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system.  |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity.  |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland.  |



### Mixin Usage

| mixed into | description |
| --- | --- |
| [Container](Container.md) |  |
| [Legislature](Legislature.md) | [en] Term of office of a parliament as a legislative assembly |
| [Session](Session.md) | [en] A parliamentary session that groups multiple meetings and spans a specif... |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |
| [AgendaItem](AgendaItem.md) | [en] An agenda item of a meeting |
| [Protocol](Protocol.md) | [en] The minutes of a meeting, recorded after the meeting |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |
| [IndividualVote](IndividualVote.md) | [en] An individual vote cast by a member during a voting procedure |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |
| [Attendance](Attendance.md) | [en] Aggregated attendance record for a meeting (number of members present, a... |
| [IndividualAttendance](IndividualAttendance.md) | [en] Individual attendance record for a specific person at a meeting (linked ... |
| [Speech](Speech.md) | [en] A speech or statement made during a meeting (also called Votum or speake... |
| [TextSegment](TextSegment.md) | [en] A text segment such as cross-references or subtitles in meeting protocol... |
| [Motion](Motion.md) | [en] A formal proposal or motion submitted during proceedings |
| [Media](Media.md) | [en] Media files or documents (including protocols in PDF/HTML/WORD or links ... |
| [PersonReference](PersonReference.md) | Lightweight reference to a person with key identification data at time of lin... |
| [GroupReference](GroupReference.md) | Lightweight reference to a group with key identification data at time of link... |





















</div>