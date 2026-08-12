

## Klasse: BlockList 


_Eine Auflistung von nummerierten oder buchstabierten Punkten (akn:blockList), optional eingeleitet durch ein akn:listIntroduction-Element._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 0..1 <br/> [EIdType](EIdType.md) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| list_introduction | 0..1 <br/> [MixedText](MixedText.md) | Optionaler Einleitungstext vor einer Auflistung (akn:listIntroduction). |
| items | * <br/> [BlockListItem](BlockListItem.md) | Punkte einer Auflistung (akn:item). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Content](Content.md) | [block_lists](block_lists.md) | range | [BlockList](BlockList.md) |
| [BlockListItem](BlockListItem.md) | [block_lists](block_lists.md) | range | [BlockList](BlockList.md) |
| [TableCell](TableCell.md) | [block_lists](block_lists.md) | range | [BlockList](BlockList.md) |



















</div>