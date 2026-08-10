

## Class: HasIdentification 


_A mixin class that provides slots for the identification of an entity. It is used for entities that are identified in their own right; their `global_uri` is the identifier and therefore mandatory._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system.  |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity.  |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans.  |



### Mixin Usage

[Container](Container.md), [Person](Person.md), [Group](Group.md), [Membership](Membership.md), [InterestLink](InterestLink.md), [ElectoralDistrict](ElectoralDistrict.md)





















</div>