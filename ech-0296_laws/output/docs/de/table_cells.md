---
search:
  boost: 5.0
---

# Slot: table_cells 


_Zellen in einer Tabellenzeile (akn:td)._



<div data-search-exclude markdown="1">



URI: [laws:table_cells](https://ld.ech.ch/schema/0296/laws/table_cells)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [TableRow](TableRow.md) | Eine Zeile in einer AkomaNtoso-Tabelle (akn:tr) |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [TableCell](TableCell.md) |
| Domäne von | [TableRow](TableRow.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: table_cells
annotations:
  description_de:
    tag: description_de
    value: Zellen in einer Tabellenzeile (akn:td).
description: Zellen in einer Tabellenzeile (akn:td).
from_schema: https://ld.ech.ch/schema/0296/laws
rank: 1000
domain_of:
- TableRow
range: TableCell
multivalued: true

```
</details></div>