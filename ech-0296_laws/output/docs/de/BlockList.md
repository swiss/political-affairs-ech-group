

## Klasse: BlockList 


_Eine Auflistung von nummerierten oder buchstabierten Punkten (akn:blockList), optional eingeleitet durch ein akn:listIntroduction-Element._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| style | 0..1 <br/> [String](String.md) | Darstellungsangabe des Elements (@style). |
| eId | 0..1 <br/> [EIdType](EIdType.md) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| list_introduction | 0..1 <br/> [MixedText](MixedText.md) | Optionaler Einleitungstext vor einer Auflistung (akn:listIntroduction). |
| items | * <br/> [BlockListItem](BlockListItem.md) | Punkte einer Auflistung (akn:item). |
| element_type | 0..1 <br/> [String](String.md) | Typ-Diskriminator für die konkrete Unterklasse einer abstrakten Basis: InlineElement oder BlockElement. <br/><br/>Vererbung: [BlockElement](BlockElement.md) |






















</div>