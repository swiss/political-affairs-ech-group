

## Klasse: TemporalGroup 


_Ein benannter Zeitraum, auf den sich eine Änderung über @period bezieht._



<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 0..1 <br/> [EIdType](EIdType.md) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| time_intervals | * <br/> [TimeInterval](TimeInterval.md) | Die Intervalle dieser Gruppe (akn:timeInterval). |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [TemporalData](TemporalData.md) | [temporal_groups](temporal_groups.md) | range | [TemporalGroup](TemporalGroup.md) |



















</div>