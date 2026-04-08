---
search:
  boost: 10.0
---

# Class: LanguageProficiency 


_[de] Sprachkenntnisse einer Person mit Angabe der Sprache und ob es sich um die bevorzugte Sprache oder die Muttersprache handelt._

_[en] Language proficiency of a person indicating the language and whether it is the preferred language or native language._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [language](language.md) | 0..1 <br/> [String](String.md) | [de] Sprachcode im ISO 639-1 Format | direct |
| [is_correspondence](is_correspondence.md) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob es sich um die bevorzugte Sprache handelt | direct |
| [is_native](is_native.md) | 0..1 <br/> [Boolean](Boolean.md) | [de] Gibt an, ob es sich um die Muttersprache handelt | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [language_proficiencies](language_proficiencies.md) | range | [LanguageProficiency](LanguageProficiency.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:LanguageProficiency |
| native | act:LanguageProficiency |







