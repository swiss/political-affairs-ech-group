

## Class: Motion 


_A formal proposal or motion submitted during proceedings._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| title | 0..1 <br/> [String](String.md) | Title of the element.  |
| description | 0..1 <br/> [String](String.md) | Descriptive text of the element.  |
| documents | * <br/> [Work](Work.md) | List of documents (FRBR Works) linked to the entity.  |






















</div>