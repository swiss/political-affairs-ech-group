

## Klasse: Article 


_Ein Artikel, die primäre legislative Einheit (akn:article). Constraints (FLX-ART-*): - akn:num ist obligatorisch (FLX-ART-001) - nur Überschriften-Elemente (num, heading, subheading) sowie akn:paragraph und akn:subdivision sind als Kinder erlaubt (FLX-ART-002) - benötigt eindeutiges @eId (FLX-ART-003)_




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 1 <br/> [EIdType](EIdType.md) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| num | 1 <br/> [MixedText](MixedText.md) | Die Artikelnummer (z.B. 'Art. 1'). In jedem Artikel obligatorisch (FLX-ART-001). |
| heading | 0..1 <br/> [MixedText](MixedText.md) | Überschrift für ein Strukturelement (akn:heading). Kann Inline-Markup einschliesslich akn:br enthalten (FLX-TXT-001: br in Überschriften erlaubt). Muss vor subheading stehen (FLX-HD-004, FLX-HD-005).  |
| subheading | 0..1 <br/> [MixedText](MixedText.md) | Unterüberschrift für ein Strukturelement (akn:subheading). fedlex:role='reference' kennzeichnet es als Referenzüberschrift (FLX-XF-005). Maximal eine subheading pro Element (FLX-HD-006).  |
| paragraphs | * <br/> [Paragraph](Paragraph.md) | Absatz-Kindelemente (akn:paragraph) innerhalb eines Artikels oder Unterabschnitts. |
| subdivisions | * <br/> [Subdivision](Subdivision.md) | Unterabschnitt-Kindelemente (akn:subdivision) innerhalb eines Artikels. |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [ActBody](ActBody.md) | [articles](articles.md) | range | [Article](Article.md) |
| [Book](Book.md) | [articles](articles.md) | range | [Article](Article.md) |
| [Title](Title.md) | [articles](articles.md) | range | [Article](Article.md) |
| [Part](Part.md) | [articles](articles.md) | range | [Article](Article.md) |
| [Chapter](Chapter.md) | [articles](articles.md) | range | [Article](Article.md) |
| [Subchapter](Subchapter.md) | [articles](articles.md) | range | [Article](Article.md) |
| [Section](Section.md) | [articles](articles.md) | range | [Article](Article.md) |
| [Subsection](Subsection.md) | [articles](articles.md) | range | [Article](Article.md) |
| [Level](Level.md) | [articles](articles.md) | range | [Article](Article.md) |
| [Transitional](Transitional.md) | [articles](articles.md) | range | [Article](Article.md) |
| [Proviso](Proviso.md) | [articles](articles.md) | range | [Article](Article.md) |














### Beispiele
#### Beispiel Article: sr101 1 3

```yaml
articles:
- eId: art_3
  num:
    inline_content:
    - element_type: B
      inline_content:
      - …
  heading:
    inline_content:
    - element_type: TextRun
      text: Kantone
  paragraphs:
  - eId: art_3/para
    content_ref:
      content_blocks:
      - …

```
#### Beispiel Article: Article with a bold article number

```yaml
articles:
- eId: art_1
  num:
    inline_content:
    - element_type: B
      inline_content:
      - …
  heading:
    inline_content:
    - element_type: TextRun
      text: Schweizerische Eidgenossenschaft
  paragraphs:
  - eId: art_1/para
    content_ref:
      content_blocks:
      - …

```
#### Beispiel Article: Article with numbered paragraphs

```yaml
articles:
- eId: art_2
  num:
    inline_content:
    - element_type: B
      inline_content:
      - …
  heading:
    inline_content:
    - element_type: TextRun
      text: Zweck
  paragraphs:
  - eId: art_2/para_1
    num:
      inline_content:
      - …
    content_ref:
      content_blocks:
      - …
  - eId: art_2/para_2
    num:
      inline_content:
      - …
    content_ref:
      content_blocks:
      - …
  - … 2 weitere

```
#### Beispiel Article: sr101 1 4

```yaml
articles:
- eId: art_4
  num:
    inline_content:
    - element_type: B
      inline_content:
      - …
  heading:
    inline_content:
    - element_type: TextRun
      text: Landessprachen
  paragraphs:
  - eId: art_4/para
    content_ref:
      content_blocks:
      - …

```
#### Beispiel Article: sr101 1 6

```yaml
articles:
- eId: art_5_a
  num:
    inline_content:
    - element_type: B
      inline_content:
      - …
    - element_type: I
      inline_content:
      - …
    - … 1 weitere
  heading:
    inline_content:
    - element_type: TextRun
      text: Subsidiarität
  paragraphs:
  - eId: art_5_a/para
    content_ref:
      content_blocks:
      - …

```
#### Beispiel Article: sr101 1 7

```yaml
articles:
- eId: art_6
  num:
    inline_content:
    - element_type: B
      inline_content:
      - …
  heading:
    inline_content:
    - element_type: TextRun
      text: Individuelle und gesellschaftliche Verantwortung
  paragraphs:
  - eId: art_6/para
    content_ref:
      content_blocks:
      - …

```
#### Beispiel Article: sr101 1 5

```yaml
articles:
- eId: art_5
  num:
    inline_content:
    - element_type: B
      inline_content:
      - …
  heading:
    inline_content:
    - element_type: TextRun
      text: Grundsätze rechtsstaatlichen Handelns
  paragraphs:
  - eId: art_5/para_1
    num:
      inline_content:
      - …
    content_ref:
      content_blocks:
      - …
  - eId: art_5/para_2
    num:
      inline_content:
      - …
    content_ref:
      content_blocks:
      - …
  - … 2 weitere

```






</div>