---
search:
  boost: 10.0
---

# Class: Training 


_[de] Ausbildung oder Bildung einer Person mit Angabe eines Typs (z.B. Schulabschluss, Universitätsabschluss, Militärdienst), eines Labels, eines ISCO-19 Codes und der zeitlichen Gültigkeit._

_[en] Training or education of a person indicating a type (e.g., school diploma, university degree, military service), a label, an ISCO-19 code, and temporal validity._

__



<div data-search-exclude markdown="1">



URI: [act:Training](https://ld.ech.ch/schema/0294/actors/Training)





## Inheritance
* **Training** [ [HasTemporalValidity](HasTemporalValidity.md)]


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [training_type](training_type.md) | 0..1 <br/> [TrainingTypeEnum](TrainingTypeEnum.md) | [de] Typ der Ausbildung oder Bildung | direct |
| [training_code](training_code.md) | 0..1 <br/> [String](String.md) | [de] ISCO-19 Code der Ausbildung oder Bildung | direct |
| [value](value.md) | 0..1 <br/> [String](String.md) | [de] Der eigentliche Wert einer Information neben weiteren attributen wie Typ... | direct |
| [valid_from](valid_from.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, ab dem die Information gültig ist | [HasTemporalValidity](HasTemporalValidity.md) |
| [valid_through](valid_through.md) | 0..1 <br/> [Date](Date.md) | [de] Das Datum, bis und mit dem die Information gültig ist | [HasTemporalValidity](HasTemporalValidity.md) |
| [is_active](is_active.md) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob die Information aktuell gültig ist | [HasTemporalValidity](HasTemporalValidity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [trainings](trainings.md) | range | [Training](Training.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Training |
| native | act:Training |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Training
description: '[de] Ausbildung oder Bildung einer Person mit Angabe eines Typs (z.B.
  Schulabschluss, Universitätsabschluss, Militärdienst), eines Labels, eines ISCO-19
  Codes und der zeitlichen Gültigkeit.

  [en] Training or education of a person indicating a type (e.g., school diploma,
  university degree, military service), a label, an ISCO-19 code, and temporal validity.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
mixins:
- HasTemporalValidity
slots:
- training_type
- training_code
- value

```
</details>

### Induced

<details>
```yaml
name: Training
description: '[de] Ausbildung oder Bildung einer Person mit Angabe eines Typs (z.B.
  Schulabschluss, Universitätsabschluss, Militärdienst), eines Labels, eines ISCO-19
  Codes und der zeitlichen Gültigkeit.

  [en] Training or education of a person indicating a type (e.g., school diploma,
  university degree, military service), a label, an ISCO-19 code, and temporal validity.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
mixins:
- HasTemporalValidity
attributes:
  training_type:
    name: training_type
    description: '[de] Typ der Ausbildung oder Bildung.

      [en] Type of training or education.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: act:trainingType
    alias: training_type
    owner: Training
    domain_of:
    - Training
    range: TrainingTypeEnum
  training_code:
    name: training_code
    description: '[de] ISCO-19 Code der Ausbildung oder Bildung.

      [en] ISCO-19 code of the training or education.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: act:trainingCode
    alias: training_code
    owner: Training
    domain_of:
    - Training
    range: string
  value:
    name: value
    description: '[de] Der eigentliche Wert einer Information neben weiteren attributen
      wie Typ, Sprache, etc.

      [en] The value of an information besides other attributes such as type, language,
      etc.

      '
    from_schema: https://ld.ech.ch/schema/0294/actors
    rank: 1000
    slot_uri: mcm:value
    alias: value
    owner: Training
    domain_of:
    - Name
    - Training
    - Contact
    - MultilingualValue
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
    owner: Training
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
    owner: Training
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
    owner: Training
    domain_of:
    - HasTemporalValidity
    range: boolean

```
</details></div>