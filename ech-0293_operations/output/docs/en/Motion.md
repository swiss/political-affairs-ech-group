

## Class: Motion 


_A formal proposal submitted during the proceedings, such as an amendment to a legal text, a procedural motion (e.g. closure of the debate) or a motion to refer back. It is an entity in its own right because an agenda item may contain several motions, each with its own course (submitted, supported, voted on) and possibly a vote of its own._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| title | 0..1 <br/> [String](String.md) | Short title of the motion.  |
| description | 0..1 <br/> [String](String.md) | Full text of the motion.  |
| documents | * <br/> [Work](Work.md) | List of documents (FRBR Works) linked to the entity.  |






















</div>