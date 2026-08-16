---
search:
  boost: 5.0
---

# Slot: inline_content 


_Geordneter gemischter Inhalt: eine Folge aus Textabschnitten und Inline-Markup-Elementen (InlineElement-Subklassen). Die Dokumentreihenfolge wird durch die Listenreihenfolge bewahrt._




<div data-search-exclude markdown="1">



URI: [laws:inline_content](https://ld.ech.ch/schema/0296/laws/inline_content)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [PrefaceP](PrefaceP.md) | Ein Vorspann-Absatz (akn:p), der Dokumentnummer und/oder -titel umschliesst |  no  |
| [BlockParagraph](BlockParagraph.md) | Ein Fliesstext-Absatz in Content (akn:p) |  no  |
| [MixedText](MixedText.md) | Wiederverwendbarer Halter für gemischten Inhalt: eine geordnete Folge aus Tex... |  no  |
| [Ref](Ref.md) | Eine Inline-Referenz (akn:ref) |  no  |
| [B](B.md) | Fett-Inline-Markup (akn:b) |  no  |
| [I](I.md) | Kursiv-Inline-Markup (akn:i) |  no  |
| [Sup](Sup.md) | Hochgestelltes Inline-Markup (akn:sup) |  no  |
| [Span](Span.md) | Generischer Inline-Bereich (akn:span) |  no  |
| [Inline](Inline.md) | Ein benanntes präsentationsbezogenes Inline (akn:inline), z |  no  |
| [Placeholder](Placeholder.md) | Ein Platzhalter für entfernten Inhalt (akn:placeholder) mit dem Erweiterungsa... |  no  |
| [Block](Block.md) | Ein generischer Block (akn:block), dessen @name den Zweck nennt; trägt gemisc... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [InlineElement](InlineElement.md) |
| Domäne von | [PrefaceP](PrefaceP.md), [BlockParagraph](BlockParagraph.md), [MixedText](MixedText.md), [Ref](Ref.md), [B](B.md), [I](I.md), [Sup](Sup.md), [Span](Span.md), [Inline](Inline.md), [Placeholder](Placeholder.md), [Block](Block.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: inline_content
annotations:
  description_de:
    tag: description_de
    value: 'Geordneter gemischter Inhalt: eine Folge aus Textabschnitten und Inline-Markup-Elementen
      (InlineElement-Subklassen). Die Dokumentreihenfolge wird durch die Listenreihenfolge
      bewahrt.

      '
  xsd_mixed:
    tag: xsd_mixed
    value: 'true'
description: 'Geordneter gemischter Inhalt: eine Folge aus Textabschnitten und Inline-Markup-Elementen
  (InlineElement-Subklassen). Die Dokumentreihenfolge wird durch die Listenreihenfolge
  bewahrt.

  '
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- PrefaceP
- BlockParagraph
- MixedText
- Ref
- B
- I
- Sup
- Span
- Inline
- Placeholder
- Block
range: InlineElement
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>