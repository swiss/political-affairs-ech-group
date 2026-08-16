

## Klasse: Content 


_Der Inhalt eines Absatzes (akn:content). Enthält Block-Elemente: akn:p (Fliesstext), akn:blockList (Aufzählungen), akn:table. Wenn in einem akn:level, muss ein akn:mod-Element enthalten sein (FLX-HR-003)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| content_blocks | * <br/> [BlockElement](BlockElement.md) | Blockinhalt in Lesereihenfolge: Absätze, Aufzählungen und Tabellen, wie sie im Dokument aufeinanderfolgen.  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Level](Level.md) | [content_ref](content_ref.md) | range | [Content](Content.md) |
| [Paragraph](Paragraph.md) | [content_ref](content_ref.md) | range | [Content](Content.md) |
| [MainBody](MainBody.md) | [content_ref](content_ref.md) | range | [Content](Content.md) |














### Beispiele
#### Beispiel Content: sr101 2 1

```yaml
content_ref:
  content_blocks:
  - element_type: BlockParagraph
    inline_content:
    - element_type: TextRun
      text: >-
        Staatliches Handeln muss im öffentlichen Interesse liegen und verhältnismässig
        sein.

```
#### Beispiel Content: sr101 4 1

```yaml
content_ref:
  content_blocks:
  - element_type: BlockParagraph
    inline_content:
    - element_type: TextRun
      text: Bund und Kantone beachten das Völkerrecht.

```
#### Beispiel Content: sr101 1 1

```yaml
content_ref:
  content_blocks:
  - element_type: BlockParagraph
    inline_content:
    - element_type: TextRun
      text: >-
        Jede Person nimmt Verantwortung für sich selber wahr und trägt nach ihren
        Kräften zur Bewältigung der Aufgaben in Staat und Gesellschaft bei.

```
#### Beispiel Content: sr101 3 1

```yaml
content_ref:
  content_blocks:
  - element_type: BlockParagraph
    inline_content:
    - element_type: TextRun
      text: Staatliche Organe und Private handeln nach Treu und Glauben.

```






</div>