

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

[Person](Person.md), [Group](Group.md), [Membership](Membership.md), [InterestLink](InterestLink.md)





















</div>