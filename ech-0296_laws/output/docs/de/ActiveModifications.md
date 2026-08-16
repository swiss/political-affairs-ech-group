

## Klasse: ActiveModifications 


_Die Änderungen, die dieser Erlass an anderen vornimmt._



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| source | 0..1 <br/> [AnchorRef](AnchorRef.md) | Anker-Referenz auf die verantwortliche Organisation (@source), z.B. '#ch.bk'. |
| modifications | * <br/> [Modification](Modification.md) | Die Änderungen in der Reihenfolge ihrer Aufzeichnung (akn:textualMod, akn:forceMod). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Analysis](Analysis.md) | [active_modifications](active_modifications.md) | range | [ActiveModifications](ActiveModifications.md) |



















</div>