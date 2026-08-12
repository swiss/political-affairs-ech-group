

## Klasse: Content 


_Der Inhalt eines Absatzes (akn:content). Enthält Block-Elemente: akn:p (Fliesstext), akn:blockList (Aufzählungen), akn:table. Wenn in einem akn:level, muss ein akn:mod-Element enthalten sein (FLX-HR-003)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| block_paragraphs | * <br/> [BlockParagraph](BlockParagraph.md) | Block-Absatz-Elemente (akn:p) innerhalb von Content. |
| block_lists | * <br/> [BlockList](BlockList.md) | Auflistungs-Elemente (akn:blockList) innerhalb von Content. |
| tables | * <br/> [Table](Table.md) | Tabellen-Elemente (akn:table) innerhalb von Content. |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Level](Level.md) | [content_ref](content_ref.md) | range | [Content](Content.md) |
| [Paragraph](Paragraph.md) | [content_ref](content_ref.md) | range | [Content](Content.md) |



















</div>