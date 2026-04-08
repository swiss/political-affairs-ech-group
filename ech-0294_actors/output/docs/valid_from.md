---
search:
  boost: 5.0
---

# Slot: valid_from 


_[de] Das Datum, ab dem die Information gültig ist._

_[en] The date from which the information is valid._

__



<div data-search-exclude markdown="1">



URI: [schema:validFrom](http://schema.org/validFrom)
Alias: valid_from

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Occupation](Occupation.md) | [de] Beruf oder Tätigkeit einer Person mit Angabe eines Labels, eines ISCO-19... |  no  |
| [Citizenship](Citizenship.md) | [de] Staatsbürgerschaft einer Person mit Angabe des Landes und der zeitlichen... |  no  |
| [HasTemporalValidity](HasTemporalValidity.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung einer zeitlichen Gülti... |  no  |
| [ElectoralDistrict](ElectoralDistrict.md) | [de] Wahlkreis oder Wahlregion, in der eine Person politisch aktiv ist; mit z... |  no  |
| [Group](Group.md) | [de] Eine politische Gruppe, Organisation oder Körperschaft (z |  no  |
| [InterestLink](InterestLink.md) | [de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer P... |  no  |
| [Name](Name.md) | [de] Ein Name mit einem Typ (z |  no  |
| [Training](Training.md) | [de] Ausbildung oder Bildung einer Person mit Angabe eines Typs (z |  no  |
| [Gender](Gender.md) | [de] Geschlecht einer Person mit Angabe eines Geschlechtscodes und der zeitli... |  no  |
| [Membership](Membership.md) | [de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [HasTemporalValidity](HasTemporalValidity.md) |
| Slot URI | [schema:validFrom](http://schema.org/validFrom) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:validFrom |
| native | act:valid_from |




## LinkML Source

<details>
```yaml
name: valid_from
description: '[de] Das Datum, ab dem die Information gültig ist.

  [en] The date from which the information is valid.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: schema:validFrom
alias: valid_from
domain_of:
- HasTemporalValidity
range: date

```
</details></div>