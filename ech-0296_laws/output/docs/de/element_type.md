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
| [BlockElement](BlockElement.md) | Abstrakte Basis für ein Element auf Blockebene: die Absätze, Aufzählungen und... |  no  |
| [Modification](Modification.md) | Abstrakte Basis für eine im Analyseblock vermerkte Änderung |  no  |
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
| [DocNumber](DocNumber.md) | Die Dokumentnummer im Vorspann |  no  |
| [DocTitle](DocTitle.md) | Der Dokumenttitel im Vorspann |  no  |
| [DocketNumber](DocketNumber.md) | Die Ordnungsnummer des Erlasses, wie sie kantonale Sammlungen führen |  no  |
| [ShortTitle](ShortTitle.md) | Der Kurztitel des Erlasses |  no  |
| [Abbr](Abbr.md) | Die Abkürzung des Erlasses |  no  |
| [DocDate](DocDate.md) | Ein Datum im Vorspann, mit dem maschinenlesbaren Wert in @date |  no  |
| [DateInline](DateInline.md) | Ein Datum im Fliesstext, mit dem maschinenlesbaren Wert in @date |  no  |
| [Signature](Signature.md) | Eine Unterschriftszeile |  no  |
| [Eol](Eol.md) | Ein Zeilenende innerhalb eines Absatzes |  no  |
| [Def](Def.md) | Ein im Text definierter Begriff |  no  |
| [NoteRef](NoteRef.md) | Verweis auf eine in den Metadaten gehaltene Anmerkung |  no  |
| [Role](Role.md) | Eine Rolle, die eine Person innehat, mit Verweis auf ihre Deklaration |  no  |
| [Person](Person.md) | Eine Person, mit Verweis auf ihre Deklaration und die innegehabte Rolle |  no  |
| [ActiveRef](ActiveRef.md) | Verweis auf einen Erlass, den dieses Dokument ändert |  no  |
| [Formula](Formula.md) | Eine Eingangs- oder Schlussformel des Vorspruchs (akn:formula) |  no  |
| [Citations](Citations.md) | Die Erwägungen des Vorspruchs — worauf sich der Erlass beruft |  no  |
| [TextualMod](TextualMod.md) | Eine Textänderung: der Wortlaut eines anderen Erlasses wird eingefügt, ersetz... |  no  |
| [ForceMod](ForceMod.md) | Eine Änderung der Rechtskraft: ein Erlass oder ein Teil davon tritt in Kraft,... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [InlineElement](InlineElement.md), [BlockElement](BlockElement.md), [Modification](Modification.md) |

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
| Abbr |
| AuthorialNote |
| B |





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
- value: Abbr
- value: AuthorialNote
- value: B
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
designates_type: true
domain_of:
- InlineElement
- BlockElement
- Modification
range: string

```
</details></div>