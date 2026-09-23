

## Class: ProtocolItem 


_An agenda item as actually recorded in the protocol. It carries the same elements as AgendaItem through the IsAgendaItem mixin, but is a class in its own right: the record is not a special case of the plan. It arises independently and may contain items that were never put on the agenda, just as the agenda may contain items that were never dealt with._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q813067 for Beat Jans. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
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
| parent_meeting | 0..1 <br/> [String](String.md) | Identifier of the meeting this record belongs to. On a meeting it names the superordinate meeting; on an agenda item, voting, election, speech or protocol it names the meeting in which the record arose. <br/><br/>Inheritance: [IsAgendaItem](IsAgendaItem.md) |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](AgendaItemTypeEnum.md) | Type of agenda item, distinguishing individual items from groups. <br/><br/>Inheritance: [IsAgendaItem](IsAgendaItem.md) |
| agenda_item_number | 0..1 <br/> [String](String.md) | Number of the agenda item on the agenda, e.g. "2.1" or "3" (string type to also support roman numerals). <br/><br/>Inheritance: [IsAgendaItem](IsAgendaItem.md) |
| agenda_item_position | 0..1 <br/> [Integer](Integer.md) | Integer position of the agenda item in the meeting sequence, used for sorting and display. <br/><br/>Inheritance: [IsAgendaItem](IsAgendaItem.md) |
| leading_actor_id | 0..1 <br/> [String](String.md) | The leading department for the agenda item. <br/><br/>Inheritance: [IsAgendaItem](IsAgendaItem.md) |
| speaking_actor_id | 0..1 <br/> [String](String.md) | The speaker or head of the department for the agenda item. <br/><br/>Inheritance: [IsAgendaItem](IsAgendaItem.md) |
| agenda_item_title | * <br/> [MultilingualString](MultilingualString.md) | Title of the agenda item. <br/><br/>Inheritance: [IsAgendaItem](IsAgendaItem.md) |
| affair_id | 0..1 <br/> [String](String.md) | Identifier of the affair (eCH-0295) the record refers to. Administrative agenda items (e.g. approval of the minutes) have no affair. An affair usually runs through several agenda items — in legislation, for instance, the debate on entering into the matter, the detailed deliberation, the final vote and, where applicable, the procedure for resolving differences between the chambers. <br/><br/>Inheritance: [IsAgendaItem](IsAgendaItem.md) |
| agenda_item_description | * <br/> [MultilingualString](MultilingualString.md) | Subtitle or detailed description of the agenda item. <br/><br/>Inheritance: [IsAgendaItem](IsAgendaItem.md) |
| state_id | 0..1 <br/> [String](String.md) | State identifier of the agenda item (reference to a state enumeration or a custom state), e.g. pending (not yet dealt with), in_progress, completed, postponed (to a later meeting) or withdrawn. <br/><br/>Inheritance: [IsAgendaItem](IsAgendaItem.md) |
| state_name | 0..1 <br/> [String](String.md) | Diverging, free-text status designation, where the status enumeration does not suffice. <br/><br/>Inheritance: [IsAgendaItem](IsAgendaItem.md) |
| landing_page | 0..1 <br/> [String](String.md) | URL providing further information. <br/><br/>Inheritance: [IsAgendaItem](IsAgendaItem.md) |
| url | * <br/> [MultilingualString](MultilingualString.md) | Landing page or further web address, multilingual. <br/><br/>Inheritance: [IsAgendaItem](IsAgendaItem.md) |
| agenda_item_category | 0..1 <br/> [String](String.md) | Free categorisation of the agenda item by content or grouping, e.g. "Gesetzgebung", "Budget und Finanzen", "Interpellationen und Anfragen", "Wahlen", by department, or introductory and technical items. The categorisation is not standardised and may vary between federal units. <br/><br/>Inheritance: [IsAgendaItem](IsAgendaItem.md) |
| parent_agenda_item | 0..1 <br/> [String](String.md) | Identifier of the agenda item this record belongs to. On an agenda item it builds a hierarchy of agenda items — e.g. an item group "Gesetzesberatungen" with the sub-items "Energiegesetz (Detailberatung)" and "Energiegesetz (Schlussabstimmung)"; on a speech it names the agenda item under which the speech was given. <br/><br/>Inheritance: [IsAgendaItem](IsAgendaItem.md) |
| has_resolution | 0..1 <br/> [Resolution](Resolution.md) | The formal decision taken on this agenda item, e.g. the adoption of the energy law. The underlying voting with its vote ratio is recorded separately as a Voting. <br/><br/>Inheritance: [IsAgendaItem](IsAgendaItem.md) |
| joint_debates | * <br/> [JointDebate](JointDebate.md) | Joint debates attached to this record: on an agenda item, the debates in which it is deliberated together with other agenda items; on a meeting or a session, the joint debates held within it. <br/><br/>Inheritance: [IsAgendaItem](IsAgendaItem.md) |
| text_segments | * <br/> [TextSegment](TextSegment.md) | Collection of text segments (e.g. verbatim protocol). <br/><br/>Inheritance: [IsAgendaItem](IsAgendaItem.md) |
| documents | * <br/> [Work](Work.md) | Documents on the agenda item as FRBR Works, e.g. dispatches and reports, motions and amendments. <br/><br/>Inheritance: [IsAgendaItem](IsAgendaItem.md) |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Protocol](Protocol.md) | [protocol_items](protocol_items.md) | range | [ProtocolItem](ProtocolItem.md) |
| [Voting](Voting.md) | [parent_protocol_item](parent_protocol_item.md) | range | [ProtocolItem](ProtocolItem.md) |
| [Election](Election.md) | [parent_protocol_item](parent_protocol_item.md) | range | [ProtocolItem](ProtocolItem.md) |



















</div>