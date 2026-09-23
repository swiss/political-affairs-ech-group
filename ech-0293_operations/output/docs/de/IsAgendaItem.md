

## Klasse: IsAgendaItem 


_Eine Mixin-Klasse, welche die Elemente eines Traktandums bereitstellt: Bezeichnung, Art, Akteure, Bezug zum Geschäft, Status, Beschluss sowie angehängte Texte und Dokumente. Sie wird vom geplanten Traktandum (AgendaItem) und vom protokollierten (ProtocolItem) verwendet, damit beide dieselben Elemente führen, ohne dass das eine vom anderen abhängt._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| agenda_item_type | 0..1 <br/> [AgendaItemTypeEnum](AgendaItemTypeEnum.md) | Art des Traktandums, unterscheidet Einzeltraktanden von Traktandengruppen.  |
| agenda_item_number | 0..1 <br/> [String](String.md) | Nummer des Traktandums auf der Traktandenliste, z.B. „2.1“ oder „3“ (Zeichenkette, damit auch römische Ziffern möglich sind).  |
| agenda_item_position | 0..1 <br/> [Integer](Integer.md) | Ganzzahlige Position des Traktandums im Sitzungsablauf, massgebend für Sortierung und Darstellung.  |
| leading_actor_id | 0..1 <br/> [String](String.md) | Das federführende Departement für das Traktandum.  |
| speaking_actor_id | 0..1 <br/> [String](String.md) | Der Sprecher oder die Sprecherin bzw. die Departementsvorsteherin oder der Departementsvorsteher für das Traktandum.  |
| agenda_item_title | * <br/> [MultilingualString](MultilingualString.md) | Titel des Traktandums.  |
| affair_id | 0..1 <br/> [String](String.md) | Identifikator des Geschäfts (eCH-0295), auf das sich der Eintrag bezieht. Administrative Traktanden (z.B. Genehmigung des Protokolls) haben kein Geschäft. Ein Geschäft durchläuft in der Regel mehrere Traktanden — in der Gesetzgebung etwa Eintretensdebatte, Detailberatung, Schlussabstimmung und gegebenenfalls die Differenzbereinigung zwischen den Räten.  |
| agenda_item_description | * <br/> [MultilingualString](MultilingualString.md) | Untertitel oder ausführliche Beschreibung des Traktandums.  |
| state_id | 0..1 <br/> [String](String.md) | Zustands-Identifikator des Traktandums (Verweis auf ein Status-Enum oder auf einen eigenen Zustand), z.B. pending (noch nicht behandelt), in_progress (in Beratung), completed (abgeschlossen), postponed (auf eine spätere Sitzung vertagt) oder withdrawn (zurückgezogen).  |
| state_name | 0..1 <br/> [String](String.md) | Abweichende, freitextliche Statusbezeichnung, wo die Status-Aufzählung nicht genügt.  |
| landing_page | 0..1 <br/> [String](String.md) | URL mit weiteren Informationen.  |
| url | * <br/> [MultilingualString](MultilingualString.md) | Landing Page oder weiterführende Webadresse, mehrsprachig.  |
| agenda_item_category | 0..1 <br/> [String](String.md) | Freie Kategorisierung des Traktandums nach Inhalt oder Gruppierung, z.B. „Gesetzgebung“, „Budget und Finanzen“, „Interpellationen und Anfragen“, „Wahlen“, nach Departement oder einleitende und technische Traktanden. Die Kategorisierung ist nicht standardisiert und kann je nach Föderaleinheit variieren.  |
| parent_agenda_item | 0..1 <br/> [String](String.md) | Identifikator des Traktandums, zu dem dieser Eintrag gehört. Bei einem Traktandum bildet er eine Hierarchie von Traktanden — z.B. eine Traktandengruppe „Gesetzesberatungen“ mit den Untertraktanden „Energiegesetz (Detailberatung)“ und „Energiegesetz (Schlussabstimmung)“; bei einer Wortmeldung bezeichnet er das Traktandum, unter dem sie erfolgte.  |
| has_resolution | 0..1 <br/> [Resolution](Resolution.md) | Der formale Beschluss zu diesem Traktandum, z.B. die Annahme des Energiegesetzes. Die zugrunde liegende Abstimmung mit dem Stimmenverhältnis wird separat als Voting erfasst.  |
| joint_debates | * <br/> [JointDebate](JointDebate.md) | An diesem Eintrag angehängte gemeinsame Beratungen: bei einem Traktandum die Beratungen, in denen es zusammen mit anderen Traktanden behandelt wird; bei einer Sitzung oder Session die darin geführten gemeinsamen Beratungen.  |
| text_segments | * <br/> [TextSegment](TextSegment.md) | Sammlung von Textsegmenten (z.B. Wortprotokoll).  |
| documents | * <br/> [Work](Work.md) | Unterlagen zum Traktandum als FRBR-Works, z.B. Botschaften und Berichte, Anträge und Änderungsanträge.  |



### Mixin-Verwendung

[AgendaItem](AgendaItem.md), [ProtocolItem](ProtocolItem.md)





















</div>