---
search:
  boost: 10.0
---

# Class: GroupType 


_[de] Art der Gruppe (z.B. Partei, Kommission, Parlament, Departement)._

_[en] Type of group (e.g., party, committee, parliament, department)._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [group_type_enum](group_type_enum.md) | 0..1 <br/> [GroupTypeEnum](GroupTypeEnum.md) | [de] Link zum kontrollierten Vokabular für Gruppentypen | direct |
| [label](label.md) | 0..1 <br/> [String](String.md) | [de] Möglichkeit bei einer strukturierten Information, ein Label zu vergeben ... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Group](Group.md) | [group_type](group_type.md) | range | [GroupType](GroupType.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:GroupType |
| native | act:GroupType |







