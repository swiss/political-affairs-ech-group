

## Class: Election 


_An election procedure for selecting persons to positions._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| datetime_begin | 0..1 <br/> [Datetime](Datetime.md) | The date and time when the meeting or voting begins.  |
| datetime_end | 0..1 <br/> [Datetime](Datetime.md) | The date and time when the meeting or voting ends.  |
| election_type | 0..1 <br/> [ElectionTypeEnum](ElectionTypeEnum.md) | Type of election procedure.  |
| type_label | 0..1 <br/> [String](String.md) | Custom type label when standard type values don't apply.  |
| title | 0..1 <br/> [String](String.md) | Title of the element.  |
| landing_page | 0..1 <br/> [String](String.md) | URL providing further information.  |
| total_absent | 0..1 <br/> [Integer](Integer.md) | Total number of absent members. Distinction between absent/excused absent - presence is tracked on attendance list.  |
| total | 0..1 <br/> [Integer](Integer.md) | Total number of votes, excluding absent and president's vote.  |
| majority_type | 0..1 <br/> [MajorityTypeEnum](MajorityTypeEnum.md) | Type of majority required for the vote (absolute, two-thirds, etc.).  |
| majority_count | 0..1 <br/> [Integer](Integer.md) | Number of votes required for the relevant majority threshold.  |
| result_text | 0..1 <br/> [String](String.md) | Free text describing the outcome of the vote, e.g., "Accepted with 78 votes".  |
| parent_meeting | 0..1 <br/> [String](String.md) | The linked meeting ID that groups the current meeting.  |
| parent_agenda_item | 0..1 <br/> [String](String.md) | If needed, this slot builds a hierarchy of agenda items.  |
| affair_id | 0..1 <br/> [String](String.md) | The connection to the affairs (business items) of the agenda item.  |
| actor_id | 0..1 <br/> [GroupReference](GroupReference.md) | Reference to the acting body/organ (lightweight snapshot at time of linking).  |
| documents | * <br/> [Work](Work.md) | List of documents (FRBR Works) linked to the entity.  |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [elections](elections.md) | range | [Election](Election.md) |



















</div>