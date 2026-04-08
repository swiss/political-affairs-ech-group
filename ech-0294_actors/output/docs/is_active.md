---
search:
  boost: 5.0
---

# Slot: is_active 


_[de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein, wenn diese Information explizit vorhanden ist._

_[en] Indicates whether the information is currently valid. Can be useful when this information is explicitly available._

__



<div data-search-exclude markdown="1">



URI: [mcm:isCurrent](https://ld.ech.ch/schema/0292/meta-common/isCurrent)
Alias: is_active

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Training](Training.md) | [de] Ausbildung oder Bildung einer Person mit Angabe eines Typs (z |  no  |
| [HasTemporalValidity](HasTemporalValidity.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung einer zeitlichen Gülti... |  no  |
| [Group](Group.md) | [de] Eine politische Gruppe, Organisation oder Körperschaft (z |  no  |
| [Gender](Gender.md) | [de] Geschlecht einer Person mit Angabe eines Geschlechtscodes und der zeitli... |  no  |
| [ElectoralDistrict](ElectoralDistrict.md) | [de] Wahlkreis oder Wahlregion, in der eine Person politisch aktiv ist; mit z... |  no  |
| [Occupation](Occupation.md) | [de] Beruf oder Tätigkeit einer Person mit Angabe eines Labels, eines ISCO-19... |  no  |
| [InterestLink](InterestLink.md) | [de] Eine Interessenbindung (Interessenkonflikt, Politikfinanzierung) einer P... |  no  |
| [Membership](Membership.md) | [de] Eine Mitgliedschaftsbeziehung zwischen einer Person und einer Gruppe |  no  |
| [Citizenship](Citizenship.md) | [de] Staatsbürgerschaft einer Person mit Angabe des Landes und der zeitlichen... |  no  |
| [Name](Name.md) | [de] Ein Name mit einem Typ (z |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [HasTemporalValidity](HasTemporalValidity.md) |
| Slot URI | [mcm:isCurrent](https://ld.ech.ch/schema/0292/meta-common/isCurrent) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:isCurrent |
| native | act:is_active |




## LinkML Source

<details>
```yaml
name: is_active
description: '[de] Gibt an, ob die Information aktuell gültig ist. Kann nützlich sein,
  wenn diese Information explizit vorhanden ist.

  [en] Indicates whether the information is currently valid. Can be useful when this
  information is explicitly available.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:isCurrent
alias: is_active
domain_of:
- HasTemporalValidity
range: boolean

```
</details></div>