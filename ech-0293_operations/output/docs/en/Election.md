

## Class: Election 


_An election in which a parliamentary body appoints one or several persons to an office or function. Unlike a voting (Voting), which decides substantive questions, an election is a decision on persons: it is often held by secret ballot and usually requires an absolute majority, whereas votings are mostly open. The presiding member, who does not take part in votings, does vote in elections. Each ballot is recorded as a separate election; the ballots of one election are linked through the common agenda item — for instance a first ballot requiring an absolute majority that remains without result, followed by a second ballot in which the relative majority suffices._




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
| title | 0..1 <br/> [String](String.md) | Title of the election, e.g. "Wahl Kommissionspräsidium WAK".  |
| landing_page | 0..1 <br/> [String](String.md) | URL providing further information.  |
| total_absent | 0..1 <br/> [Integer](Integer.md) | Number of absent members who could not take part. Whether an absence was excused is tracked on the attendance list (Attendance).  |
| total | 0..1 <br/> [Integer](Integer.md) | Total number of votes, excluding absent and president's vote.  |
| majority_type | 0..1 <br/> [MajorityTypeEnum](MajorityTypeEnum.md) | Type of majority required for the vote (absolute, two-thirds, etc.).  |
| majority_count | 0..1 <br/> [Integer](Integer.md) | Number of votes required for the relevant majority threshold.  |
| result_text | 0..1 <br/> [String](String.md) | Free text describing the outcome, e.g. "Accepted with 120 to 75 votes with 5 abstentions". For votings, the categorical decision (accepted, rejected, noted …) is not recorded here but in the Resolution (resolution_type) of the agenda item.  |
| parent_meeting | 0..1 <br/> [String](String.md) | Identifier of the meeting this record belongs to. On a meeting it names the superordinate meeting; on an agenda item, voting, election, speech or protocol it names the meeting in which the record arose.  |
| parent_protocol | 0..1 <br/> [Protocol](Protocol.md) | The protocol in which the voting or election is recorded. A vote is held during the sitting and is therefore anchored in the minutes, not in the agenda planned beforehand: what was put on the agenda does not yet say what was actually voted on. Conversely, the protocol lists its votings and elections (votings, elections).  |
| parent_protocol_item | 0..1 <br/> [ProtocolItem](ProtocolItem.md) | The recorded agenda item (ProtocolItem) under which the voting or election took place. Omitted when the vote was taken without an agenda item; the link to the sitting is then given by parent_protocol and parent_meeting alone.  |
| affair_id | 0..1 <br/> [String](String.md) | Identifier of the affair (eCH-0295) the record refers to. Administrative agenda items (e.g. approval of the minutes) have no affair. An affair usually runs through several agenda items — in legislation, for instance, the debate on entering into the matter, the detailed deliberation, the final vote and, where applicable, the procedure for resolving differences between the chambers.  |
| actor_id | 0..1 <br/> [GroupReference](GroupReference.md) | Reference to the acting body/organ (lightweight snapshot at time of linking).  |
| documents | * <br/> [Work](Work.md) | List of documents (FRBR Works) linked to the entity.  |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Container](Container.md) | [elections](elections.md) | range | [Election](Election.md) |
| [Protocol](Protocol.md) | [elections](elections.md) | range | [Election](Election.md) |



















</div>