

## Klasse: TemporalData 


_Die Zeitgruppen, auf die sich eine Änderung bezieht. Jede Gruppe hält das Intervall, in dem sie gilt._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| source | 0..1 <br/> [AnchorRef](AnchorRef.md) | Anker-Referenz auf die verantwortliche Organisation (@source), z.B. '#ch.bk'. |
| temporal_groups | * <br/> [TemporalGroup](TemporalGroup.md) | Die Zeitgruppen (akn:temporalGroup). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [ActMeta](ActMeta.md) | [temporal_data_ref](temporal_data_ref.md) | range | [TemporalData](TemporalData.md) |



















</div>