

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
#### Beispiel Article: Article with a bold article number

```yaml
articles:
- eId: art_1
  num:
    inline_content:
    - element_type: B
      inline_content:
      - element_type: TextRun
        text: Art. 1
  heading:
    inline_content:
    - element_type: TextRun
      text: Schweizerische Eidgenossenschaft
  paragraphs:
  - eId: art_1/para
    content_ref:
      block_paragraphs:
      - inline_content:
        - element_type: TextRun
          text: >-
            Das Schweizervolk und die Kantone Zürich, Bern, Luzern, Uri, Schwyz, Obwalden
            und Nidwalden, Glarus, Zug, Freiburg, Solothurn, Basel-Stadt und Basel-Landschaft,
            Schaffhausen, Appenzell Ausserrhoden und Appenzell Innerrhoden, St. Gallen,
            Graubünden, Aargau, Thurgau, Tessin, Waadt, Wallis, Neuenburg, Genf und
            Jura bilden die Schweizerische Eidgenossenschaft.

```
#### Beispiel Article: Article with numbered paragraphs

```yaml
articles:
- eId: art_2
  num:
    inline_content:
    - element_type: B
      inline_content:
      - element_type: TextRun
        text: Art. 2
  heading:
    inline_content:
    - element_type: TextRun
      text: Persönlicher Geltungsbereich
  paragraphs:
  - eId: art_2/para_1
    num:
      inline_content:
      - element_type: TextRun
        text: '1'
    content_ref:
      block_lists:
      - eId: art_2/para_1/lst
        list_introduction:
          eId: art_2/para_1/listintro
          inline_content:
          - element_type: TextRun
            text: ' Dieses Gesetz gilt für:'
        items:
        - eId: art_2/para_1/lbl_a
          num:
            inline_content:
            - element_type: TextRun
              text: 'a. '
          block_paragraphs:
          - inline_content:
            - element_type: TextRun
              text: die Bundesverwaltung;
        - eId: art_2/para_1/lbl_b
          num:
            inline_content:
            - element_type: TextRun
              text: 'b. '
          block_paragraphs:
          - inline_content:
            - element_type: TextRun
              text: >-
                Organisationen und Personen des öffentlichen oder privaten Rechts,
                die nicht der Bundesverwaltung angehören, soweit sie Erlasse oder
                erstinstanzliche Verfügungen im Sinne von Artikel 5 des Bundesgesetzes
                vom 20. Dezember 1968 über das Verwaltungsverfahren erlassen;

```






</div>