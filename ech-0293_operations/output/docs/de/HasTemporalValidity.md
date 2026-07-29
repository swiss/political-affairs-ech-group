

## Klasse: HasTemporalValidity 


_Eine Mixin-Klasse, die Slots für die Modellierung einer zeitlichen Gültigkeit einer Information (nicht eines Events) zur Verfügung stellt._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| valid_from | 0..1 <br/> [Date](Date.md) | Das Datum, ab dem die Information gültig ist.  |
| valid_through | 0..1 <br/> [Date](Date.md) | Das Datum, bis und mit dem die Information gültig ist.  |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist.  |



### Mixin-Verwendung

| mixed into | description |
| --- | --- |





















</div>