---
search:
  boost: 5.0
---

# Slot: element_type 


_Typ-Diskriminator für die konkrete InlineElement-Subklasse._



<div data-search-exclude markdown="1">



URI: [laws:element_type](https://ld.ech.ch/schema/0296/laws/element_type)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [InlineElement](InlineElement.md) | Abstrakte Basis für ein modelliertes Inline-Markup-Element in gemischtem Inha... |  no  |
| [TextRun](TextRun.md) | Ein einfacher Textabschnitt in gemischtem Inhalt |  no  |
| [Ref](Ref.md) | Eine Inline-Referenz (akn:ref) |  no  |
| [B](B.md) | Fett-Inline-Markup (akn:b) |  no  |
| [I](I.md) | Kursiv-Inline-Markup (akn:i) |  no  |
| [Sup](Sup.md) | Hochgestelltes Inline-Markup (akn:sup) |  no  |
| [Span](Span.md) | Generischer Inline-Bereich (akn:span) |  no  |
| [Br](Br.md) | Ein Zeilenumbruch (akn:br) |  no  |
| [Inline](Inline.md) | Ein benanntes präsentationsbezogenes Inline (akn:inline), z |  no  |
| [Placeholder](Placeholder.md) | Ein Platzhalter für entfernten Inhalt (akn:placeholder) mit dem Erweiterungsa... |  no  |
| [AuthorialNote](AuthorialNote.md) | Eine Fussnote des Autors (akn:authorialNote) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [InlineElement](InlineElement.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
### Slot-Eigenschaften

| Eigenschaft | Wert |
| --- | --- |
| Designates Type | Yes |














## LinkML-Quelle

<details>
```yaml
name: element_type
annotations:
  description_de:
    tag: description_de
    value: Typ-Diskriminator für die konkrete InlineElement-Subklasse.
description: Typ-Diskriminator für die konkrete InlineElement-Subklasse.
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
designates_type: true
domain_of:
- InlineElement
range: string

```
</details></div>