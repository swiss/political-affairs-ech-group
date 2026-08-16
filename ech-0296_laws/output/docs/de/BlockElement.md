

## Klasse: BlockElement 


_Abstrakte Basis für ein Element auf Blockebene: die Absätze, Aufzählungen und Tabellen des Inhalts sowie Formel und Erwägungen des Vorspruchs._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| element_type | 0..1 <br/> [String](String.md) | Typ-Diskriminator für die konkrete Unterklasse einer abstrakten Basis: InlineElement oder BlockElement.  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Preamble](Preamble.md) | [content_blocks](content_blocks.md) | range | [BlockElement](BlockElement.md) |
| [Content](Content.md) | [content_blocks](content_blocks.md) | range | [BlockElement](BlockElement.md) |
| [BlockListItem](BlockListItem.md) | [content_blocks](content_blocks.md) | range | [BlockElement](BlockElement.md) |
| [TableCell](TableCell.md) | [content_blocks](content_blocks.md) | range | [BlockElement](BlockElement.md) |
| [AuthorialNote](AuthorialNote.md) | [content_blocks](content_blocks.md) | range | [BlockElement](BlockElement.md) |
| [MainBody](MainBody.md) | [content_blocks](content_blocks.md) | range | [BlockElement](BlockElement.md) |
| [Conclusions](Conclusions.md) | [content_blocks](content_blocks.md) | range | [BlockElement](BlockElement.md) |
| [Note](Note.md) | [content_blocks](content_blocks.md) | range | [BlockElement](BlockElement.md) |
| [Formula](Formula.md) | [content_blocks](content_blocks.md) | range | [BlockElement](BlockElement.md) |
| [Citation](Citation.md) | [content_blocks](content_blocks.md) | range | [BlockElement](BlockElement.md) |



















</div>