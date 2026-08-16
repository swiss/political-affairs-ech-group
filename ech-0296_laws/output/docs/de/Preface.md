

## Klasse: Preface 


_Der Vorspann des Erlasses (akn:preface) mit Dokumentnummer und -titel. Fedlex Schematron verlangt akn:docNumber (FLX-PF-001) und akn:docTitle (FLX-PF-002) innerhalb eines akn:p-Elements._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| preface_paragraphs | * <br/> [PrefaceP](PrefaceP.md) | Die akn:p-Absätze des Vorspanns, die docNumber/docTitle umschliessen. |
| containers | * <br/> [Container](Container.md) | Behälter des Vorspanns (akn:container). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Act](Act.md) | [preface_ref](preface_ref.md) | range | [Preface](Preface.md) |
| [Doc](Doc.md) | [preface_ref](preface_ref.md) | range | [Preface](Preface.md) |














### Beispiele
#### Beispiel Preface: bgoe 1 1

```yaml
preface_ref:
  preface_paragraphs:
  - inline_content:
    - element_type: DocNumber
      inline_content:
      - …
  - inline_content:
    - element_type: DocTitle
      inline_content:
      - …
      - …
      - … 1 weitere
  - … 2 weitere

```
#### Beispiel Preface: sr101 1 1

```yaml
preface_ref:
  preface_paragraphs:
  - inline_content:
    - element_type: DocNumber
      inline_content:
      - …
  - inline_content:
    - element_type: DocTitle
      inline_content:
      - …
      - …
      - … 1 weitere
  - … 1 weitere

```
#### Beispiel Preface: zh idg 1 1

```yaml
preface_ref:
  preface_paragraphs:
  - inline_content:
    - element_type: DocketNumber
      eId: docketNum_1
      title_attr: Orndungsnummer
      inline_content:
      - …
    - element_type: DocTitle
      eId: actTitle
      title_attr: Erlasstitel
      inline_content:
      - …
    - … 3 weitere

```






</div>