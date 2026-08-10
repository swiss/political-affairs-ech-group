

## Class: Media 


_Media files or documents (including protocols in PDF/HTML/WORD or links to audio/video)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| title | 0..1 <br/> [String](String.md) | Title of the element.  |
| media_type | 0..1 <br/> [String](String.md) | Type of media (audio, video, document).  |
| url | * <br/> [MultilingualString](MultilingualString.md) | Landing page or further web address, multilingual.  |
| version | 0..1 <br/> [String](String.md) | Version number or identifier.  |
| parent_type | 0..1 <br/> [String](String.md) | Type of parent object (meeting, agenda, speech, affair).  |






















</div>