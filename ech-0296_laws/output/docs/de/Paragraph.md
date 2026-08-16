

## Klasse: Paragraph 


_Ein Absatz innerhalb eines Artikels oder Unterabschnitts (akn:paragraph). Constraints (FLX-PR-*): - nur Überschriften-Elemente und akn:content als Kinder erlaubt (FLX-PR-001) - nur als direktes Kind von akn:article oder akn:subdivision erlaubt (FLX-PR-002) - benötigt eindeutiges @eId (FLX-PR-003)_




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 1 <br/> [EIdType](EIdType.md) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| num | 0..1 <br/> [MixedText](MixedText.md) | Nummerierungselement für ein Strukturelement oder einen Artikel (akn:num). Bei Artikeln obligatorisch (FLX-ART-001). num muss vor heading und subheading stehen (FLX-HD-001, FLX-HD-002, FLX-HD-003).  |
| heading | 0..1 <br/> [MixedText](MixedText.md) | Überschrift für ein Strukturelement (akn:heading). Kann Inline-Markup einschliesslich akn:br enthalten (FLX-TXT-001: br in Überschriften erlaubt). Muss vor subheading stehen (FLX-HD-004, FLX-HD-005).  |
| content_ref | 0..1 <br/> [Content](Content.md) | Inhaltselement innerhalb eines Absatzes (akn:content). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Article](Article.md) | [paragraphs](paragraphs.md) | range | [Paragraph](Paragraph.md) |
| [Subdivision](Subdivision.md) | [paragraphs](paragraphs.md) | range | [Paragraph](Paragraph.md) |
| [Transitional](Transitional.md) | [paragraphs](paragraphs.md) | range | [Paragraph](Paragraph.md) |
| [Proviso](Proviso.md) | [paragraphs](paragraphs.md) | range | [Paragraph](Paragraph.md) |














### Beispiele
#### Beispiel Paragraph: zh idg 5 1

```yaml
paragraphs:
- eId: title_2__chp_G__art_34__para_1
  num:
    inline_content:
    - element_type: TextRun
      text: '1'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …
    - element_type: BlockList
      eId: title_7__art_34__para_1__content__blocklist_1
      items:
      - …
      - …
      - … 5 weitere

```
#### Beispiel Paragraph: zh idg 4 1

```yaml
paragraphs:
- eId: title_9__art_44__para_1
  num:
    inline_content:
    - element_type: TextRun
      text: '1'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …
    - element_type: BlockList
      eId: title_9__art_44__para___content__blocklist_1
      items:
      - …

```
#### Beispiel Paragraph: zh idg 3 1

```yaml
paragraphs:
- eId: title_9__art_43__para_1
  num:
    inline_content:
    - element_type: TextRun
      text: '1'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: zh idg 7 1

```yaml
paragraphs:
- eId: title_7__art_36__para_1
  num:
    inline_content:
    - element_type: TextRun
      text: '1'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: sr101 5 2

```yaml
paragraphs:
- eId: art_5/para_2
  num:
    inline_content:
    - element_type: TextRun
      text: '2'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: sr101 3 1

```yaml
paragraphs:
- eId: art_3/para
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: zh idg 10 1

```yaml
paragraphs:
- eId: title_7__art_39__para_1
  num:
    inline_content:
    - element_type: TextRun
      text: '1'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: zh idg 4 2

```yaml
paragraphs:
- eId: title_7__art_33__para_2
  num:
    inline_content:
    - element_type: TextRun
      text: '2'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: zh idg 7 3

```yaml
paragraphs:
- eId: title_7__art_36__para_3
  num:
    inline_content:
    - element_type: TextRun
      text: '3'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …
      - …
      - … 1 weitere

```
#### Beispiel Paragraph: zh idg 6 2

```yaml
paragraphs:
- eId: title_7__art_35__para_2
  num:
    inline_content:
    - element_type: TextRun
      text: '2'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: zh idg 2 2

```yaml
paragraphs:
- eId: title_9__art_42__para_2
  num:
    inline_content:
    - element_type: TextRun
      text: '2'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …
    - element_type: BlockList
      eId: title_9__art_42__para_2__content__blocklist_1
      items:
      - …
      - …

```
#### Beispiel Paragraph: sr101 6 1

```yaml
paragraphs:
- eId: art_5_a/para
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: zh idg 6 3

```yaml
paragraphs:
- eId: title_6__art_29__para_3
  num:
    inline_content:
    - element_type: TextRun
      text: '3'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: sr101 2 4

```yaml
paragraphs:
- eId: art_2/para_4
  num:
    inline_content:
    - element_type: TextRun
      text: '4'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: zh idg 1 4

```yaml
paragraphs:
- eId: title_3__art_14__para_4
  num:
    inline_content:
    - element_type: TextRun
      text: '4'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: sr101 5 1

```yaml
paragraphs:
- eId: art_5/para_1
  num:
    inline_content:
    - element_type: TextRun
      text: '1'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: sr101 4 1

```yaml
paragraphs:
- eId: art_4/para
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: zh idg 2 3

```yaml
paragraphs:
- eId: title_7__art_31__para_3
  num:
    inline_content:
    - element_type: TextRun
      text: '3'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: sr101 5 3

```yaml
paragraphs:
- eId: art_5/para_3
  num:
    inline_content:
    - element_type: TextRun
      text: '3'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: Paragraph with a list instead of running text

```yaml
paragraphs:
- eId: art_2/para_1
  num:
    inline_content:
    - element_type: TextRun
      text: '1'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: zh idg 6 4

```yaml
paragraphs:
- eId: title_6__art_29__para_4
  num:
    inline_content:
    - element_type: TextRun
      text: '4'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: zh idg 1 1

```yaml
paragraphs:
- eId: title_9__art_41__para_1
  num:
    inline_content:
    - element_type: TextRun
      text: '1'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …
    - element_type: BlockList
      eId: title_9__art_41__para_1__content__blocklist_1
      items:
      - …
      - …

```
#### Beispiel Paragraph: zh idg 6 1

```yaml
paragraphs:
- eId: title_7__art_35__para_1
  num:
    inline_content:
    - element_type: TextRun
      text: '1'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: zh idg 7 2

```yaml
paragraphs:
- eId: title_7__art_36__para_2
  num:
    inline_content:
    - element_type: TextRun
      text: '2'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: sr101 7 1

```yaml
paragraphs:
- eId: art_6/para
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: zh idg 9 1

```yaml
paragraphs:
- eId: title_7__art_38__para_1
  num: {}
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: zh idg 2 1

```yaml
paragraphs:
- eId: title_9__art_42__para_1
  num:
    inline_content:
    - element_type: TextRun
      text: '1'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …
    - element_type: BlockList
      eId: title_9__art_42__para_1__content__blocklist_1
      items:
      - …
      - …

```
#### Beispiel Paragraph: zh idg 8 1

```yaml
paragraphs:
- eId: title_7__art_37__para_1
  num:
    inline_content:
    - element_type: TextRun
      text: '1'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: sr101 5 4

```yaml
paragraphs:
- eId: art_5/para_4
  num:
    inline_content:
    - element_type: TextRun
      text: '4'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: sr101 2 2

```yaml
paragraphs:
- eId: art_2/para_2
  num:
    inline_content:
    - element_type: TextRun
      text: '2'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: zh idg 1 2

```yaml
paragraphs:
- eId: title_8__art_40__para_2
  num:
    inline_content:
    - element_type: TextRun
      text: '2'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: sr101 2 3

```yaml
paragraphs:
- eId: art_2/para_3
  num:
    inline_content:
    - element_type: TextRun
      text: '3'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: Paragraph with running text

```yaml
paragraphs:
- eId: art_1/para
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: zh idg 3 3

```yaml
paragraphs:
- eId: title_7__art_32__para_3
  num:
    inline_content:
    - element_type: TextRun
      text: '3'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: zh idg 1 3

```yaml
paragraphs:
- eId: title_5__art_23__para_3
  num:
    inline_content:
    - element_type: TextRun
      text: '3'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: zh idg 5 2

```yaml
paragraphs:
- eId: title_6__art_28__para_2
  num:
    inline_content:
    - element_type: TextRun
      text: '2'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```
#### Beispiel Paragraph: zh idg 3 2

```yaml
paragraphs:
- eId: title_7__art_32__para_2
  num:
    inline_content:
    - element_type: TextRun
      text: '2'
  content_ref:
    content_blocks:
    - element_type: BlockParagraph
      inline_content:
      - …

```






</div>