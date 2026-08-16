

## Klasse: PrefaceP 


_Ein Vorspann-Absatz (akn:p), der Dokumentnummer und/oder -titel umschliesst. Fedlex verlangt akn:docNumber und akn:docTitle innerhalb eines akn:p des Vorspanns (FLX-PF-001/002)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| doc_number | 0..1 <br/> [String](String.md) | Dokumentnummer im Vorspann (akn:docNumber). Pflicht gemäss FLX-PF-001. Typischerweise die SR-Nummer, z.B. '101'.  |
| doc_title | 0..1 <br/> [MixedText](MixedText.md) | Dokumenttitel im Vorspann (akn:docTitle). Pflicht gemäss FLX-PF-002. Kann Inline-Markup und akn:br für Zeilenumbrüche enthalten.  |
| inline_content | * <br/> [InlineElement](InlineElement.md) | Geordneter gemischter Inhalt: eine Folge aus Textabschnitten und Inline-Markup-Elementen (InlineElement-Subklassen). Die Dokumentreihenfolge wird durch die Listenreihenfolge bewahrt.  |

##### Einschränkungen


Mindestens eines der folgenden Felder muss gesetzt sein:

- [doc_number](doc_number.md)
- [doc_title](doc_title.md)
- [inline_content](inline_content.md)










### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Preface](Preface.md) | [preface_paragraphs](preface_paragraphs.md) | range | [PrefaceP](PrefaceP.md) |














### Beispiele
#### Beispiel PrefaceP: sr101 1 1

```yaml
preface_paragraphs:
- doc_number: '101'

```
#### Beispiel PrefaceP: sr101 1 2

```yaml
preface_paragraphs:
- doc_title:
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
- doc_title:
    inline_content:
    - element_type: TextRun
      text: Bundesgesetz
    - element_type: Br
    - … 1 weitere

```
#### Beispiel PrefaceP: bgoe 1 1

```yaml
preface_paragraphs:
- doc_number: '152.3 '

```
#### Beispiel PrefaceP: bgoe 1 4

```yaml
preface_paragraphs:
- inline_content:
  - element_type: TextRun
    text: vom 17. Dezember 2004 (Stand am 1. November 2023)

```






</div>