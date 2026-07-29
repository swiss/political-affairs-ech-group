

## Klasse: Manifestation 


_FRBR Manifestation: eine konkrete Dateiform einer Expression, über eine URL adressierbar._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| id | 1 <br/> [String](String.md) | Eindeutiger Identifikator des Elements.  |
| dates | * <br/> [Date](Date.md) | Datumsangaben zum Element, jeweils mit Typangabe.  |
| format | 0..1 <br/> [String](String.md) | Das Dateiformat der Manifestation (z.B. pdf, html).  |
| manifestation_url | 0..1 <br/> [Uri](Uri.md) | URL, unter der die Dateiform abgerufen werden kann.  |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Expression](Expression.md) | [manifestations](manifestations.md) | range | [Manifestation](Manifestation.md) |



















</div>