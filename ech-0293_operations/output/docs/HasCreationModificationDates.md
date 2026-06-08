

## Class: HasCreationModificationDates 


_A mixin class that provides slots for modeling creation and modification dates of an entity._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created.  |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created.  |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified.  |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified.  |



### Mixin Usage

| mixed into | description |
| --- | --- |
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





















</div>