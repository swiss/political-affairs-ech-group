

## Class: GroupReference 


_Lightweight reference to a group with key identification data at time of linking. The referenced group is identified by `local_id` or `global_uri`; at least one of the two is required. A `local_id` is resolved within the same delivery, a `global_uri` also beyond it._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Local identifier of the referenced entity. It is resolved within the same delivery. <br/><br/>Inheritance: [HasReferenceIdentification](HasReferenceIdentification.md) |
| global_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | The unique, globally valid URI of the referenced entity. Unlike a local_id it also resolves beyond the delivery. <br/><br/>Inheritance: [HasReferenceIdentification](HasReferenceIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasReferenceIdentification](HasReferenceIdentification.md) |
| label | 0..1 <br/> [String](String.md) | Assign a label to a structured piece of information (e.g., display name, position, etc.).  |
| abbreviation | * <br/> [MultilingualValue](MultilingualValue.md) | Abbreviation (can be multilingual).  |

##### Constraints


At least one of the following must be set:

- [local_id](local_id.md)
- [global_uri](global_uri.md)










### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Group](Group.md) | [parent_groups](parent_groups.md) | range | [GroupReference](GroupReference.md) |
| [Membership](Membership.md) | [group_reference](group_reference.md) | range | [GroupReference](GroupReference.md) |



















</div>