---
search:
  boost: 5.0
---

# Slot: block_lists 


_Auflistungs-Elemente (akn:blockList) innerhalb von Content._



<div data-search-exclude markdown="1">



URI: [laws:block_lists](https://ld.ech.ch/schema/0296/laws/block_lists)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Content](Content.md) | Der Inhalt eines Absatzes (akn:content) |  no  |
| [BlockListItem](BlockListItem.md) | Ein einzelner Punkt in einer Auflistung (akn:item) |  no  |
| [TableCell](TableCell.md) | Eine Zelle in einer Tabellenzeile (akn:td) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [BlockList](BlockList.md) |
| Domäne von | [Content](Content.md), [BlockListItem](BlockListItem.md), [TableCell](TableCell.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: block_lists
annotations:
  description_de:
    tag: description_de
    value: Auflistungs-Elemente (akn:blockList) innerhalb von Content.
description: Auflistungs-Elemente (akn:blockList) innerhalb von Content.
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- Content
- BlockListItem
- TableCell
range: BlockList
multivalued: true

```
</details></div>