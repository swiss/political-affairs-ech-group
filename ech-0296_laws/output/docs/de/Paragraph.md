

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
#### Beispiel Paragraph: Paragraph with a list instead of running text

```yaml
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
              Organisationen und Personen des öffentlichen oder privaten Rechts, die
              nicht der Bundesverwaltung angehören, soweit sie Erlasse oder erstinstanzliche
              Verfügungen im Sinne von Artikel 5 des Bundesgesetzes vom 20. Dezember
              1968 über das Verwaltungsverfahren erlassen;

```
#### Beispiel Paragraph: Paragraph with running text

```yaml
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






</div>