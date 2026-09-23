

## Klasse: ProtocolItem 


_Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde. Es führt über den Mixin IsAgendaItem dieselben Elemente wie AgendaItem, ist aber eine eigenständige Klasse: Das Protokollierte ist kein Sonderfall des Geplanten._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| date_begin_actual | 0..1 <br/> [Date](Date.md) | Das tatsächliche Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_begin_actual | 0..1 <br/> [Datetime](Datetime.md) | Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](IsEventWithDuration.md) |
| date_begin_planned | 0..1 <br/> [Date](Date.md) | Das geplante Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_begin_planned | 0..1 <br/> [Datetime](Datetime.md) | Das geplante Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](IsEventWithDuration.md) |
| date_end_actual | 0..1 <br/> [Date](Date.md) | Das tatsächliche Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_end_actual | 0..1 <br/> [Datetime](Datetime.md) | Das tatsächliche Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](IsEventWithDuration.md) |
| date_end_planned | 0..1 <br/> [Date](Date.md) | Das geplante Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](IsEventWithDuration.md) |
| datetime_end_planned | 0..1 <br/> [Datetime](Datetime.md) | Das geplante Enddatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer. <br/><br/>Vererbung: [IsEventWithDuration](IsEventWithDuration.md) |
| date_created | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_created | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität erstellt wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| date_modified | 0..1 <br/> [Date](Date.md) | Das Datum, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| datetime_modified | 0..1 <br/> [Datetime](Datetime.md) | Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde. <br/><br/>Vererbung: [HasCreationModificationDates](HasCreationModificationDates.md) |
| parent_meeting | 0..1 <br/> [String](String.md) | Identifikator der Sitzung, zu der dieser Eintrag gehört. Bei einer Sitzung bezeichnet er die übergeordnete Sitzung, bei Traktandum, Abstimmung, Wahl, Wortmeldung oder Protokoll die Sitzung, in der der Eintrag entstanden ist. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](AgendaItemTypeEnum.md) | Art des Traktandums, unterscheidet Einzeltraktanden von Traktandengruppen. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| agenda_item_number | 0..1 <br/> [String](String.md) | Laufnummer des Traktandums (String-Typ zur Unterstützung römischer Ziffern). <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| agenda_item_position | 0..1 <br/> [Integer](Integer.md) | Ganzzahlige Position des Traktandums in der Sitzungsreihenfolge. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| leading_actor_id | 0..1 <br/> [String](String.md) | Das federführende Departement für das Traktandum. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| speaking_actor_id | 0..1 <br/> [String](String.md) | Der Sprecher oder die Sprecherin bzw. die Departementsvorsteherin oder der Departementsvorsteher für das Traktandum. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| agenda_item_title | * <br/> [MultilingualString](MultilingualString.md) | Titel des Traktandums. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| affair_id | 0..1 <br/> [String](String.md) | Die Verbindung zu den Geschäften des Traktandums. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| agenda_item_description | * <br/> [MultilingualString](MultilingualString.md) | Untertitel oder ausführliche Beschreibung des Traktandums. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| state_id | 0..1 <br/> [String](String.md) | Zustands-Identifikator (Verweis auf das Status-Enum oder auf einen eigenen Zustand). <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| state_name | 0..1 <br/> [String](String.md) | Benutzerdefinierte Zustandsbeschreibung für die Sitzung. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| landing_page | 0..1 <br/> [String](String.md) | URL mit weiteren Informationen. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| url | * <br/> [MultilingualString](MultilingualString.md) | Landing Page oder weiterführende Webadresse, mehrsprachig. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| agenda_item_category | 0..1 <br/> [String](String.md) | Kategorie für gruppierte Traktanden (z.B. Einführung, nach Departement, technische Traktanden). <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| parent_agenda_item | 0..1 <br/> [String](String.md) | Identifikator des Traktandums, zu dem dieser Eintrag gehört. Bei einem Traktandum baut er eine Hierarchie von Traktanden auf, bei Abstimmung, Wahl oder Wortmeldung bezeichnet er das Traktandum, unter dem der Eintrag behandelt wurde. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| has_resolution | 0..1 <br/> [Resolution](Resolution.md) | Die Resolution oder Entscheidung zu diesem Traktandum. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| text_segments | * <br/> [TextSegment](TextSegment.md) | Sammlung von Textsegmenten (z.B. Wortprotokoll). <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| documents | * <br/> [Work](Work.md) | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Protocol](Protocol.md) | [protocol_items](protocol_items.md) | range | [ProtocolItem](ProtocolItem.md) |
| [Voting](Voting.md) | [parent_protocol_item](parent_protocol_item.md) | range | [ProtocolItem](ProtocolItem.md) |
| [Election](Election.md) | [parent_protocol_item](parent_protocol_item.md) | range | [ProtocolItem](ProtocolItem.md) |



















</div>