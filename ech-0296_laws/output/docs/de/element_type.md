---
search:
  boost: 5.0
---

# Slot: element_type 


_Typ-Diskriminator für die konkrete Unterklasse einer abstrakten Basis: InlineElement oder BlockElement._




<div data-search-exclude markdown="1">



URI: [laws:element_type](https://ld.ech.ch/schema/0296/laws/element_type)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [InlineElement](InlineElement.md) | Abstrakte Basis für ein modelliertes Inline-Markup-Element in gemischtem Inha... |  no  |
| [BlockElement](BlockElement.md) | Abstrakte Basis für ein Element auf Blockebene innerhalb von Inhalt, Aufzählu... |  no  |
| [BlockParagraph](BlockParagraph.md) | Ein Fliesstext-Absatz in Content (akn:p) |  no  |
| [BlockList](BlockList.md) | Eine Auflistung von nummerierten oder buchstabierten Punkten (akn:blockList),... |  no  |
| [Table](Table.md) | Ein Tabellen-Element innerhalb von Content (akn:table) |  no  |
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
| Domäne von | [InlineElement](InlineElement.md), [BlockElement](BlockElement.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
### Slot-Eigenschaften

| Eigenschaft | Wert |
| --- | --- |
| Designates Type | Yes |











## Beispiele

| Wert |
| --- |
| AuthorialNote |
| B |
| BlockList |





## LinkML-Quelle

<details>
```yaml
name: element_type
annotations:
  description_de:
    tag: description_de
    value: 'Typ-Diskriminator für die konkrete Unterklasse einer abstrakten Basis:
      InlineElement oder BlockElement.

      '
description: 'Typ-Diskriminator für die konkrete Unterklasse einer abstrakten Basis:
  InlineElement oder BlockElement.

  '
examples:
- value: AuthorialNote
- value: B
- value: BlockList
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
designates_type: true
domain_of:
- InlineElement
- BlockElement
range: string

```
</details></div>