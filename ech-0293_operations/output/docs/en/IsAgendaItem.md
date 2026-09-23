

## Class: IsAgendaItem 


_A mixin class that provides the elements of an agenda item: designation, type, actors, the link to the affair, state, resolution and attached texts and documents. It is used by the planned agenda item (AgendaItem) and by the recorded one (ProtocolItem), so that both carry the same elements without one depending on the other._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| parent_meeting | 0..1 <br/> [String](String.md) | Identifier of the meeting this record belongs to. On a meeting it names the superordinate meeting; on an agenda item, voting, election, speech or protocol it names the meeting in which the record arose.  |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](AgendaItemTypeEnum.md) | Type of agenda item, distinguishing individual items from groups.  |
| agenda_item_number | 0..1 <br/> [String](String.md) | Number of the agenda item on the agenda, e.g. "2.1" or "3" (string type to also support roman numerals).  |
| agenda_item_position | 0..1 <br/> [Integer](Integer.md) | Integer position of the agenda item in the meeting sequence, used for sorting and display.  |
| leading_actor_id | 0..1 <br/> [String](String.md) | The leading department for the agenda item.  |
| speaking_actor_id | 0..1 <br/> [String](String.md) | The speaker or head of the department for the agenda item.  |
| agenda_item_title | * <br/> [MultilingualString](MultilingualString.md) | Title of the agenda item.  |
| affair_id | 0..1 <br/> [String](String.md) | Identifier of the affair (eCH-0295) the record refers to. Administrative agenda items (e.g. approval of the minutes) have no affair. An affair usually runs through several agenda items — in legislation, for instance, the debate on entering into the matter, the detailed deliberation, the final vote and, where applicable, the procedure for resolving differences between the chambers.  |
| agenda_item_description | * <br/> [MultilingualString](MultilingualString.md) | Subtitle or detailed description of the agenda item.  |
| state_id | 0..1 <br/> [String](String.md) | State identifier of the agenda item (reference to a state enumeration or a custom state), e.g. pending (not yet dealt with), in_progress, completed, postponed (to a later meeting) or withdrawn.  |
| state_name | 0..1 <br/> [String](String.md) | Diverging, free-text status designation, where the status enumeration does not suffice.  |
| landing_page | 0..1 <br/> [String](String.md) | URL providing further information.  |
| url | * <br/> [MultilingualString](MultilingualString.md) | Landing page or further web address, multilingual.  |
| agenda_item_category | 0..1 <br/> [String](String.md) | Free categorisation of the agenda item by content or grouping, e.g. "Gesetzgebung", "Budget und Finanzen", "Interpellationen und Anfragen", "Wahlen", by department, or introductory and technical items. The categorisation is not standardised and may vary between federal units.  |
| parent_agenda_item | 0..1 <br/> [String](String.md) | Identifier of the agenda item this record belongs to. On an agenda item it builds a hierarchy of agenda items — e.g. an item group "Gesetzesberatungen" with the sub-items "Energiegesetz (Detailberatung)" and "Energiegesetz (Schlussabstimmung)"; on a speech it names the agenda item under which the speech was given.  |
| has_resolution | 0..1 <br/> [Resolution](Resolution.md) | The formal decision taken on this agenda item, e.g. the adoption of the energy law. The underlying voting with its vote ratio is recorded separately as a Voting.  |
| joint_debates | * <br/> [JointDebate](JointDebate.md) | Joint debates attached to this record: on an agenda item, the debates in which it is deliberated together with other agenda items; on a meeting or a session, the joint debates held within it.  |
| text_segments | * <br/> [TextSegment](TextSegment.md) | Collection of text segments (e.g. verbatim protocol).  |
| documents | * <br/> [Work](Work.md) | Documents on the agenda item as FRBR Works, e.g. dispatches and reports, motions and amendments.  |



### Mixin Usage

[AgendaItem](AgendaItem.md), [ProtocolItem](ProtocolItem.md)





















</div>