

# Class: MultilingualValue 


_[de] Ein mehrsprachiger String mit Angabe der Sprache._

_[en] A multilingual string with language specification._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| value | 0..1 <br/> [String](String.md) | [de] Der eigentliche Wert einer Information neben weiteren attributen wie Typ, Sprache, etc.
[en] The value of an information besides other attributes such as type, language, etc.
 |
| language | 0..1 <br/> [String](String.md) | [de] Sprachcode im ISO 639-1 Format.
[en] Language code in ISO 639-1 format.
 |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Group](Group.md) | [abbreviation](abbreviation.md) | range | [MultilingualValue](MultilingualValue.md) |
| [Group](Group.md) | [description](description.md) | range | [MultilingualValue](MultilingualValue.md) |
| [GroupReference](GroupReference.md) | [abbreviation](abbreviation.md) | range | [MultilingualValue](MultilingualValue.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:MultilingualValue |
| native | act:MultilingualValue |









</div>