

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














### Beispiele
#### Beispiel BlockParagraph: bgoe excerpt 1 1

```yaml
block_paragraphs:
- inline_content:
  - element_type: TextRun
    text: >-
      Dieses Gesetz soll die Transparenz über den Auftrag, die Organisation und die
      Tätigkeit der Verwaltung fördern. Zu diesem Zweck trägt es zur Information der
      Öffentlichkeit bei, indem es den Zugang zu amtlichen Dokumenten gewährleistet.

```
#### Beispiel BlockParagraph: sr101 excerpt 1 1

```yaml
block_paragraphs:
- inline_content:
  - element_type: TextRun
    text: >-
      Das Schweizervolk und die Kantone Zürich, Bern, Luzern, Uri, Schwyz, Obwalden
      und Nidwalden, Glarus, Zug, Freiburg, Solothurn, Basel-Stadt und Basel-Landschaft,
      Schaffhausen, Appenzell Ausserrhoden und Appenzell Innerrhoden, St. Gallen,
      Graubünden, Aargau, Thurgau, Tessin, Waadt, Wallis, Neuenburg, Genf und Jura
      bilden die Schweizerische Eidgenossenschaft.

```






</div>