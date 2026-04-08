---
search:
  boost: 10.0
---

# Class: Gender 


_[de] Geschlecht einer Person mit Angabe eines Geschlechtscodes und der zeitlichen Gültigkeit._

_[en] Gender of a person indicating a gender code and temporal validity._

__



<div data-search-exclude markdown="1">



URI: [act:Gender](https://ld.ech.ch/schema/0294/actors/Gender)





## Inheritance
* **Gender** [ [HasTemporalValidity](HasTemporalValidity.md)]


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [gender_code](gender_code.md) | 0..1 <br/> [String](String.md) | [de] Geschlechtscode (z | direct |
| [pronouns](pronouns.md) | * <br/> [String](String.md) | [de] Von der Person verwendete Pronomen | direct |
| [valid_from](valid_from.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, ab dem die Information gültig ist | [HasTemporalValidity](HasTemporalValidity.md) |
| [valid_through](valid_through.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, bis und mit dem die Information gültig ist | [HasTemporalValidity](HasTemporalValidity.md) |
| [is_active](is_active.md) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Information aktuell gültig ist | [HasTemporalValidity](HasTemporalValidity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [genders](genders.md) | range | [Gender](Gender.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Gender |
| native | act:Gender |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Gender
description: '[de] Geschlecht einer Person mit Angabe eines Geschlechtscodes und der
  zeitlichen Gültigkeit.

  [en] Gender of a person indicating a gender code and temporal validity.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
mixins:
- HasTemporalValidity
slots:
- gender_code
- pronouns

```
</details>

### Induced

<details>
```yaml
name: Gender
description: '[de] Geschlecht einer Person mit Angabe eines Geschlechtscodes und der
  zeitlichen Gültigkeit.

  [en] Gender of a person indicating a gender code and temporal validity.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
mixins:
- HasTemporalValidity
attributes:
  gender_code:
    name: gender_code
    description: '[de] Geschlechtscode (z.B. gemäß ISO 5218).

      [en] Gender code (e.g., according to ISO 5218).

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: act:genderCode
    alias: gender_code
    owner: Gender
    domain_of:
    - Gender
    range: string
  pronouns:
    name: pronouns
    description: '[de] Von der Person verwendete Pronomen.

      [en] Pronouns used by the person.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: act:pronouns
    alias: pronouns
    owner: Gender
    domain_of:
    - Gender
    range: string
    multivalued: true
    inlined: true
    inlined_as_list: true
  valid_from:
    name: valid_from
    description: '[de] Das Datum, ab dem die Information gültig ist.

      [en] The date from which the information is valid.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: schema:validFrom
    alias: valid_from
    owner: Gender
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
    owner: Gender
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
    owner: Gender
    domain_of:
    - HasTemporalValidity
    range: boolean

```
</details></div>