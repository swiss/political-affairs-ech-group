---
search:
  boost: 10.0
---

# Class: HasTemporalValidity 


_[de] Eine Mixin-Klasse, die Slots für die Modellierung einer zeitlichen Gültigkeit einer Information (nicht eines Events) zur Verfügung stellt._

_[en] A mixin class that provides slots for modeling a temporal validity of information (not of an event)._

__



<div data-search-exclude markdown="1">



URI: [act:HasTemporalValidity](https://ld.ech.ch/schema/0294/actors/HasTemporalValidity)




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Mixin | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [valid_from](valid_from.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, ab dem die Information gültig ist | direct |
| [valid_through](valid_through.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, bis und mit dem die Information gültig ist | direct |
| [is_active](is_active.md) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Information aktuell gültig ist | direct |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [Group](Group.md) | [de] Eine politische Gruppe, Organisation oder Körperschaft (z |
| [Membership](Membership.md) | [de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe |
| [InterestLink](InterestLink.md) | [de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer P... |
| [Name](Name.md) | [de] Ein Name mit einem Typ (z |
| [Citizenship](Citizenship.md) | [de] Staatsbürgerschaft einer Person mit Angabe des Landes und der zeitlichen... |
| [Gender](Gender.md) | [de] Geschlecht einer Person mit Angabe eines Geschlechtscodes und der zeitli... |
| [Occupation](Occupation.md) | [de] Beruf oder Tätigkeit einer Person mit Angabe eines Labels, eines ISCO-19... |
| [Training](Training.md) | [de] Ausbildung oder Bildung einer Person mit Angabe eines Typs (z |
| [ElectoralDistrict](ElectoralDistrict.md) | [de] Wahlkreis oder Wahlregion, in der eine Person politisch aktiv ist; mit z... |














## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:HasTemporalValidity |
| native | act:HasTemporalValidity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HasTemporalValidity
description: '[de] Eine Mixin-Klasse, die Slots für die Modellierung einer zeitlichen
  Gültigkeit einer Information (nicht eines Events) zur Verfügung stellt.

  [en] A mixin class that provides slots for modeling a temporal validity of information
  (not of an event).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
mixin: true
slots:
- valid_from
- valid_through
- is_active

```
</details>

### Induced

<details>
```yaml
name: HasTemporalValidity
description: '[de] Eine Mixin-Klasse, die Slots für die Modellierung einer zeitlichen
  Gültigkeit einer Information (nicht eines Events) zur Verfügung stellt.

  [en] A mixin class that provides slots for modeling a temporal validity of information
  (not of an event).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
mixin: true
attributes:
  valid_from:
    name: valid_from
    description: '[de] Das Datum, ab dem die Information gültig ist.

      [en] The date from which the information is valid.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: schema:validFrom
    alias: valid_from
    owner: HasTemporalValidity
    domain_of:
    - HasTemporalValidity
    range: date
  valid_through:
    name: valid_through
    description: '[de] Das Datum, bis und mit dem die Information gültig ist.

      [en] The date until which the information is valid, inclusive.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: schema:validThrough
    alias: valid_through
    owner: HasTemporalValidity
    domain_of:
    - HasTemporalValidity
    range: date
  is_active:
    name: is_active
    description: '[de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich
      sein, wenn diese Information explizit vorhanden ist.

      [en] Indicates whether the information is currently valid. Can be useful when
      this information is explicitly available.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: mcm:isCurrent
    alias: is_active
    owner: HasTemporalValidity
    domain_of:
    - HasTemporalValidity
    range: boolean

```
</details></div>