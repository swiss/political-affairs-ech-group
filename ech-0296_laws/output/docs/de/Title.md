

## Klasse: Title 


_Titel-Ebene eines Erlasses (akn:title). Erlaubte Kinder: book, part, chapter, subchapter, section, subsection, level (FLX-HR-001-ti). Benötigt eindeutiges @eId (FLX-HR-002-ti)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 1 <br/> [EIdType](EIdType.md) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| num | 0..1 <br/> [MixedText](MixedText.md) | Nummerierungselement für ein Strukturelement oder einen Artikel (akn:num). Bei Artikeln obligatorisch (FLX-ART-001). num muss vor heading und subheading stehen (FLX-HD-001, FLX-HD-002, FLX-HD-003).  |
| heading | 0..1 <br/> [MixedText](MixedText.md) | Überschrift für ein Strukturelement (akn:heading). Kann Inline-Markup einschliesslich akn:br enthalten (FLX-TXT-001: br in Überschriften erlaubt). Muss vor subheading stehen (FLX-HD-004, FLX-HD-005).  |
| subheading | 0..1 <br/> [MixedText](MixedText.md) | Unterüberschrift für ein Strukturelement (akn:subheading). fedlex:role='reference' kennzeichnet es als Referenzüberschrift (FLX-XF-005). Maximal eine subheading pro Element (FLX-HD-006).  |
| books | * <br/> [Book](Book.md) | Buch-Kindelemente (akn:book). |
| parts | * <br/> [Part](Part.md) | Teil-Kindelemente (akn:part). |
| chapters | * <br/> [Chapter](Chapter.md) | Kapitel-Kindelemente (akn:chapter). |
| subchapters | * <br/> [Subchapter](Subchapter.md) | Unterkapitel-Kindelemente (akn:subchapter). |
| sections | * <br/> [Section](Section.md) | Abschnitt-Kindelemente (akn:section). |
| subsections | * <br/> [Subsection](Subsection.md) | Unterabschnitt-Kindelemente (akn:subsection). |
| levels | * <br/> [Level](Level.md) | Transparente Level-Kindelemente (akn:level). |
| articles | * <br/> [Article](Article.md) | Artikel-Kindelemente (akn:article). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [ActBody](ActBody.md) | [titles](titles.md) | range | [Title](Title.md) |
| [Book](Book.md) | [titles](titles.md) | range | [Title](Title.md) |
| [Level](Level.md) | [titles](titles.md) | range | [Title](Title.md) |














### Beispiele
#### Beispiel Title: sr101 1 3

```yaml
titles:
- eId: tit_3
  num:
    inline_content:
    - element_type: TextRun
      text: '3. Titel:'
  heading:
    inline_content:
    - element_type: TextRun
      text: Bund, Kantone und Gemeinden
  chapters:
  - eId: tit_3/chap_1
    num:
      inline_content:
      - …
    heading:
      inline_content:
      - …
    sections:
    - eId: tit_3/chap_1/sec_1
      num: …
      heading: …
      articles:
      - …
      - …
      - … 1 weitere
    - eId: tit_3/chap_1/sec_2
      num: …
      heading: …
      articles:
      - …
      - …
      - … 5 weitere
    - … 2 weitere
  - eId: tit_3/chap_2
    num:
      inline_content:
      - …
    heading:
      inline_content:
      - …
    sections:
    - eId: tit_3/chap_2/sec_1
      num: …
      heading: …
      articles:
      - …
      - …
      - … 1 weitere
    - eId: tit_3/chap_2/sec_2
      num: …
      heading: …
      articles:
      - …
      - …
      - … 3 weitere
    - … 8 weitere
  - … 1 weitere

```
#### Beispiel Title: sr101 1 5

```yaml
titles:
- eId: tit_5
  num:
    inline_content:
    - element_type: TextRun
      text: '5. Titel:'
  heading:
    inline_content:
    - element_type: TextRun
      text: Bundesbehörden
  chapters:
  - eId: tit_5/chap_1
    num:
      inline_content:
      - …
    heading:
      inline_content:
      - …
    articles:
    - eId: art_143
      num: …
      heading: …
      paragraphs:
      - …
    - eId: art_144
      num: …
      heading: …
      paragraphs:
      - …
      - …
      - … 1 weitere
    - … 3 weitere
  - eId: tit_5/chap_2
    num:
      inline_content:
      - …
    heading:
      inline_content:
      - …
    sections:
    - eId: tit_5/chap_2/sec_1
      num: …
      heading: …
      articles:
      - …
      - …
      - … 6 weitere
    - eId: tit_5/chap_2/sec_2
      num: …
      heading: …
      articles:
      - …
      - …
      - … 5 weitere
    - … 1 weitere
  - … 2 weitere

```
#### Beispiel Title: Title with number heading and articles

```yaml
titles:
- eId: tit_1
  num:
    inline_content:
    - element_type: TextRun
      text: '1. Titel:'
  heading:
    inline_content:
    - element_type: TextRun
      text: Allgemeine Bestimmungen
  articles:
  - eId: art_1
    num:
      inline_content:
      - …
    heading:
      inline_content:
      - …
    paragraphs:
    - eId: art_1/para
      content_ref: …
  - eId: art_2
    num:
      inline_content:
      - …
    heading:
      inline_content:
      - …
    paragraphs:
    - eId: art_2/para_1
      num: …
      content_ref: …
    - eId: art_2/para_2
      num: …
      content_ref: …
    - … 2 weitere
  - … 5 weitere

```
#### Beispiel Title: sr101 1 6

```yaml
titles:
- eId: tit_6
  num:
    inline_content:
    - element_type: TextRun
      text: '6. Titel:'
  heading:
    inline_content:
    - element_type: TextRun
      text: Revision der Bundesverfassung und Übergangsbestimmungen
  chapters:
  - eId: tit_6/chap_1
    num:
      inline_content:
      - …
    heading:
      inline_content:
      - …
    articles:
    - eId: art_192
      num: …
      heading: …
      paragraphs:
      - …
      - …
    - eId: art_193
      num: …
      heading: …
      paragraphs:
      - …
      - …
      - … 2 weitere
    - … 2 weitere
  - eId: tit_6/chap_2
    num:
      inline_content:
      - …
    heading:
      inline_content:
      - …
    articles:
    - eId: art_196
      num: …
      heading: …
      subdivisions:
      - …
      - …
      - … 14 weitere
    - eId: art_197
      num: …
      heading: …
      subdivisions:
      - …
      - …
      - … 14 weitere

```
#### Beispiel Title: sr101 1 2

```yaml
titles:
- eId: tit_2
  num:
    inline_content:
    - element_type: TextRun
      text: '2. Titel:'
  heading:
    inline_content:
    - element_type: TextRun
      text: Grundrechte, Bürgerrechte und Sozialziele
  chapters:
  - eId: tit_2/chap_1
    num:
      inline_content:
      - …
    heading:
      inline_content:
      - …
    articles:
    - eId: art_7
      num: …
      heading: …
      paragraphs:
      - …
    - eId: art_8
      num: …
      heading: …
      paragraphs:
      - …
      - …
      - … 2 weitere
    - … 30 weitere
  - eId: tit_2/chap_2
    num:
      inline_content:
      - …
    heading:
      inline_content:
      - …
    articles:
    - eId: art_37
      num: …
      heading: …
      paragraphs:
      - …
      - …
    - eId: art_38
      num: …
      heading: …
      paragraphs:
      - …
      - …
      - … 1 weitere
    - … 2 weitere
  - … 1 weitere

```
#### Beispiel Title: sr101 1 4

```yaml
titles:
- eId: tit_4
  num:
    inline_content:
    - element_type: TextRun
      text: '4. Titel:'
  heading:
    inline_content:
    - element_type: TextRun
      text: Volk und Stände
  chapters:
  - eId: tit_4/chap_1
    num:
      inline_content:
      - …
    heading:
      inline_content:
      - …
    articles:
    - eId: art_136
      num: …
      heading: …
      paragraphs:
      - …
      - …
    - eId: art_137
      num: …
      heading: …
      paragraphs:
      - …
  - eId: tit_4/chap_2
    num:
      inline_content:
      - …
    heading:
      inline_content:
      - …
    articles:
    - eId: art_138
      num: …
      heading: …
      paragraphs:
      - …
      - …
    - eId: art_139
      num: …
      heading: …
      paragraphs:
      - …
      - …
      - … 3 weitere
    - … 6 weitere

```






</div>