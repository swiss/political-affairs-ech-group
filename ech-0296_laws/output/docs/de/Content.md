

## Klasse: Content 


_Der Inhalt eines Absatzes (akn:content). Enthält Block-Elemente: akn:p (Fliesstext), akn:blockList (Aufzählungen), akn:table. Wenn in einem akn:level, muss ein akn:mod-Element enthalten sein (FLX-HR-003)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| block_paragraphs | * <br/> [BlockParagraph](BlockParagraph.md) | Block-Absatz-Elemente (akn:p) innerhalb von Content. |
| block_lists | * <br/> [BlockList](BlockList.md) | Auflistungs-Elemente (akn:blockList) innerhalb von Content. |
| tables | * <br/> [Table](Table.md) | Tabellen-Elemente (akn:table) innerhalb von Content. |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Level](Level.md) | [content_ref](content_ref.md) | range | [Content](Content.md) |
| [Paragraph](Paragraph.md) | [content_ref](content_ref.md) | range | [Content](Content.md) |














### Beispiele
#### Beispiel Content: bgoe excerpt 1 1

```yaml
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
#### Beispiel Content: sr101 excerpt 1 1

```yaml
content_ref:
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