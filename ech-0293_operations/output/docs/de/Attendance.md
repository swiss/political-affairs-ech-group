

## Klasse: Attendance 


_Aggregierte Anwesenheitsliste für eine Sitzung (Anzahl Anwesende, Abwesende, Entschuldigte): Sie hält fest, welche Mitglieder eines parlamentarischen Organs bei einer Sitzung anwesend, abwesend oder entschuldigt waren. Die Anwesenheit wird auf zwei Ebenen erfasst — mit diesem Aggregat und den Gesamtzahlen für die Sitzung sowie mit je einer IndividualAttendance pro Person, die über parent_attendance daran hängt. Anwesenheitslisten dienen der Dokumentation der Teilnahme, der Prüfung der Beschlussfähigkeit, der Transparenz gegenüber der Öffentlichkeit, der Rechenschaft über die Pflichterfüllung, der Statistik von Anwesenheitsquoten sowie der Administration von Entschädigungen und Spesen._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| parent_meeting | 0..1 <br/> [String](String.md) | Die Sitzung, zu der die Anwesenheitsliste gehört.  |
| datetime_begin | 0..1 <br/> [Datetime](Datetime.md) | Datum und Uhrzeit, zu der die Anwesenheit erfasst wurde.  |
| actor_id | 0..1 <br/> [GroupReference](GroupReference.md) | Referenz auf das handelnde Organ/Gremium (Momentaufnahme zum Zeitpunkt der Verknüpfung).  |
| total_count | 0..1 <br/> [Integer](Integer.md) | Gesamtzahl aller Mitglieder des Gremiums, die Bezugsgrösse für Quorum-Berechnungen (z.B. 200 für den Nationalrat, 46 für den Ständerat). Die Beschlussfähigkeit selbst wird nicht als eigenes Feld gespeichert: Sie ergibt sich aus dem Verhältnis von total_present zu total_count und den Quorum-Regeln des Gremiums und wird bei Bedarf datenseitig berechnet.  |
| total_present | 0..1 <br/> [Integer](Integer.md) | Anzahl anwesender Mitglieder, z.B. 185 von 200.  |
| total_absent | 0..1 <br/> [Integer](Integer.md) | Anzahl unentschuldigt abwesender Mitglieder, z.B. 3 von 200.  |
| total_excused | 0..1 <br/> [Integer](Integer.md) | Anzahl Mitglieder, deren Abwesenheit entschuldigt war, z.B. 12 von 200.  |
| date_created | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Container](Container.md) | [attendances](attendances.md) | range | [Attendance](Attendance.md) |
| [IndividualAttendance](IndividualAttendance.md) | [parent_attendance](parent_attendance.md) | range | [Attendance](Attendance.md) |



















</div>