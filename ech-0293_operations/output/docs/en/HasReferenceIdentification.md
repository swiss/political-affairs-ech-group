

## Class: HasReferenceIdentification 


_A mixin class that provides the slots with which a reference names the entity it points at. Unlike `HasIdentification` it does not identify the referencing object itself, which is why `global_uri` is neither an identifier here nor mandatory: a system that only holds the local id of the referenced entity states that id instead. A reference class using this mixin should require at least one of the two._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Local identifier of the referenced entity. It is resolved within the same delivery.  |
| global_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | The unique, globally valid URI of the referenced entity. Unlike a local_id it also resolves beyond the delivery.  |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans.  |



### Mixin Usage

| mixed into | description |
| --- | --- |
| [PersonReference](PersonReference.md) | Lightweight reference to a person with key identification data at time of lin... |
| [GroupReference](GroupReference.md) | Lightweight reference to a group with key identification data at time of link... |





















</div>