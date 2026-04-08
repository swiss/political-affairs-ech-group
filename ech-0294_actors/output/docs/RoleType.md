---
search:
  boost: 10.0
---

# Class: RoleType 


_[de] Rolle einer Person in einer Mitgliedschaft oder Funktion (z.B. Mitglied, Präsident, Stellvertreter)._

_[en] Role of a person in a membership or function (e.g., member, president, deputy)._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [role_type_enum](role_type_enum.md) | 0..1 <br/> [RoleEnum](RoleEnum.md) | [en] Role of the person in the membership or function | direct |
| [label](label.md) | 0..1 <br/> [String](String.md) | [de] Möglichkeit bei einer strukturierten Information, ein Label zu vergeben ... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](Membership.md) | [role_type](role_type.md) | range | [RoleType](RoleType.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:RoleType |
| native | act:RoleType |







