

## Klasse: MainBody 


_Hauptteil eines beiliegenden Dokuments (akn:mainBody). Anders als der Erlasskörper nimmt er Absätze und Ebenen unmittelbar auf, ohne die Gesetzeshierarchie._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| content_blocks | * <br/> [BlockElement](BlockElement.md) | Blockinhalt in Lesereihenfolge: Absätze, Aufzählungen und Tabellen, wie sie im Dokument aufeinanderfolgen.  |
| levels | * <br/> [Level](Level.md) | Transparente Level-Kindelemente (akn:level). |
| content_ref | 0..1 <br/> [Content](Content.md) | Inhaltselement innerhalb eines Absatzes (akn:content). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Doc](Doc.md) | [main_body](main_body.md) | range | [MainBody](MainBody.md) |



















</div>