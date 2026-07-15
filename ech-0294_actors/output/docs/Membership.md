

## Class: Membership 


_A membership relationship between a person and a group, representing formal affiliation (e.g., party member, commission member, parliamentarian). Distinct from InterestLink, which covers external interest bindings and conflicts of interest to organizations outside the actor schema._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| person_reference | 0..1 <br/> [PersonReference](PersonReference.md) | Reference to a person with snapshot data at time of linking.  |
| group_reference | 0..1 <br/> [GroupReference](GroupReference.md) | Reference to a group with snapshot data at time of linking.  |
| role_type | 0..1 <br/> [RoleType](RoleType.md) | Role of the person in the membership or function.  |
| authorized_to_vote | 0..1 <br/> [Boolean](Boolean.md) | Indicates if the person is authorized to vote in the group. Typically false for substitute members (when not deputizing), observers, secretaries, and guests.  |
| is_active | 0..1 <br/> [Boolean](Boolean.md) | Indicates if the membership is currently active. Can complement or replace `valid_from`/`valid_through`. If not set, activity is derived from the temporal validity fields.  |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| valid_from | 0..1 <br/> [Date](Date.md) | The date from which the information is valid. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |
| valid_through | 0..1 <br/> [Date](Date.md) | The date until which the information is valid, inclusive. <br/><br/>Inheritance: [HasTemporalValidity](HasTemporalValidity.md) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [memberships](memberships.md) | range | [Membership](Membership.md) |



















</div>