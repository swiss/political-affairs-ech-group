

## Class: HasTemporalValidity 


_[de] Eine Mixin-Klasse, die Slots für die Modellierung einer zeitlichen Gültigkeit einer Information (nicht eines Events) zur Verfügung stellt._

_[en] A mixin class that provides slots for modeling a temporal validity of information (not of an event)._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| valid_from | 0..1 <br/> [Date](Date.md) | [de] Das Datum, ab dem die Information gültig ist. [en] The date from which the information is valid.  |
| valid_through | 0..1 <br/> [Date](Date.md) | [de] Das Datum, bis und mit dem die Information gültig ist. [en] The date until which the information is valid, inclusive.  |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist. [en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available.  |



### Mixin Usage

| mixed into | description |
| --- | --- |
| [Group](Group.md) | [de] Eine politische Gruppe, Organisation oder Körperschaft (z |
| [Membership](Membership.md) | [de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe |
| [InterestLink](InterestLink.md) | [de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer P... |
| [Name](Name.md) | [de] Ein Name mit einem Typ (z |
| [Citizenship](Citizenship.md) | [de] Staatsangehörigkeit einer Person unter Angabe des Landes und der zeitlic... |
| [Gender](Gender.md) | [de] Geschlecht einer Person mit Angabe eines Geschlechtscodes und der zeitli... |
| [Occupation](Occupation.md) | [de] Beruf oder Tätigkeit einer Person mit Angabe eines Labels, eines ISCO-19... |
| [Training](Training.md) | [de] Ausbildung oder Bildung einer Person mit Angabe eines Typs (z |
| [ElectoralDistrict](ElectoralDistrict.md) | [de] Wahlkreis oder Wahlregion, in der eine Person politisch aktiv ist; mit z... |





















</div>