

## Class: PersonReference 


_Lightweight reference to a person with key identification data at time of linking. Preserves historical accuracy even if the person changes later._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| label | 1 <br/> [String](String.md) | Mandatory short display name to identify the person within the organisation (e.g. with added birth year to distinguish persons with the same name).  |
| label_long | 0..1 <br/> [String](String.md) | Optional long display name including academic titles and full official name (e.g. "Dr. Maria Muster-Beispiel").  |
| role_type | 0..1 <br/> [RoleType](RoleType.md) | Role of the person in the membership or function.  |
| group_label | 0..1 <br/> [String](String.md) | Name of the body/group at time of linking.  |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. https://www.wikidata.org/wiki/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](Membership.md) | [person_reference](person_reference.md) | range | [PersonReference](PersonReference.md) |
| [InterestLink](InterestLink.md) | [person_reference](person_reference.md) | range | [PersonReference](PersonReference.md) |



















</div>