

## Klasse: HasCreationModificationDates 


_A mixin class that provides slots for modeling creation and modification dates of an entity._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created.  |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created.  |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified.  |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified.  |



### Mixin-Verwendung

| mixed into | description |
| --- | --- |
| [Person](Person.md) | Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Be... |
| [Group](Group.md) | Eine politische Gruppe, Organisation oder Körperschaft (z |
| [Membership](Membership.md) | Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe, die ein... |
| [InterestLink](InterestLink.md) | Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person... |





















</div>