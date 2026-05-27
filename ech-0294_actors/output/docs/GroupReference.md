---
search:
  boost: 10.0
---

# Class: GroupReference 


_[de] Leichtgewichtige Referenz auf eine Gruppe mit den wichtigsten Identifikationsmerkmalen zum Zeitpunkt der Verknüpfung._

_[en] Lightweight reference to a group with key identification data at time of linking._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [label](label.md) | 0..1 <br/> [String](String.md) | [de] Möglichkeit bei einer strukturierten Information, ein Label zu vergeben ... | direct |
| [abbreviation](abbreviation.md) | * <br/> [MultilingualValue](MultilingualValue.md) | [de] Abkürzung (kann mehrsprachig sein) | direct |
| [group_type](group_type.md) | 0..1 <br/> [GroupType](GroupType.md) | [de] Klasse der Gruppierung, wie z | direct |
| [local_id](local_id.md) | 0..1 <br/> [String](String.md) | [de] Lokaler Identifikator | [HasIdentification](HasIdentification.md) |
| [global_uri](global_uri.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine eindeutige, global gültige URI für die Entität | [HasIdentification](HasIdentification.md) |
| [wikidata_uri](wikidata_uri.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z | [HasIdentification](HasIdentification.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](Membership.md) | [group_reference](group_reference.md) | range | [GroupReference](GroupReference.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:GroupReference |
| native | act:GroupReference |







