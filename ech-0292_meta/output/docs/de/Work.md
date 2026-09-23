

## Klasse: Work 


_FRBR Work: das abstrakte Dokument als solches, unabhängig von einer konkreten Sprachfassung oder einem Dateiformat._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| id | 1 <br/> [String](String.md) | Eindeutiger Identifikator des Elements.  |
| document_category | 0..1 <br/> [DocumentCategoryEnum](DocumentCategoryEnum.md) | Kategorie des Dokuments. Wenn nicht gesetzt, wird automatisch 'other' verwendet.  |
| expressions | * <br/> [Expression](Expression.md) | Die Sprachfassungen (Expressions) eines Works.  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [WorkContainer](WorkContainer.md) | [works](works.md) | range | [Work](Work.md) |



















</div>