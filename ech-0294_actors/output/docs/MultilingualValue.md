---
search:
  boost: 10.0
---

# Class: MultilingualValue 


_[de] Ein mehrsprachiger String mit Angabe der Sprache._

_[en] A multilingual string with language specification._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 0..1 <br/> [String](String.md) | [de] Der eigentliche Wert einer Information neben weiteren attributen wie Typ... | direct |
| [language](language.md) | 0..1 <br/> [String](String.md) | [de] Sprachcode im ISO 639-1 Format | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Group](Group.md) | [abbreviation](abbreviation.md) | range | [MultilingualValue](MultilingualValue.md) |
| [Group](Group.md) | [description](description.md) | range | [MultilingualValue](MultilingualValue.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:MultilingualValue |
| native | act:MultilingualValue |







