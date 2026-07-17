

## Class: Motion 


_[en] A formal proposal or motion submitted during proceedings._

_[de] Ein formeller Antrag, der während der Verhandlungen eingereicht wird._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| title | 0..1 <br/> [String](String.md) | None |
| description | 0..1 <br/> [String](String.md) | None |
| documents | * <br/> [Work](Work.md) | [de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind. [en] List of documents (FRBR Works) linked to the entity.  |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |






















</div>