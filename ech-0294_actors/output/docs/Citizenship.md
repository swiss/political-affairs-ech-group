---
search:
  boost: 10.0
---

# Class: Citizenship 


_[de] Staatsangehörigkeit einer Person unter Angabe des Landes und der zeitlichen Gültigkeit. Wenn kein `valid_from` angegeben ist, ist diese Information nicht bekannt. Ist bekannt, dass die Staatsangehörigkeit seit der Geburt gültig ist, ist das Geburtsdatum hier anzugeben. Wenn kein `valid_through` angegeben ist, ist die Staatsangehörigkeit weiterhin gültig._

_[en] Citizenship (also used for Nationality) of a person indicating the country and temporal validity. If there is no `valid_from` provided, the information is not known. If it is known that the citizenship is valid from birth, the birthdate is to be repeated here. If there is no `valid_through`, the citizenship is still active._

__



<div data-search-exclude markdown="1">




## Attribute

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







