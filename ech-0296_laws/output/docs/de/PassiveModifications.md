

## Klasse: PassiveModifications 


_Die Änderungen, die andere Erlasse an diesem vornehmen._



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| source | 0..1 <br/> [AnchorRef](AnchorRef.md) | Anker-Referenz auf die verantwortliche Organisation (@source), z.B. '#ch.bk'. |
| modifications | * <br/> [Modification](Modification.md) | Die Änderungen in der Reihenfolge ihrer Aufzeichnung (akn:textualMod, akn:forceMod). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Analysis](Analysis.md) | [passive_modifications](passive_modifications.md) | range | [PassiveModifications](PassiveModifications.md) |



















</div>