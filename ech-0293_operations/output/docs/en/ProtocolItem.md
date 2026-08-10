

## Class: ProtocolItem 


_An agenda item as actually recorded in the protocol._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| parent_meeting | 0..1 <br/> [String](String.md) | The linked meeting ID that groups the current meeting. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](AgendaItemTypeEnum.md) | Type of agenda item, distinguishing individual items from groups. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| agenda_item_number | 0..1 <br/> [String](String.md) | Sequential number of the agenda item (string type to support roman numerals). <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| agenda_item_position | 0..1 <br/> [Integer](Integer.md) | Integer position of the agenda item in the meeting sequence. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| leading_actor_id | 0..1 <br/> [String](String.md) | The leading department for the agenda item. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| speaking_actor_id | 0..1 <br/> [String](String.md) | The speaker or head of the department for the agenda item. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| agenda_item_title | * <br/> [MultilingualString](MultilingualString.md) | Title of the agenda item. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| affair_id | 0..1 <br/> [String](String.md) | The connection to the affairs (business items) of the agenda item. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| agenda_item_description | * <br/> [MultilingualString](MultilingualString.md) | Subtitle or detailed description of the agenda item. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| state_id | 0..1 <br/> [String](String.md) | State identifier (reference to state enum or custom state). <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| state_name | 0..1 <br/> [String](String.md) | Custom state description for the meeting. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| landing_page | 0..1 <br/> [String](String.md) | URL providing further information. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| url | * <br/> [MultilingualString](MultilingualString.md) | Landing page or further web address, multilingual. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| agenda_item_category | 0..1 <br/> [String](String.md) | Category for grouped agenda items (e.g., introduction, by department, technical agenda items). <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| parent_agenda_item | 0..1 <br/> [String](String.md) | If needed, this slot builds a hierarchy of agenda items. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| has_resolution | 0..1 <br/> [Resolution](Resolution.md) | The resolution or decision taken on this agenda item. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| documents | * <br/> [Work](Work.md) | List of documents (FRBR Works) linked to the entity. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| date_begin_actual | 0..1 <br/> [Date](Date.md) | The actual start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_begin_actual | 0..1 <br/> [Datetime](Datetime.md) | The actual start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| date_begin_planned | 0..1 <br/> [Date](Date.md) | The planned start date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_begin_planned | 0..1 <br/> [Datetime](Datetime.md) | The planned start date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| date_end_actual | 0..1 <br/> [Date](Date.md) | The actual end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_end_actual | 0..1 <br/> [Datetime](Datetime.md) | The actual end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| date_end_planned | 0..1 <br/> [Date](Date.md) | The planned end date of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_end_planned | 0..1 <br/> [Datetime](Datetime.md) | The planned end date and time of an event or occurrence with time duration. <br/><br/>Inheritance: [IsEventWithDuration](IsEventWithDuration.md) |
| date_created | 0..1 <br/> [Date](Date.md) | The date when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was created. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | The date when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | The date and time when an entity was last modified. <br/><br/>Inheritance: [HasCreationModificationDates](HasCreationModificationDates.md) |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Protocol](Protocol.md) | [protocol_items](protocol_items.md) | range | [ProtocolItem](ProtocolItem.md) |



















</div>