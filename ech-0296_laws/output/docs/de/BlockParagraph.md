

## Klasse: BlockParagraph 


_Ein Fliesstext-Absatz in Content (akn:p). Kann gemischten Inhalt mit Inline-Markup enthalten (XmlContent-Typ). Hinweis: akn:br ist hier nicht erlaubt, nur in Überschriften (FLX-TXT-001)._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| fedlex_role | 0..1 <br/> [FedlexRoleEnum](FedlexRoleEnum.md) | Fedlex-Erweiterungsattribut fedlex:role. FLX-XF-003 lässt 'marginal' (nur an akn:level, FLX-XF-004) und 'reference' (nur an akn:subheading, FLX-XF-005) zu; die publizierte Bundesverfassung führt zusätzlich 'heading' an einem Präambel-Absatz.  |
| inline_content | * <br/> [InlineElement](InlineElement.md) | Geordneter gemischter Inhalt: eine Folge aus Textabschnitten und Inline-Markup-Elementen (InlineElement-Subklassen). Die Dokumentreihenfolge wird durch die Listenreihenfolge bewahrt.  |
| element_type | 0..1 <br/> [String](String.md) | Typ-Diskriminator für die konkrete Unterklasse einer abstrakten Basis: InlineElement oder BlockElement. <br/><br/>Vererbung: [BlockElement](BlockElement.md) |






















</div>