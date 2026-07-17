

## Klasse: Citizenship 


_Staatsangehörigkeit (wird auch für Nationalität verwendet) einer Person unter Angabe des Landes und der zeitlichen Gültigkeit. Wenn kein `valid_from` angegeben ist, ist diese Information nicht bekannt. Ist bekannt, dass die Staatsangehörigkeit seit der Geburt gültig ist, ist das Geburtsdatum hier anzugeben. Wenn kein `valid_through` angegeben ist, ist die Staatsangehörigkeit weiterhin gültig._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| country | 0..1 <br/> [String](String.md) | ISO 3166-1 alpha-2 Ländercode.  |
| valid_from | 0..1 <br/> [Date](Date.md) | Das Datum, ab dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | Das Datum, bis und mit dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](HasTemporalValidity.md) |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. <br/><br/>Vererbung: [HasTemporalValidity](HasTemporalValidity.md) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [citizenships](citizenships.md) | range | [Citizenship](Citizenship.md) |



















</div>