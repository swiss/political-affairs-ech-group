

## Klasse: IsAgendaItem 


_Eine Mixin-Klasse, welche die Elemente eines Traktandums bereitstellt: Bezeichnung, Art, Akteure, Bezug zum Geschäft, Status, Beschluss sowie angehängte Texte und Dokumente. Sie wird vom geplanten Traktandum (AgendaItem) und vom protokollierten (ProtocolItem) verwendet, damit beide dieselben Elemente führen, ohne dass das eine vom anderen abhängt._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| parent_meeting | 0..1 <br/> [String](String.md) | Identifikator der Sitzung, zu der dieser Eintrag gehört. Bei einer Sitzung bezeichnet er die übergeordnete Sitzung, bei Traktandum, Abstimmung, Wahl, Wortmeldung oder Protokoll die Sitzung, in der der Eintrag entstanden ist.  |
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](AgendaItemTypeEnum.md) | Art des Traktandums, unterscheidet Einzeltraktanden von Traktandengruppen.  |
| agenda_item_number | 0..1 <br/> [String](String.md) | Laufnummer des Traktandums (String-Typ zur Unterstützung römischer Ziffern).  |
| agenda_item_position | 0..1 <br/> [Integer](Integer.md) | Ganzzahlige Position des Traktandums in der Sitzungsreihenfolge.  |
| leading_actor_id | 0..1 <br/> [String](String.md) | Das federführende Departement für das Traktandum.  |
| speaking_actor_id | 0..1 <br/> [String](String.md) | Der Sprecher oder die Sprecherin bzw. die Departementsvorsteherin oder der Departementsvorsteher für das Traktandum.  |
| agenda_item_title | * <br/> [MultilingualString](MultilingualString.md) | Titel des Traktandums.  |
| affair_id | 0..1 <br/> [String](String.md) | Die Verbindung zu den Geschäften des Traktandums.  |
| agenda_item_description | * <br/> [MultilingualString](MultilingualString.md) | Untertitel oder ausführliche Beschreibung des Traktandums.  |
| state_id | 0..1 <br/> [String](String.md) | Zustands-Identifikator (Verweis auf das Status-Enum oder auf einen eigenen Zustand).  |
| state_name | 0..1 <br/> [String](String.md) | Benutzerdefinierte Zustandsbeschreibung für die Sitzung.  |
| landing_page | 0..1 <br/> [String](String.md) | URL mit weiteren Informationen.  |
| url | * <br/> [MultilingualString](MultilingualString.md) | Landing Page oder weiterführende Webadresse, mehrsprachig.  |
| agenda_item_category | 0..1 <br/> [String](String.md) | Kategorie für gruppierte Traktanden (z.B. Einführung, nach Departement, technische Traktanden).  |
| parent_agenda_item | 0..1 <br/> [String](String.md) | Identifikator des Traktandums, zu dem dieser Eintrag gehört. Bei einem Traktandum baut er eine Hierarchie von Traktanden auf, bei Abstimmung, Wahl oder Wortmeldung bezeichnet er das Traktandum, unter dem der Eintrag behandelt wurde.  |
| has_resolution | 0..1 <br/> [Resolution](Resolution.md) | Die Resolution oder Entscheidung zu diesem Traktandum.  |
| text_segments | * <br/> [TextSegment](TextSegment.md) | Sammlung von Textsegmenten (z.B. Wortprotokoll).  |
| documents | * <br/> [Work](Work.md) | Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.  |



### Mixin-Verwendung

[AgendaItem](AgendaItem.md), [ProtocolItem](ProtocolItem.md)





















</div>