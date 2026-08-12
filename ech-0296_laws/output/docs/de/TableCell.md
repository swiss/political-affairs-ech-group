

## Klasse: TableCell 


_Eine Zelle in einer Tabellenzeile (akn:td). Enthält Block-Inhalt: Fliesstext-Absätze (akn:p) und Auflistungen (akn:blockList)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| colspan | 0..1 <br/> [String](String.md) | Das @colspan-Attribut auf akn:td (HTML-artige Darstellung). |
| block_paragraphs | * <br/> [BlockParagraph](BlockParagraph.md) | Block-Absatz-Elemente (akn:p) innerhalb von Content. |
| block_lists | * <br/> [BlockList](BlockList.md) | Auflistungs-Elemente (akn:blockList) innerhalb von Content. |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [TableRow](TableRow.md) | [table_cells](table_cells.md) | range | [TableCell](TableCell.md) |



















</div>