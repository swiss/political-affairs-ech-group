

## Class: IndividualAttendance 


_Individual attendance record for a specific person at a meeting (linked via the parent Attendance aggregate)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| parent_attendance | 0..1 <br/> [Attendance](Attendance.md) | The Attendance aggregate this individual attendance record belongs to.  |
| actor_id | 0..1 <br/> [PersonReference](PersonReference.md) | Reference to the acting person (lightweight snapshot at time of linking).  |
| attendance_type | 0..1 <br/> [AttendanceTypeEnum](AttendanceTypeEnum.md) | Type of individual attendance.  |
| reason | * <br/> [MultilingualString](MultilingualString.md) | Reason for absence or lateness (free-text, multilingual).  |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [individual_attendances](individual_attendances.md) | range | [IndividualAttendance](IndividualAttendance.md) |



















</div>