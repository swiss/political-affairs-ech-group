---
search:
  boost: 5.0
---

# Slot: valid_from 


_Das Datum, ab dem die Information gültig ist._

__



<div data-search-exclude markdown="1">



URI: [schema:validFrom](http://schema.org/validFrom)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [HasTemporalValidity](HasTemporalValidity.md) | Eine Mixin-Klasse, die Slots für die Modellierung einer zeitlichen Gültigkeit... |  no  |
| [Group](Group.md) | Eine politische Gruppe, Organisation oder Körperschaft (z |  no  |
| [Membership](Membership.md) | Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe, die ein... |  no  |
| [InterestLink](InterestLink.md) | Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer Person... |  no  |
| [Name](Name.md) | Ein Name mit einem Typ (z |  no  |
| [Citizenship](Citizenship.md) | Staatsangehörigkeit (wird auch für Nationalität verwendet) einer Person unter... |  no  |
| [Gender](Gender.md) | Geschlecht einer Person mit Angabe eines Geschlechtscodes und der zeitlichen ... |  no  |
| [Occupation](Occupation.md) | Beruf oder Tätigkeit einer Person mit Angabe eines Labels, eines ISCO-19 Code... |  no  |
| [Training](Training.md) | Ausbildung oder Bildung einer Person mit Angabe eines Typs (z |  no  |
| [ElectoralDistrict](ElectoralDistrict.md) | Wahlkreis oder Wahlregion, in der eine Person politisch aktiv ist; mit zeitli... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Date](Date.md) |
| Domäne von | [HasTemporalValidity](HasTemporalValidity.md) |
| Slot-URI | [schema:validFrom](http://schema.org/validFrom) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: valid_from
annotations:
  description_de:
    tag: description_de
    value: 'Das Datum, ab dem die Information gültig ist.

      '
  description_fr:
    tag: description_fr
    value: 'La date à partir de laquelle l''information est valable.

      '
description: 'Das Datum, ab dem die Information gültig ist.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: schema:validFrom
domain_of:
- HasTemporalValidity
range: date

```
</details></div>