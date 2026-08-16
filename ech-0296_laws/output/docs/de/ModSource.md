

## Klasse: ModSource 


_Die Stelle, welche die Änderung bewirkt._



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 0..1 <br/> [EIdType](EIdType.md) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| href | 0..1 <br/> [String](String.md) | URI-Referenz (@href), für Links zu Organisationen, Rollen oder externen URIs. |
| pos | 0..1 <br/> [String](String.md) | Lage der Änderung zum Ziel (@pos), z.B. „before“. |
| up_to | 0..1 <br/> [String](String.md) | Ende eines Zielbereichs (@upTo). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [TextualMod](TextualMod.md) | [mod_sources](mod_sources.md) | range | [ModSource](ModSource.md) |
| [ForceMod](ForceMod.md) | [mod_sources](mod_sources.md) | range | [ModSource](ModSource.md) |



















</div>