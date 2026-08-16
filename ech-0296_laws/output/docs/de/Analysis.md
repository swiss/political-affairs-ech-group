

## Klasse: Analysis 


_Der Analyseblock: welche Änderungen dieser Erlass vornimmt und erfährt. Fedlex verwendet ihn nicht; kantonale Sammlungen halten hier ihre Änderungen fest._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| source | 0..1 <br/> [AnchorRef](AnchorRef.md) | Anker-Referenz auf die verantwortliche Organisation (@source), z.B. '#ch.bk'. |
| active_modifications | 0..1 <br/> [ActiveModifications](ActiveModifications.md) | Die Änderungen, die dieser Erlass an anderen vornimmt (akn:activeModifications). |
| passive_modifications | 0..1 <br/> [PassiveModifications](PassiveModifications.md) | Die Änderungen, die andere Erlasse an diesem vornehmen (akn:passiveModifications). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [ActMeta](ActMeta.md) | [analysis_ref](analysis_ref.md) | range | [Analysis](Analysis.md) |



















</div>