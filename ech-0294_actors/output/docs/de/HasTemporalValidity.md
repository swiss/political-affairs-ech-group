

## Klasse: HasTemporalValidity 


_A mixin class that provides slots for modeling a temporal validity of information (not of an event)._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
| ---  | --- | --- |
| valid_from | 0..1 <br/> [Date](Date.md) | The date from which the information is valid.  |
| valid_through | 0..1 <br/> [Date](Date.md) | The date until which the information is valid, inclusive.  |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Indicates whether the information is currently valid. Can be useful when this information is explicitly available.  |



### Mixin-Verwendung

| mixed into | description |
| --- | --- |
| [Group](Group.md) | Eine politische Gruppe, Organisation oder Körperschaft (z |
| [Membership](Membership.md) | Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe, die ein... |
| [InterestLink](InterestLink.md) | Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person... |
| [Name](Name.md) | Ein Name mit einem Typ (z |
| [Citizenship](Citizenship.md) | Staatsangehörigkeit (wird auch für Nationalität verwendet) einer Person unter... |
| [Gender](Gender.md) | Geschlecht einer Person mit Angabe eines Geschlechtscodes und der zeitlichen ... |
| [Occupation](Occupation.md) | Beruf oder Tätigkeit einer Person mit Angabe eines Labels, eines ISCO-19 Code... |
| [Training](Training.md) | Ausbildung oder Bildung einer Person mit Angabe eines Typs (z |
| [ElectoralDistrict](ElectoralDistrict.md) | Wahlkreis oder Wahlregion, in der eine Person politisch aktiv ist; mit zeitli... |





















</div>