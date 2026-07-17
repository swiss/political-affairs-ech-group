

## Class: Attendance 


_[en] Aggregated attendance record for a meeting (number of members present, absent, excused)._

_[de] Aggregierte Anwesenheitsliste für eine Sitzung (Anzahl Anwesende, Abwesende, Entschuldigte)._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| parent_meeting | 0..1 <br/> [String](String.md) | [en] The linked meeting ID that groups the current meeting. [de] Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.  |
| datetime_begin | 0..1 <br/> [Datetime](Datetime.md) | [en] The date and time when the meeting or voting begins. [de] Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt.  |
| actor_id | 0..1 <br/> [GroupReference](GroupReference.md) | [en] Reference to the acting body/organ (lightweight snapshot at time of linking). [de] Referenz auf das handelnde Organ/Gremium (leichtgewichtiger Snapshot zum Zeitpunkt der Verknüpfung).  |
| total_count | 0..1 <br/> [Integer](Integer.md) | [en] Total number of members of the body (reference value for quorum calculations). [de] Gesamtzahl aller Mitglieder des Gremiums (Bezugsgrösse für Quorum-Berechnungen).  |
| total_present | 0..1 <br/> [Integer](Integer.md) | Total number of members present |
| total_absent | 0..1 <br/> [Integer](Integer.md) | [en] Total number of absent members. Distinction between absent/excused absent - presence is tracked on attendance list. [de] Gesamtzahl abwesender Mitglieder. Unterscheidung zwischen abwesend/entschuldigt abwesend - Anwesenheit wird auf Anwesenheitsliste verfolgt.  |
| total_excused | 0..1 <br/> [Integer](Integer.md) | Total number of excused absences |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [attendances](attendances.md) | range | [Attendance](Attendance.md) |
| [IndividualAttendance](IndividualAttendance.md) | [parent_attendance](parent_attendance.md) | range | [Attendance](Attendance.md) |



















</div>