

## Klasse: DocDate 


_Ein Datum im Vorspann, mit dem maschinenlesbaren Wert in @date._



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 0..1 <br/> [EIdType](EIdType.md) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| date_attr | 0..1 <br/> [String](String.md) | Das Datum, das dieses Element auszeichnet, nach ISO 8601 (@date). |
| title_attr | 0..1 <br/> [String](String.md) | Menschenlesbare Bezeichnung der ausgezeichneten Stelle (@title). |
| inline_content | * <br/> [InlineElement](InlineElement.md) | Geordneter gemischter Inhalt: eine Folge aus Textabschnitten und Inline-Markup-Elementen (InlineElement-Subklassen). Die Dokumentreihenfolge wird durch die Listenreihenfolge bewahrt.  |
| element_type | 0..1 <br/> [String](String.md) | Typ-Diskriminator für die konkrete Unterklasse einer abstrakten Basis: InlineElement oder BlockElement. <br/><br/>Vererbung: [InlineElement](InlineElement.md) |






















</div>