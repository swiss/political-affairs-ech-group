

## Klasse: Attendance 


_Aggregierte Anwesenheitsliste für eine Sitzung (Anzahl Anwesende, Abwesende, Entschuldigte)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| parent_meeting | 0..1 <br/> [String](String.md) | Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.  |
| datetime_begin | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt.  |
| actor_id | 0..1 <br/> [GroupReference](GroupReference.md) | Referenz auf das handelnde Organ/Gremium (leichtgewichtiger Snapshot zum Zeitpunkt der Verknüpfung).  |
| total_count | 0..1 <br/> [Integer](Integer.md) | Gesamtzahl aller Mitglieder des Gremiums (Bezugsgrösse für Quorum-Berechnungen).  |
| total_present | 0..1 <br/> [Integer](Integer.md) | Gesamtzahl der anwesenden Mitglieder.  |
| total_absent | 0..1 <br/> [Integer](Integer.md) | Gesamtzahl abwesender Mitglieder. Unterscheidung zwischen abwesend/entschuldigt abwesend - Anwesenheit wird auf Anwesenheitsliste verfolgt.  |
| total_excused | 0..1 <br/> [Integer](Integer.md) | Gesamtzahl der entschuldigten Abwesenheiten.  |
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| date_created | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [attendances](attendances.md) | range | [Attendance](Attendance.md) |
| [IndividualAttendance](IndividualAttendance.md) | [parent_attendance](parent_attendance.md) | range | [Attendance](Attendance.md) |



















</div>