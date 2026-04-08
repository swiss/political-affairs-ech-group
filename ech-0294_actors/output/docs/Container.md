---
search:
  boost: 10.0
---

# Class: Container 


_[de] Container für politische Akteure, Gruppen und Beziehungen._

_[en] Container for political actors, groups, and relationships._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [persons](persons.md) | * <br/> [Person](Person.md) | [de] Sammlung von Personen | direct |
| [groups](groups.md) | * <br/> [Group](Group.md) | [de] Sammlung von Gruppen | direct |
| [memberships](memberships.md) | * <br/> [Membership](Membership.md) | [de] Sammlung von Mitgliedschaften | direct |
| [interest_links](interest_links.md) | * <br/> [InterestLink](InterestLink.md) | [de] Sammlung von Interessenbindungen | direct |
| [local_id](local_id.md) | 0..1 <br/> [String](String.md) | [de] Lokaler Identifikator | [HasIdentification](HasIdentification.md) |
| [global_uri](global_uri.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine eindeutige, global gültige URI für die Entität | [HasIdentification](HasIdentification.md) |
| [wikidata_uri](wikidata_uri.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z | [HasIdentification](HasIdentification.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:Container |
| native | act:Container |







