

## Klasse: PersonReference 


_Leichtgewichtige Referenz auf eine Person mit den wichtigsten Identifikationsmerkmalen zum Zeitpunkt der Verknüpfung. Ermöglicht historische Korrektheit auch wenn sich die Person später ändert._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| label | 1 <br/> [String](String.md) | Obligatorischer Kurzname zur Identifikation der Person innerhalb der Organisation (z.B. mit Geburtsjahr zur Unterscheidung von Personen mit gleichem Namen).  |
| label_long | 0..1 <br/> [String](String.md) | Optionaler langer Anzeigename mit akademischen Titeln und vollständigem amtlichem Namen (z.B. "Dr. Maria Muster-Beispiel").  |
| group_label | 0..1 <br/> [String](String.md) | Name des Gremiums zum Zeitpunkt der Verknüpfung.  |
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [IndividualVote](IndividualVote.md) | [actor_id](actor_id.md) | range | [PersonReference](PersonReference.md) |
| [IndividualAttendance](IndividualAttendance.md) | [actor_id](actor_id.md) | range | [PersonReference](PersonReference.md) |
| [Speech](Speech.md) | [actor_id](actor_id.md) | range | [PersonReference](PersonReference.md) |



















</div>