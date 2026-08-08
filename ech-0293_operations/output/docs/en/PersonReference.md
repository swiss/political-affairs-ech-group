

## Class: PersonReference 


_Lightweight reference to a person with key identification data at time of linking. Preserves historical accuracy even if the person changes later. The referenced person is identified by `local_id` or `global_uri`; at least one of the two is required._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| local_id | 0..1 <br/> [String](String.md) | Local identifier of the referenced entity. It is resolved within the same delivery. <br/><br/>Inheritance: [HasReferenceIdentification](HasReferenceIdentification.md) |
| global_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | The unique, globally valid URI of the referenced entity. Unlike a local_id it also resolves beyond the delivery. <br/><br/>Inheritance: [HasReferenceIdentification](HasReferenceIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasReferenceIdentification](HasReferenceIdentification.md) |
| label | 1 <br/> [String](String.md) | Mandatory short display name to identify the person within the organisation (e.g. with added birth year to distinguish persons with the same name).  |
| label_long | 0..1 <br/> [String](String.md) | Optional long display name including academic titles and full official name (e.g. "Dr. Maria Muster-Beispiel").  |
| group_label | 0..1 <br/> [String](String.md) | Name of the body/group at time of linking.  |

##### Constraints


At least one of the following must be set:

- [local_id](local_id.md)
- [global_uri](global_uri.md)










### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [IndividualVote](IndividualVote.md) | [actor_id](actor_id.md) | range | [PersonReference](PersonReference.md) |
| [IndividualAttendance](IndividualAttendance.md) | [actor_id](actor_id.md) | range | [PersonReference](PersonReference.md) |
| [Speech](Speech.md) | [actor_id](actor_id.md) | range | [PersonReference](PersonReference.md) |



















</div>