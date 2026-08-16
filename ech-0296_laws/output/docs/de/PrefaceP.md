

## Klasse: PrefaceP 


_Ein Vorspann-Absatz (akn:p). Fedlex verlangt akn:docNumber und akn:docTitle irgendwo im Vorspann (FLX-PF-001/002); kantonale Sammlungen zeichnen zusätzlich Ordnungsnummer, Kurztitel, Abkürzung und Datum aus._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| fedlex_role | 0..1 <br/> [FedlexRoleEnum](FedlexRoleEnum.md) | Fedlex-Erweiterungsattribut fedlex:role. FLX-XF-003 lässt 'marginal' (nur an akn:level, FLX-XF-004) und 'reference' (nur an akn:subheading, FLX-XF-005) zu; die publizierte Bundesverfassung führt zusätzlich 'heading' an einem Präambel-Absatz.  |
| inline_content | * <br/> [InlineElement](InlineElement.md) | Geordneter gemischter Inhalt: eine Folge aus Textabschnitten und Inline-Markup-Elementen (InlineElement-Subklassen). Die Dokumentreihenfolge wird durch die Listenreihenfolge bewahrt.  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Preface](Preface.md) | [preface_paragraphs](preface_paragraphs.md) | range | [PrefaceP](PrefaceP.md) |














### Beispiele
#### Beispiel PrefaceP: sr101 1 1

```yaml
preface_paragraphs:
- inline_content:
  - element_type: DocNumber
    inline_content:
    - element_type: TextRun
      text: '101'

```
#### Beispiel PrefaceP: sr101 1 2

```yaml
preface_paragraphs:
- inline_content:
  - element_type: DocTitle
    inline_content:
    - element_type: TextRun
      text: Bundesverfassung
    - element_type: Br
    - … 1 weitere

```
#### Beispiel PrefaceP: sr101 1 3

```yaml
preface_paragraphs:
- inline_content:
  - element_type: TextRun
    text: vom 18. April 1999 (Stand am 3. März 2024)

```
#### Beispiel PrefaceP: bgoe 1 3

```yaml
preface_paragraphs:
- inline_content:
  - element_type: TextRun
    text: (Öffentlichkeitsgesetz, BGÖ)

```
#### Beispiel PrefaceP: bgoe 1 2

```yaml
preface_paragraphs:
- inline_content:
  - element_type: DocTitle
    inline_content:
    - element_type: TextRun
      text: Bundesgesetz
    - element_type: Br
    - … 1 weitere

```
#### Beispiel PrefaceP: zh idg 1 1

```yaml
preface_paragraphs:
- inline_content:
  - element_type: DocketNumber
    eId: docketNum_1
    title_attr: Orndungsnummer
    inline_content:
    - element_type: TextRun
      text: '170.4'
  - element_type: DocTitle
    eId: actTitle
    title_attr: Erlasstitel
    inline_content:
    - element_type: TextRun
      text: Gesetz über die Information und den Datenschutz
  - … 3 weitere

```
#### Beispiel PrefaceP: bgoe 1 1

```yaml
preface_paragraphs:
- inline_content:
  - element_type: DocNumber
    inline_content:
    - element_type: TextRun
      text: '152.3'

```
#### Beispiel PrefaceP: bgoe 1 4

```yaml
preface_paragraphs:
- inline_content:
  - element_type: TextRun
    text: vom 17. Dezember 2004 (Stand am 1. November 2023)

```






</div>