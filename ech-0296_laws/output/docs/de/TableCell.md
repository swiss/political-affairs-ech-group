

## Klasse: TableCell 


_Eine Zelle in einer Tabellenzeile (akn:td). Enthält Block-Inhalt: Fliesstext-Absätze (akn:p) und Auflistungen (akn:blockList)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| colspan | 0..1 <br/> [String](String.md) | Das @colspan-Attribut auf akn:td (HTML-artige Darstellung). |
| content_blocks | * <br/> [BlockElement](BlockElement.md) | Blockinhalt in Lesereihenfolge: Absätze, Aufzählungen und Tabellen, wie sie im Dokument aufeinanderfolgen.  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [TableRow](TableRow.md) | [table_cells](table_cells.md) | range | [TableCell](TableCell.md) |



















</div>