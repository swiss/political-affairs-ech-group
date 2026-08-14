

## Klasse: Preface 


_Der Vorspann des Erlasses (akn:preface) mit Dokumentnummer und -titel. Fedlex Schematron verlangt akn:docNumber (FLX-PF-001) und akn:docTitle (FLX-PF-002) innerhalb eines akn:p-Elements._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| preface_paragraphs | * <br/> [PrefaceP](PrefaceP.md) | Die akn:p-Absätze des Vorspanns, die docNumber/docTitle umschliessen. |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Act](Act.md) | [preface_ref](preface_ref.md) | range | [Preface](Preface.md) |














### Beispiele
#### Beispiel Preface: sr101 excerpt 1 1

```yaml
preface_ref:
  preface_paragraphs:
  - doc_number: '101'
  - doc_title:
      inline_content:
      - element_type: TextRun
        text: Bundesverfassung
      - element_type: Br
      - element_type: TextRun
        text: der Schweizerischen Eidgenossenschaft

```
#### Beispiel Preface: bgoe excerpt 1 1

```yaml
preface_ref:
  preface_paragraphs:
  - doc_number: '152.3 '
  - doc_title:
      inline_content:
      - element_type: TextRun
        text: Bundesgesetz
      - element_type: Br
      - element_type: TextRun
        text: über das Öffentlichkeitsprinzip der Verwaltung

```






</div>