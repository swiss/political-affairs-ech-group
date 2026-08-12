---
search:
  boost: 5.0
---

# Slot: block_paragraphs 


_Block-Absatz-Elemente (akn:p) innerhalb von Content._



<div data-search-exclude markdown="1">



URI: [laws:block_paragraphs](https://ld.ech.ch/schema/0296/laws/block_paragraphs)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Preamble](Preamble.md) | Die Präambel des Erlasses (akn:preamble) mit einleitenden Fliesstext-Absätzen... |  no  |
| [Content](Content.md) | Der Inhalt eines Absatzes (akn:content) |  no  |
| [BlockListItem](BlockListItem.md) | Ein einzelner Punkt in einer Auflistung (akn:item) |  no  |
| [TableCell](TableCell.md) | Eine Zelle in einer Tabellenzeile (akn:td) |  no  |
| [AuthorialNote](AuthorialNote.md) | Eine Fussnote des Autors (akn:authorialNote) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [BlockParagraph](BlockParagraph.md) |
| Domäne von | [Preamble](Preamble.md), [Content](Content.md), [BlockListItem](BlockListItem.md), [TableCell](TableCell.md), [AuthorialNote](AuthorialNote.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: block_paragraphs
annotations:
  description_de:
    tag: description_de
    value: Block-Absatz-Elemente (akn:p) innerhalb von Content.
description: Block-Absatz-Elemente (akn:p) innerhalb von Content.
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- Preamble
- Content
- BlockListItem
- TableCell
- AuthorialNote
range: BlockParagraph
multivalued: true

```
</details></div>