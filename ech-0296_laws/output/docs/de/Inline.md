

## Klasse: Inline 


_Ein benanntes präsentationsbezogenes Inline (akn:inline), z.B. name='man-font-style-normal'._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| name_attr | 0..1 <br/> [String](String.md) | Das @name-Attribut auf akn:inline, z.B. 'man-font-style-normal'. |
| inline_content | * <br/> [InlineElement](InlineElement.md) | Geordneter gemischter Inhalt: eine Folge aus Textabschnitten und Inline-Markup-Elementen (InlineElement-Subklassen). Die Dokumentreihenfolge wird durch die Listenreihenfolge bewahrt.  |
| element_type | 0..1 <br/> [String](String.md) | Typ-Diskriminator für die konkrete Unterklasse einer abstrakten Basis: InlineElement oder BlockElement. <br/><br/>Vererbung: [InlineElement](InlineElement.md) |






















</div>