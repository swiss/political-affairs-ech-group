

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
#### Beispiel Content: zh idg 2 1

```yaml
content_ref:
  content_blocks:
  - element_type: BlockParagraph
    inline_content:
    - element_type: TextRun
      text: >-
        In den folgenden Gesetzen wird der Ausdruck «besonders schützenswerte Personendaten»
        oder «besonders schützenswerte Daten» ersetzt durch den Ausdruck «besondere
        Personendaten»:
  - element_type: BlockList
    eId: title_9__art_42__para_2__content__blocklist_1
    items:
    - eId: title_9__art_42__para_2__content__blocklist_1__item_a
      content_blocks:
      - …
      num:
        inline_content:
        - …
    - eId: title_9__art_42__para_2__content__blocklist_1__item_b
      content_blocks:
      - …
      num:
        inline_content:
        - …

```
#### Beispiel Content: zh idg 4 1

```yaml
content_ref:
  content_blocks:
  - element_type: BlockParagraph
    inline_content:
    - element_type: TextRun
      text: >-
        Eignen sich Informationen für eine gewerbliche Nutzung, kann ein Entgelt erhoben
        werden, das sich nach dem Markt richtet.

```
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
#### Beispiel Content: zh idg 1 1

```yaml
content_ref:
  content_blocks:
  - element_type: BlockParagraph
    inline_content:
    - element_type: TextRun
      text: 'Die nachfolgenden Gesetze werden wie folgt geändert:'
  - element_type: BlockList
    eId: title_9__art_44__para___content__blocklist_1
    items:
    - eId: title_9__art_44__para___content__blocklist_1__item_a
      content_blocks:
      - …
      num:
        inline_content:
        - …
      heading:
        eId: title_9__art_44__para___content__blocklist_1__item_a__heading
        inline_content:
        - …
        - …

```
#### Beispiel Content: zh idg 3 1

```yaml
content_ref:
  content_blocks:
  - element_type: BlockParagraph
    inline_content:
    - element_type: TextRun
      text: >-
        Die oder der Beauftragte ist berechtigt, die Verfügung nach Massgabe des Verwaltungsrechtspflegegesetzes
        vom 24. Mai 19596
    - element_type: NoteRef
      href: '#note_2'
      marker: '2'
    - … 1 weitere

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