

## Class: HasIdentification 


_A mixin class that provides slots for the identification of an entity._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system.  |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity.  |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans.  |



### Mixin Usage

| mixed into | description |
| --- | --- |
| [Container](Container.md) | Container for the records of public council operations: legislatures, session... |
| [Legislature](Legislature.md) | Term of office of a parliament as a legislative assembly |
| [Session](Session.md) | A parliamentary session that groups multiple meetings and spans a specific ti... |
| [Meeting](Meeting.md) | A general meeting class used for Sessions, Comittee Meetings, individual sess... |
| [AgendaItem](AgendaItem.md) | An agenda item of a meeting |
| [Protocol](Protocol.md) | The minutes of a meeting, recorded after the meeting |
| [Voting](Voting.md) | A voting procedure with individual votes and results |
| [IndividualVote](IndividualVote.md) | An individual vote cast by a member during a voting procedure |
| [Election](Election.md) | An election procedure for selecting persons to positions |
| [Attendance](Attendance.md) | Aggregated attendance record for a meeting (number of members present, absent... |
| [IndividualAttendance](IndividualAttendance.md) | Individual attendance record for a specific person at a meeting (linked via t... |
| [Speech](Speech.md) | A speech or statement made during a meeting (also called Votum or speaker seg... |
| [TextSegment](TextSegment.md) | A text segment such as cross-references or subtitles in meeting protocols |
| [Motion](Motion.md) | A formal proposal or motion submitted during proceedings |
| [Media](Media.md) | Media files or documents (including protocols in PDF/HTML/WORD or links to au... |
| [PersonReference](PersonReference.md) | Lightweight reference to a person with key identification data at time of lin... |
| [GroupReference](GroupReference.md) | Lightweight reference to a group with key identification data at time of link... |





















</div>