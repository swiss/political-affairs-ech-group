

## Class: Attendance 


_Aggregated attendance record for a meeting (number of members present, absent, excused): it records which members of a parliamentary body were present, absent or excused at a sitting. Attendance is captured on two levels — this aggregate with the totals for the meeting, and one IndividualAttendance per person, linked to it via parent_attendance. Attendance records serve the documentation of participation, the verification of the quorum, transparency towards the public, accountability for the fulfilment of duties, statistics on attendance rates and the administration of allowances and expenses._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| parent_meeting | 0..1 <br/> [String](String.md) | The meeting to which the attendance list belongs.  |
| datetime_begin | 0..1 <br/> [Datetime](Datetime.md) | Date and time at which attendance was recorded.  |
| group_reference | 0..1 <br/> [GroupReference](GroupReference.md) | Reference to the acting body/organ (lightweight snapshot at time of linking).  |
| total_count | 0..1 <br/> [Integer](Integer.md) | Total number of members of the body, the reference value for quorum calculations (e.g. 200 for the National Council, 46 for the Council of States). The quorum itself is not stored as a field of its own: it follows from the ratio of total_present to total_count and the quorum rules of the body, and is calculated on the data side when needed.  |
| total_present | 0..1 <br/> [Integer](Integer.md) | Number of members present, e.g. 185 of 200.  |
| total_absent | 0..1 <br/> [Integer](Integer.md) | Number of members absent without excuse, e.g. 3 of 200.  |
| total_excused | 0..1 <br/> [Integer](Integer.md) | Number of members whose absence was excused, e.g. 12 of 200.  |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](Container.md) | [attendances](attendances.md) | range | [Attendance](Attendance.md) |
| [IndividualAttendance](IndividualAttendance.md) | [parent_attendance](parent_attendance.md) | range | [Attendance](Attendance.md) |



















</div>