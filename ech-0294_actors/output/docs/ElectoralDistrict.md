---
search:
  boost: 10.0
---

# Class: ElectoralDistrict 


_[de] Wahlkreis oder Wahlregion, in der eine Person politisch aktiv ist; mit zeitlicher Gültigkeit._

_[en] Electoral district or region where a person is politically active; with temporal validity._

__



<div data-search-exclude markdown="1">



URI: [act:ElectoralDistrict](https://ld.ech.ch/schema/0294/actors/ElectoralDistrict)





## Inheritance
* **ElectoralDistrict** [ [HasTemporalValidity](HasTemporalValidity.md)]


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [district](district.md) | 0..1 <br/> [String](String.md) | [de] Wahlkreis oder Wahlregion | direct |
| [valid_from](valid_from.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, ab dem die Information gültig ist | [HasTemporalValidity](HasTemporalValidity.md) |
| [valid_through](valid_through.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, bis und mit dem die Information gültig ist | [HasTemporalValidity](HasTemporalValidity.md) |
| [is_active](is_active.md) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Information aktuell gültig ist | [HasTemporalValidity](HasTemporalValidity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [electoral_district](electoral_district.md) | range | [ElectoralDistrict](ElectoralDistrict.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:ElectoralDistrict |
| native | act:ElectoralDistrict |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ElectoralDistrict
description: '[de] Wahlkreis oder Wahlregion, in der eine Person politisch aktiv ist;
  mit zeitlicher Gültigkeit.

  [en] Electoral district or region where a person is politically active; with temporal
  validity.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
mixins:
- HasTemporalValidity
slots:
- district

```
</details>

### Induced

<details>
```yaml
name: ElectoralDistrict
description: '[de] Wahlkreis oder Wahlregion, in der eine Person politisch aktiv ist;
  mit zeitlicher Gültigkeit.

  [en] Electoral district or region where a person is politically active; with temporal
  validity.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
mixins:
- HasTemporalValidity
attributes:
  district:
    name: district
    description: '[de] Wahlkreis oder Wahlregion.

      [en] Electoral district or region.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: act:district
    alias: district
    owner: ElectoralDistrict
    domain_of:
    - ElectoralDistrict
    range: string
  valid_from:
    name: valid_from
    description: '[de] Das Datum, ab dem die Information gültig ist.

      [en] The date from which the information is valid.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: schema:validFrom
    alias: valid_from
    owner: ElectoralDistrict
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
    owner: ElectoralDistrict
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
    owner: ElectoralDistrict
    domain_of:
    - HasTemporalValidity
    range: boolean

```
</details></div>