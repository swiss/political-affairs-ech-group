

## Classe: Work 


_FRBR Work : le document abstrait en tant que tel, indépendamment d'une version linguistique ou d'un format de fichier concrets._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| id | 1 <br/> [String](String.md) | Identifiant univoque de l'élément.  |
| work_type | 0..1 <br/> [WorkTypesEnum](WorkTypesEnum.md) | Type de document (p. ex. procès-verbal, version déposée, droit en vigueur).  |
| document_category | 0..1 <br/> [DocumentCategoryEnum](DocumentCategoryEnum.md) | Catégorie du document. Si elle n'est pas renseignée, la valeur 'other' est utilisée automatiquement.  |
| expressions | * <br/> [Expression](Expression.md) | Les versions linguistiques (Expressions) d'un Work.  |





### Utilisations

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