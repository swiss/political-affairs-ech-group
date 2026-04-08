---
search:
  boost: 10.0
---

# Class: Contact 


_[de] Kontaktinformation einer Person mit Angabe eines Typs (z.B. E-Mail, LinkedIn) und eines Werts._

_[en] Contact information of a person indicating a type (e.g., email, LinkedIn) and a value._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [contact_type](contact_type.md) | 0..1 <br/> [ContactTypeEnum](ContactTypeEnum.md) | [de] Typ der Kontaktinformation | direct |
| [value](value.md) | 0..1 <br/> [String](String.md) | [de] Der eigentliche Wert einer Information neben weiteren attributen wie Typ... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Person](Person.md) | [contacts](contacts.md) | range | [Contact](Contact.md) |
| [Group](Group.md) | [contacts](contacts.md) | range | [Contact](Contact.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Contact |
| native | act:Contact |







