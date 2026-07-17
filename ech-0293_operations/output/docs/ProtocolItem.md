

## Class: ProtocolItem 


_[en] An agenda item as actually recorded in the protocol._

_[de] Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde._

__



<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| parent_meeting | 0..1 <br/> [String](String.md) | [en] The linked meeting ID that groups the current meeting. [de] Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](AgendaItemTypeEnum.md) | [en] Type of agenda item, distinguishing individual items from groups. [de] Art des Traktandums, unterscheidet Einzeltraktanden von Traktandengruppen. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| agenda_item_number | 0..1 <br/> [String](String.md) | [en] Sequential number of the agenda item (string type to support roman numerals). [de] Laufnummer des Traktandums (String-Typ zur Unterstützung römischer Ziffern). <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| agenda_item_position | 0..1 <br/> [Integer](Integer.md) | [en] Integer position of the agenda item in the meeting sequence. [de] Ganzzahlige Position des Traktandums in der Sitzungsreihenfolge. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| leading_actor_id | 0..1 <br/> [String](String.md) | [en] The leading department for the agenda item. [de] Das federführende Departement für den Tagesordnungspunkt. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| speaking_actor_id | 0..1 <br/> [String](String.md) | [en] The speaker or head of the department for the agenda item. [de] Der Sprecher oder Departementsvorsteher für den Tagesordnungspunkt. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| agenda_item_title | * <br/> [MultilingualString](MultilingualString.md) | [en] Title of the agenda item. [de] Titel des Traktandums. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| affair_id | 0..1 <br/> [String](String.md) | [en] The connection to the affairs (business items) of the agenda item. [de] Die Verbindung zu den Geschäften (Geschäftsgegenständen) des Tagesordnungspunkts. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| agenda_item_description | * <br/> [MultilingualString](MultilingualString.md) | [en] Subtitle or detailed description of the agenda item. [de] Untertitel oder ausführliche Beschreibung des Traktandums. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| state_id | 0..1 <br/> [String](String.md) | State identifier (reference to state enum or custom state)<br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| state_name | 0..1 <br/> [String](String.md) | [en] Custom state description for the meeting. [de] Benutzerdefinierte Zustandsbeschreibung für die Sitzung. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| landing_page | 0..1 <br/> [String](String.md) | [en] URL providing further information. [de] URL mit weiteren Informationen. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| url | * <br/> [MultilingualString](MultilingualString.md) | None<br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| agenda_item_category | 0..1 <br/> [String](String.md) | [en] Category for grouped agenda items (e.g., introduction, by department, technical agenda items). [de] Kategorie für gruppierte Traktanden (z.B. Einführung, nach Departement, technische Traktanden). <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| parent_agenda_item | 0..1 <br/> [String](String.md) | [en] If needed, this slot builds a hierarchy of agenda items. [de] Wenn erforderlich, baut dieser Slot eine Hierarchie von Tagesordnungspunkten auf. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| has_resolution | 0..1 <br/> [Resolution](Resolution.md) | [en] The resolutionor decision taken on this agenda item. [de] Die Resolution oder Entscheidung zu diesem Traktandum. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| documents | * <br/> [Work](Work.md) | [de] Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind. [en] List of documents (FRBR Works) linked to the entity. <br/><br/>Inheritance: [AgendaItem](AgendaItem.md) |
| local_id | 0..1 <br/> [String](String.md) | Local identifier. For example, a UUID from the council information system. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | A unique, globally valid URI for the entity. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | A URI that refers to a Wikidata entity, e.g. http://www.wikidata.org/entity/Q39 for Switzerland. <br/><br/>Inheritance: [HasIdentification](HasIdentification.md) |
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

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Protocol](Protocol.md) | [protocol_items](protocol_items.md) | range | [ProtocolItem](ProtocolItem.md) |



















</div>