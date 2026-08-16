

## Klasse: TimeInterval 


_Ein Intervall zwischen zwei Daten. Anfang und Ende benennen Datumselemente im Dokument über einen Anker, statt das Datum selbst zu tragen; ein leeres Ende heisst, dass das Intervall offen ist._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| eId | 0..1 <br/> [EIdType](EIdType.md) | Eindeutiger Element-Identifier im Dokument (@eId). Vom Fedlex Schematron gefordert bei allen Hierarchieelementen, Artikeln, Unterabschnitten und Absätzen. Folgt der AKN-eId-Namenskonvention (hierarchische Pfadnotation), z.B. 'ti_1', 'ch_1', 'art_1', 'art_1-para_1'.  |
| refers_to | 0..1 <br/> [String](String.md) | Anker, der nennt, worauf sich das Element bezieht (@refersTo). |
| start_ref | 0..1 <br/> [String](String.md) | Anker des Datums, an dem das Intervall beginnt (@start). |
| end_ref | 0..1 <br/> [String](String.md) | Anker des Datums, an dem das Intervall endet (@end); leer, solange es offen ist. |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [TemporalGroup](TemporalGroup.md) | [time_intervals](time_intervals.md) | range | [TimeInterval](TimeInterval.md) |



















</div>