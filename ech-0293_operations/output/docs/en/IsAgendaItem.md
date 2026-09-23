

## Class: IsAgendaItem 


_A mixin class that provides the elements of an agenda item: designation, type, actors, the link to the affair, state, resolution and attached texts and documents. It is used by the planned agenda item (AgendaItem) and by the recorded one (ProtocolItem), so that both carry the same elements without one depending on the other._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| parent_meeting | 0..1 <br/> [String](String.md) | The linked meeting ID that groups the current meeting.  |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](AgendaItemTypeEnum.md) | Type of agenda item, distinguishing individual items from groups.  |
| agenda_item_number | 0..1 <br/> [String](String.md) | Sequential number of the agenda item (string type to support roman numerals).  |
| agenda_item_position | 0..1 <br/> [Integer](Integer.md) | Integer position of the agenda item in the meeting sequence.  |
| leading_actor_id | 0..1 <br/> [String](String.md) | The leading department for the agenda item.  |
| speaking_actor_id | 0..1 <br/> [String](String.md) | The speaker or head of the department for the agenda item.  |
| agenda_item_title | * <br/> [MultilingualString](MultilingualString.md) | Title of the agenda item.  |
| affair_id | 0..1 <br/> [String](String.md) | The connection to the affairs (business items) of the agenda item.  |
| agenda_item_description | * <br/> [MultilingualString](MultilingualString.md) | Subtitle or detailed description of the agenda item.  |
| state_id | 0..1 <br/> [String](String.md) | State identifier (reference to state enum or custom state).  |
| state_name | 0..1 <br/> [String](String.md) | Custom state description for the meeting.  |
| landing_page | 0..1 <br/> [String](String.md) | URL providing further information.  |
| url | * <br/> [MultilingualString](MultilingualString.md) | Landing page or further web address, multilingual.  |
| agenda_item_category | 0..1 <br/> [String](String.md) | Category for grouped agenda items (e.g., introduction, by department, technical agenda items).  |
| parent_agenda_item | 0..1 <br/> [String](String.md) | If needed, this slot builds a hierarchy of agenda items.  |
| has_resolution | 0..1 <br/> [Resolution](Resolution.md) | The resolution or decision taken on this agenda item.  |
| text_segments | * <br/> [TextSegment](TextSegment.md) | Collection of text segments (e.g. verbatim protocol).  |
| documents | * <br/> [Work](Work.md) | List of documents (FRBR Works) linked to the entity.  |



### Mixin Usage

[AgendaItem](AgendaItem.md), [ProtocolItem](ProtocolItem.md)





















</div>