

## Class: GroupReference 


_Lightweight reference to a group with key identification data at time of linking._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| label | 0..1 <br/> [String](String.md) | Assign a label to a structured piece of information (e.g., display name, position, etc.).  |
| abbreviation | * <br/> [MultilingualValue](MultilingualValue.md) | Abbreviation (can be multilingual).  |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Legislature](Legislature.md) | [actor_id](actor_id.md) | range | [GroupReference](GroupReference.md) |
| [Meeting](Meeting.md) | [group_id](group_id.md) | range | [GroupReference](GroupReference.md) |
| [Meeting](Meeting.md) | [actor_id](actor_id.md) | range | [GroupReference](GroupReference.md) |
| [Voting](Voting.md) | [actor_id](actor_id.md) | range | [GroupReference](GroupReference.md) |
| [Election](Election.md) | [actor_id](actor_id.md) | range | [GroupReference](GroupReference.md) |
| [Attendance](Attendance.md) | [actor_id](actor_id.md) | range | [GroupReference](GroupReference.md) |



















</div>