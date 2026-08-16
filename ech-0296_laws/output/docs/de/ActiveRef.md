

## Klasse: ActiveRef 


_Verweis auf einen Erlass, den dieses Dokument ändert._



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 0..1 <br/> [EIdType](EIdType.md) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| href | 0..1 <br/> [String](String.md) | URI-Referenz (@href), für Links zu Organisationen, Rollen oder externen URIs. |
| show_as | 0..1 <br/> [String](String.md) | Lesbare Anzeigebezeichnung einer TLC-Referenz (@showAs). |
| element_type | 0..1 <br/> [String](String.md) | Typ-Diskriminator für die konkrete Unterklasse einer abstrakten Basis: InlineElement oder BlockElement. <br/><br/>Vererbung: [InlineElement](InlineElement.md) |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [References](References.md) | [active_refs](active_refs.md) | range | [ActiveRef](ActiveRef.md) |



















</div>