

## Klasse: Name 


_Ein Name mit einem Typ (z.B. Rufname, amtlicher Name) und einem Wert und einer zeitlichen Gültigkeit._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| name_type | 1 <br/> [NameTypeEnum](NameTypeEnum.md) | Typ des Namens gemäss eCH-0011 (personNameData).  |
| value | 1 <br/> [String](String.md) | Der eigentliche Wert einer Information neben weiteren attributen wie Typ, Sprache, etc.  |
| valid_from | 0..1 <br/> [Date](Date.md) | Das Datum, ab dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | Das Datum, bis und mit dem die Information gültig ist. <br/><br/>Vererbung: [HasTemporalValidity](HasTemporalValidity.md) |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. <br/><br/>Vererbung: [HasTemporalValidity](HasTemporalValidity.md) |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [names](names.md) | range | [Name](Name.md) |



















</div>