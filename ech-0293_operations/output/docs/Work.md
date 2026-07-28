

## Class: Work 

<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
| ---  | --- | --- |
| id | 1 <br/> [String](String.md) | None |
| work_type | 0..1 <br/> [WorkTypesEnum](WorkTypesEnum.md) | None |
| document_category | 0..1 <br/> [DocumentCategoryEnum](DocumentCategoryEnum.md) | [de] Kategorie des Dokuments. Wenn nicht gesetzt, wird automatisch 'other' verwendet. [en] Category of the document. If not set, 'other' is automatically used.  |
| expressions | * <br/> [Expression](Expression.md) | None |





### Usages

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