

## Klasse: TextSegment 


_Ein Textsegment wie Querverweise oder Zwischentitel. Textsegmente werden am Protokoll, an einer Wortmeldung oder an einem Traktandum geführt (geplantes AgendaItem oder protokolliertes ProtocolItem)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Lokaler Identifikator. Bspw. eine UUID aus dem Ratsinformationssystem. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Eine eindeutige, global gültige URI für die Entität. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q813067 für Beat Jans. <br/><br/>Vererbung: [HasIdentification](HasIdentification.md) |
| text | 1 <br/> [String](String.md) | Textinhalt des Elements.  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [IsAgendaItem](IsAgendaItem.md) | [text_segments](text_segments.md) | range | [TextSegment](TextSegment.md) |
| [AgendaItem](AgendaItem.md) | [text_segments](text_segments.md) | range | [TextSegment](TextSegment.md) |
| [Protocol](Protocol.md) | [text_segments](text_segments.md) | range | [TextSegment](TextSegment.md) |
| [ProtocolItem](ProtocolItem.md) | [text_segments](text_segments.md) | range | [TextSegment](TextSegment.md) |



















</div>