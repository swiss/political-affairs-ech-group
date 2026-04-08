---
search:
  boost: 10.0
---

# Class: Citizenship 


_[de] Staatsbürgerschaft einer Person mit Angabe des Landes und der zeitlichen Gültigkeit._

_[en] Citizenship of a person indicating the country and temporal validity._

__



<div data-search-exclude markdown="1">



URI: [act:Citizenship](https://ld.ech.ch/schema/0294/actors/Citizenship)





## Inheritance
* **Citizenship** [ [HasTemporalValidity](HasTemporalValidity.md)]


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [country](country.md) | 0..1 <br/> [String](String.md) | [de] ISO 3166 Ländercode | direct |
| [valid_from](valid_from.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, ab dem die Information gültig ist | [HasTemporalValidity](HasTemporalValidity.md) |
| [valid_through](valid_through.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, bis und mit dem die Information gültig ist | [HasTemporalValidity](HasTemporalValidity.md) |
| [is_active](is_active.md) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Information aktuell gültig ist | [HasTemporalValidity](HasTemporalValidity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [citizenships](citizenships.md) | range | [Citizenship](Citizenship.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Citizenship |
| native | act:Citizenship |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Citizenship
description: '[de] Staatsbürgerschaft einer Person mit Angabe des Landes und der zeitlichen
  Gültigkeit.

  [en] Citizenship of a person indicating the country and temporal validity.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
mixins:
- HasTemporalValidity
slots:
- country

```
</details>

### Induced

<details>
```yaml
name: Citizenship
description: '[de] Staatsbürgerschaft einer Person mit Angabe des Landes und der zeitlichen
  Gültigkeit.

  [en] Citizenship of a person indicating the country and temporal validity.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
mixins:
- HasTemporalValidity
attributes:
  country:
    name: country
    description: '[de] ISO 3166 Ländercode.

      [en] ISO 3166 country code.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: act:country
    alias: country
    owner: Citizenship
    domain_of:
    - Citizenship
    range: string
    pattern: ^[A-Z]{2}$
  valid_from:
    name: valid_from
    description: '[de] Das Datum, ab dem die Information gültig ist.

      [en] The date from which the information is valid.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: schema:validFrom
    alias: valid_from
    owner: Citizenship
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
    owner: Citizenship
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
    owner: Citizenship
    domain_of:
    - HasTemporalValidity
    range: boolean

```
</details></div>