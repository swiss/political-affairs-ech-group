

## Klasse: HasCreationModificationDates 


_Eine Mixin-Klasse, die Slots für die Modellierung von Erstellungs- und Änderungsdaten einer Entität zur Verfügung stellt._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| date_created | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität erstellt wurde.  |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde.  |
| date_modified | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität zuletzt geändert wurde.  |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde.  |



### Mixin-Verwendung

| mixed into | description |
| --- | --- |
| [Person](Person.md) | Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Be... |
| [Group](Group.md) | Eine politische Gruppe, Organisation oder Körperschaft (z |
| [Membership](Membership.md) | Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe, die ein... |
| [InterestLink](InterestLink.md) | Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person... |





















</div>