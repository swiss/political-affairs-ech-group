

## Klasse: BlockParagraph 


_Ein Fliesstext-Absatz in Content (akn:p). Kann gemischten Inhalt mit Inline-Markup enthalten (XmlContent-Typ). Hinweis: akn:br ist hier nicht erlaubt, nur in Überschriften (FLX-TXT-001)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| inline_content | * <br/> [InlineElement](InlineElement.md) | Geordneter gemischter Inhalt: eine Folge aus Textabschnitten und Inline-Markup-Elementen (InlineElement-Subklassen). Die Dokumentreihenfolge wird durch die Listenreihenfolge bewahrt.  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Preamble](Preamble.md) | [block_paragraphs](block_paragraphs.md) | range | [BlockParagraph](BlockParagraph.md) |
| [Content](Content.md) | [block_paragraphs](block_paragraphs.md) | range | [BlockParagraph](BlockParagraph.md) |
| [BlockListItem](BlockListItem.md) | [block_paragraphs](block_paragraphs.md) | range | [BlockParagraph](BlockParagraph.md) |
| [TableCell](TableCell.md) | [block_paragraphs](block_paragraphs.md) | range | [BlockParagraph](BlockParagraph.md) |
| [AuthorialNote](AuthorialNote.md) | [block_paragraphs](block_paragraphs.md) | range | [BlockParagraph](BlockParagraph.md) |



















</div>