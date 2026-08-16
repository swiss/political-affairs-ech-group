

## Klasse: Block 


_Ein generischer Block (akn:block), dessen @name den Zweck nennt; trägt gemischten Inhalt._



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| block_name | 0..1 <br/> [BlockNameEnum](BlockNameEnum.md) | Zweck des Blocks (akn:block/@name). |
| inline_content | * <br/> [InlineElement](InlineElement.md) | Geordneter gemischter Inhalt: eine Folge aus Textabschnitten und Inline-Markup-Elementen (InlineElement-Subklassen). Die Dokumentreihenfolge wird durch die Listenreihenfolge bewahrt.  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Container](Container.md) | [blocks](blocks.md) | range | [Block](Block.md) |



















</div>