

## Klasse: HasIdentification 


_Eine Mixin-Klasse, die Slots für die Identifikation einer Entität zur Verfügung stellt. Sie wird für Entitäten verwendet, die aus sich heraus identifiziert sind; deren `global_uri` ist der Identifikator und daher obligatorisch._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem.  |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität.  |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans.  |



### Mixin-Verwendung

| mixed into | description |
| --- | --- |
| [Container](Container.md) | Container für die Daten des öffentlichen Ratsbetriebs: Legislaturperioden, Se... |
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
| [TextSegment](TextSegment.md) | Ein Textsegment wie Querverweise oder Zwischentitel in Sitzungsprotokollen |
| [Motion](Motion.md) | Ein formeller Antrag, der während der Verhandlungen eingereicht wird |
| [Media](Media.md) | Mediendateien oder Dokumente (einschliesslich Protokolle in PDF/HTML/WORD ode... |





















</div>