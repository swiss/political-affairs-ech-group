

## Klasse: PersonReference 


_Kurzreferenz auf eine Person mit den wichtigsten Identifikationsmerkmalen zum Zeitpunkt der Verknüpfung. Ermöglicht historische Korrektheit auch wenn sich die Person später ändert. Die referenzierte Person wird über `local_id` oder `global_uri` bezeichnet; mindestens eines von beiden ist erforderlich._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| label | 1 <br/> [String](String.md) | Obligatorischer Kurzname zur Identifikation der Person innerhalb der Organisation (z.B. mit Geburtsjahr zur Unterscheidung von Personen mit gleichem Namen).  |
| label_long | 0..1 <br/> [String](String.md) | Optionaler langer Anzeigename mit akademischen Titeln und vollständigem amtlichem Namen (z.B. "Dr. Maria Muster-Beispiel").  |
| group_label | 0..1 <br/> [String](String.md) | Name des Gremiums zum Zeitpunkt der Verknüpfung.  |
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator der referenzierten Entität. Er wird innerhalb derselben Lieferung aufgelöst. <br/><br/>Vererbung: [HasReferenceIdentification](HasReferenceIdentification.md) |
| global_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Die eindeutige, global gültige URI der referenzierten Entität. Im Unterschied zu einer local_id ist sie auch über die Lieferung hinaus auflösbar. <br/><br/>Vererbung: [HasReferenceIdentification](HasReferenceIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasReferenceIdentification](HasReferenceIdentification.md) |

##### Einschränkungen


Mindestens eines der folgenden Felder muss gesetzt sein:

- [local_id](local_id.md)
- [global_uri](global_uri.md)










### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [IndividualVote](IndividualVote.md) | [actor_id](actor_id.md) | range | [PersonReference](PersonReference.md) |
| [IndividualAttendance](IndividualAttendance.md) | [actor_id](actor_id.md) | range | [PersonReference](PersonReference.md) |
| [Speech](Speech.md) | [actor_id](actor_id.md) | range | [PersonReference](PersonReference.md) |



















</div>