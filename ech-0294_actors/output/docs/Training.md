---
search:
  boost: 10.0
---

# Class: Training 


_[de] Ausbildung oder Bildung einer Person mit Angabe eines Typs (z.B. Schulabschluss, Universitätsabschluss, Militärdienst), eines Labels, eines ISCO-19 Codes und der zeitlichen Gültigkeit._

_[en] Training or education of a person indicating a type (e.g., school diploma, university degree, military service), a label, an ISCO-19 code, and temporal validity._

__



<div data-search-exclude markdown="1">




## Attribute

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







