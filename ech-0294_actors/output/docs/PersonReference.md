---
search:
  boost: 10.0
---

# Class: PersonReference 


_[de] Leichtgewichtige Referenz auf eine Person mit den wichtigsten Identifikationsmerkmalen zum Zeitpunkt der Verknüpfung. Ermöglicht historische Korrektheit auch wenn sich die Person später ändert._

_[en] Lightweight reference to a person with key identification data at time of linking. Preserves historical accuracy even if the person changes later._

__



<div data-search-exclude markdown="1">




## Attribute

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [label](label.md) | 0..1 <br/> [String](String.md) | [de] Möglichkeit bei einer strukturierten Information, ein Label zu vergeben ... | direct |
| [label_long](label_long.md) | 0..1 <br/> [String](String.md) | [de] Möglichkeit bei einer strukturierten Information, ein erweitertesLabel z... | direct |
| [role_type](role_type.md) | 0..1 <br/> [RoleType](RoleType.md) | [en] Role of the person in the membership or function | direct |
| [group_label](group_label.md) | 0..1 <br/> [String](String.md) | [de] Name des Gremiums zum Zeitpunkt der Verknüpfung | direct |
| [local_id](local_id.md) | 0..1 <br/> [String](String.md) | [de] Lokaler Identifikator | [HasIdentification](HasIdentification.md) |
| [global_uri](global_uri.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine eindeutige, global gültige URI für die Entität | [HasIdentification](HasIdentification.md) |
| [wikidata_uri](wikidata_uri.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | [de] Eine URI, die auf eine Wikidata-Entität verweist, z | [HasIdentification](HasIdentification.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](Membership.md) | [person_reference](person_reference.md) | range | [PersonReference](PersonReference.md) |
| [InterestLink](InterestLink.md) | [person_reference](person_reference.md) | range | [PersonReference](PersonReference.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:PersonReference |
| native | act:PersonReference |







