

## Klasse: ProtocolItem 


_Ein Traktandum, wie es im Protokoll tatsächlich festgehalten wurde. Es führt über das Mixin IsAgendaItem dieselben Elemente wie AgendaItem, ist aber eine eigenständige Klasse: Das Protokollierte ist kein Sonderfall des Geplanten. Es entsteht unabhängig und kann Traktanden enthalten, die nie traktandiert waren, so wie die Traktandenliste Punkte enthalten kann, die nie behandelt wurden._




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
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](AgendaItemTypeEnum.md) | Art des Traktandums, unterscheidet Einzeltraktanden von Traktandengruppen. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| agenda_item_number | 0..1 <br/> [String](String.md) | Nummer des Traktandums auf der Traktandenliste, z.B. „2.1“ oder „3“ (Zeichenkette, damit auch römische Ziffern möglich sind). <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| agenda_item_position | 0..1 <br/> [Integer](Integer.md) | Ganzzahlige Position des Traktandums im Sitzungsablauf, massgebend für Sortierung und Darstellung. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| leading_actor_id | 0..1 <br/> [String](String.md) | Das federführende Departement für das Traktandum. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| speaking_actor_id | 0..1 <br/> [String](String.md) | Der Sprecher oder die Sprecherin bzw. die Departementsvorsteherin oder der Departementsvorsteher für das Traktandum. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| agenda_item_title | * <br/> [MultilingualString](MultilingualString.md) | Titel des Traktandums. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| affair_id | 0..1 <br/> [String](String.md) | Identifikator des Geschäfts (eCH-0295), auf das sich der Eintrag bezieht. Administrative Traktanden (z.B. Genehmigung des Protokolls) haben kein Geschäft. Ein Geschäft durchläuft in der Regel mehrere Traktanden — in der Gesetzgebung etwa Eintretensdebatte, Detailberatung, Schlussabstimmung und gegebenenfalls die Differenzbereinigung zwischen den Räten. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| agenda_item_description | * <br/> [MultilingualString](MultilingualString.md) | Untertitel oder ausführliche Beschreibung des Traktandums. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| state_id | 0..1 <br/> [String](String.md) | Zustands-Identifikator des Traktandums (Verweis auf ein Status-Enum oder auf einen eigenen Zustand), z.B. pending (noch nicht behandelt), in_progress (in Beratung), completed (abgeschlossen), postponed (auf eine spätere Sitzung vertagt) oder withdrawn (zurückgezogen). <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| state_name | 0..1 <br/> [String](String.md) | Abweichende, freitextliche Statusbezeichnung, wo die Status-Aufzählung nicht genügt. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| landing_page | 0..1 <br/> [String](String.md) | URL mit weiteren Informationen. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| url | * <br/> [MultilingualString](MultilingualString.md) | Landing Page oder weiterführende Webadresse, mehrsprachig. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| agenda_item_category | 0..1 <br/> [String](String.md) | Freie Kategorisierung des Traktandums nach Inhalt oder Gruppierung, z.B. „Gesetzgebung“, „Budget und Finanzen“, „Interpellationen und Anfragen“, „Wahlen“, nach Departement oder einleitende und technische Traktanden. Die Kategorisierung ist nicht standardisiert und kann je nach Föderaleinheit variieren. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| parent_agenda_item | 0..1 <br/> [String](String.md) | Identifikator des Traktandums, zu dem dieser Eintrag gehört. Bei einem Traktandum bildet er eine Hierarchie von Traktanden — z.B. eine Traktandengruppe „Gesetzesberatungen“ mit den Untertraktanden „Energiegesetz (Detailberatung)“ und „Energiegesetz (Schlussabstimmung)“; bei einer Wortmeldung bezeichnet er das Traktandum, unter dem sie erfolgte. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| has_resolution | 0..1 <br/> [Resolution](Resolution.md) | Der formale Beschluss zu diesem Traktandum, z.B. die Annahme des Energiegesetzes. Die zugrunde liegende Abstimmung mit dem Stimmenverhältnis wird separat als Voting erfasst. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| joint_debates | * <br/> [JointDebate](JointDebate.md) | An diesem Eintrag angehängte gemeinsame Beratungen: bei einem Traktandum die Beratungen, in denen es zusammen mit anderen Traktanden behandelt wird; bei einer Sitzung oder Session die darin geführten gemeinsamen Beratungen. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| text_segments | * <br/> [TextSegment](TextSegment.md) | Sammlung von Textsegmenten (z.B. Wortprotokoll). <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |
| documents | * <br/> [Work](Work.md) | Unterlagen zum Traktandum als FRBR-Works, z.B. Botschaften und Berichte, Anträge und Änderungsanträge. <br/><br/>Vererbung: [IsAgendaItem](IsAgendaItem.md) |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Protocol](Protocol.md) | [protocol_items](protocol_items.md) | range | [ProtocolItem](ProtocolItem.md) |
| [Voting](Voting.md) | [parent_protocol_item](parent_protocol_item.md) | range | [ProtocolItem](ProtocolItem.md) |
| [Election](Election.md) | [parent_protocol_item](parent_protocol_item.md) | range | [ProtocolItem](ProtocolItem.md) |



















</div>