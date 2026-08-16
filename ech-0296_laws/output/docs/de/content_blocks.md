---
search:
  boost: 5.0
---

# Slot: content_blocks 


_Blockinhalt in Lesereihenfolge: Absätze, Aufzählungen und Tabellen, wie sie im Dokument aufeinanderfolgen._




<div data-search-exclude markdown="1">



URI: [laws:content_blocks](https://ld.ech.ch/schema/0296/laws/content_blocks)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Preamble](Preamble.md) | Die Präambel des Erlasses (akn:preamble) mit einleitenden Fliesstext-Absätzen... |  no  |
| [Content](Content.md) | Der Inhalt eines Absatzes (akn:content) |  no  |
| [BlockListItem](BlockListItem.md) | Ein einzelner Punkt in einer Auflistung (akn:item) |  no  |
| [TableCell](TableCell.md) | Eine Zelle in einer Tabellenzeile (akn:td) |  no  |
| [AuthorialNote](AuthorialNote.md) | Eine Fussnote des Autors (akn:authorialNote) |  no  |
| [MainBody](MainBody.md) | Hauptteil eines beiliegenden Dokuments (akn:mainBody) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [BlockElement](BlockElement.md) |
| Domäne von | [Preamble](Preamble.md), [Content](Content.md), [BlockListItem](BlockListItem.md), [TableCell](TableCell.md), [AuthorialNote](AuthorialNote.md), [MainBody](MainBody.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: content_blocks
annotations:
  description_de:
    tag: description_de
    value: 'Blockinhalt in Lesereihenfolge: Absätze, Aufzählungen und Tabellen, wie
      sie im Dokument aufeinanderfolgen.

      '
description: 'Blockinhalt in Lesereihenfolge: Absätze, Aufzählungen und Tabellen,
  wie sie im Dokument aufeinanderfolgen.

  '
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- Preamble
- Content
- BlockListItem
- TableCell
- AuthorialNote
- MainBody
range: BlockElement
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>