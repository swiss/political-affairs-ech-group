

## Klasse: Work 


_FRBR Work: das abstrakte Dokument als solches, unabhängig von einer konkreten Sprachfassung oder einem Dateiformat._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| id | 1 <br/> [String](String.md) | Eindeutiger Identifikator des Elements.  |
| work_type | 0..1 <br/> [WorkTypesEnum](WorkTypesEnum.md) | Art des Dokuments (z.B. Protokoll, eingereichte Fassung, geltendes Recht).  |
| document_category | 0..1 <br/> [DocumentCategoryEnum](DocumentCategoryEnum.md) | Kategorie des Dokuments. Wenn nicht gesetzt, wird automatisch 'other' verwendet.  |
| expressions | * <br/> [Expression](Expression.md) | Die Sprachfassungen (Expressions) eines Works.  |





### Verwendungen

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Legislature](Legislature.md) | [documents](documents.md) | range | [Work](Work.md) |
| [Session](Session.md) | [documents](documents.md) | range | [Work](Work.md) |
| [Meeting](Meeting.md) | [documents](documents.md) | range | [Work](Work.md) |
| [AgendaItem](AgendaItem.md) | [documents](documents.md) | range | [Work](Work.md) |
| [Protocol](Protocol.md) | [documents](documents.md) | range | [Work](Work.md) |
| [ProtocolItem](ProtocolItem.md) | [documents](documents.md) | range | [Work](Work.md) |
| [Resolution](Resolution.md) | [documents](documents.md) | range | [Work](Work.md) |
| [Voting](Voting.md) | [documents](documents.md) | range | [Work](Work.md) |
| [Election](Election.md) | [documents](documents.md) | range | [Work](Work.md) |
| [Speech](Speech.md) | [documents](documents.md) | range | [Work](Work.md) |
| [Motion](Motion.md) | [documents](documents.md) | range | [Work](Work.md) |
| [WorkContainer](WorkContainer.md) | [works](works.md) | range | [Work](Work.md) |



















</div>