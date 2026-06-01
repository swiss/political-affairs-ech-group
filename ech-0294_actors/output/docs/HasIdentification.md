

## Class: HasIdentification 


_A mixin class that provides slots for the identification of an entity._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system.  |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity.  |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland.  |



### Mixin Usage

| mixed into | description |
| --- | --- |
| [Container](Container.md) | Container for political actors, groups, and relationships |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |
| [Group](Group.md) | A political group, organization, or body (e |
| [PersonReference](PersonReference.md) | Lightweight reference to a person with key identification data at time of lin... |
| [GroupReference](GroupReference.md) | Lightweight reference to a group with key identification data at time of link... |
| [Membership](Membership.md) | A membership relationship between a person and a group, representing formal a... |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |
| [IsProcessStep](IsProcessStep.md) | A mixin class for a single step in a multi-stage process (e |





















</div>