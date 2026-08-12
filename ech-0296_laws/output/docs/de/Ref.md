

## Klasse: Ref 


_Eine Inline-Referenz (akn:ref). Trägt @href, und bei internen SR-Querverweisen die Fedlex-Erweiterungsattribute fedlex:rs und fedlex:rs-uri._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| href | 0..1 <br/> [String](String.md) | URI-Referenz (@href), für Links zu Organisationen, Rollen oder externen URIs. |
| fedlex_rs | 0..1 <br/> [String](String.md) | Fedlex-Erweiterungsattribut fedlex:rs auf akn:ref: die SR-Nummer des referenzierten Erlasses (z.B. '641.20').  |
| fedlex_rs_uri | 0..1 <br/> [ELIURI](ELIURI.md) | Fedlex-Erweiterungsattribut fedlex:rs-uri auf akn:ref: die ELI-URI des SR-Eintrags des referenzierten Erlasses.  |
| inline_content | * <br/> [InlineElement](InlineElement.md) | Geordneter gemischter Inhalt: eine Folge aus Textabschnitten und Inline-Markup-Elementen (InlineElement-Subklassen). Die Dokumentreihenfolge wird durch die Listenreihenfolge bewahrt.  |
| element_type | 0..1 <br/> [String](String.md) | Typ-Diskriminator für die konkrete InlineElement-Subklasse.<br/><br/>Vererbung: [InlineElement](InlineElement.md) |






















</div>