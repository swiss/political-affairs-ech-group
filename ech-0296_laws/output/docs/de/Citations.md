

## Klasse: Citations 


_Die Erwägungen des Vorspruchs — worauf sich der Erlass beruft._



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 0..1 <br/> [EIdType](EIdType.md) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| citation_list | * <br/> [Citation](Citation.md) | Die Erwägungen selbst (akn:citation). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Preamble](Preamble.md) | [citations_ref](citations_ref.md) | range | [Citations](Citations.md) |



















</div>