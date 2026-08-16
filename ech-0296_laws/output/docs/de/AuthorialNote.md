

## Klasse: AuthorialNote 


_Eine Fussnote des Autors (akn:authorialNote). Rekursiv in Block-Inhalt: enthält ein oder mehrere akn:p-Absätze, die selbst Inline-Inhalt tragen._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| content_blocks | * <br/> [BlockElement](BlockElement.md) | Blockinhalt in Lesereihenfolge: Absätze, Aufzählungen und Tabellen, wie sie im Dokument aufeinanderfolgen.  |
| element_type | 0..1 <br/> [String](String.md) | Typ-Diskriminator für die konkrete Unterklasse einer abstrakten Basis: InlineElement oder BlockElement. <br/><br/>Vererbung: [InlineElement](InlineElement.md) |






















</div>