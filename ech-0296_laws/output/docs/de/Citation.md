

## Klasse: Citation 


_Eine einzelne Erwägung._



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 0..1 <br/> [EIdType](EIdType.md) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| refers_to | 0..1 <br/> [String](String.md) | Anker, der nennt, worauf sich das Element bezieht (@refersTo). |
| content_blocks | * <br/> [BlockElement](BlockElement.md) | Blockinhalt in Lesereihenfolge: Absätze, Aufzählungen und Tabellen, wie sie im Dokument aufeinanderfolgen.  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Citations](Citations.md) | [citation_list](citation_list.md) | range | [Citation](Citation.md) |



















</div>