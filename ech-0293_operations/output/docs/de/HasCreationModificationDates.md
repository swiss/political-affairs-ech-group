

## Klasse: HasCreationModificationDates 


_Eine Mixin-Klasse, die Slots für die Modellierung von Erstellungs- und Änderungsdaten einer Entität zur Verfügung stellt._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| date_created | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität erstellt wurde.  |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde.  |
| date_modified | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität zuletzt geändert wurde.  |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde.  |



### Mixin-Verwendung

| mixed into | description |
| --- | --- |
| [Legislature](Legislature.md) | Amtsdauer eines Parlaments als gesetzgebender Versammlung |
| [Session](Session.md) | Eine Parlamentssession, die mehrere Sitzungen gruppiert und sich über einen b... |
| [Meeting](Meeting.md) | Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sess... |
| [AgendaItem](AgendaItem.md) | Ein Traktandum einer Sitzung |
| [Protocol](Protocol.md) | Das nach der Sitzung erstellte Protokoll |
| [Voting](Voting.md) | Ein Abstimmungsverfahren mit Einzelstimmen und Ergebnissen |
| [IndividualVote](IndividualVote.md) | Eine Einzelstimme eines Mitglieds während eines Abstimmungsverfahrens |
| [Election](Election.md) | Ein Wahlverfahren zur Wahl von Personen in Positionen |
| [Attendance](Attendance.md) | Aggregierte Anwesenheitsliste für eine Sitzung (Anzahl Anwesende, Abwesende, ... |
| [IndividualAttendance](IndividualAttendance.md) | Einzelne Anwesenheitsfeststellung einer Person an einer Sitzung (verknüpft üb... |
| [Speech](Speech.md) | Eine Wortmeldung während einer Sitzung (auch Votum oder Redebeitrag genannt) |





















</div>