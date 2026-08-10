

## Classe: Resolution 


_Une décision prise sur un point de l'ordre du jour, y compris les procédures de vote._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| resolution_type | 0..1 <br/> [ResolutionTypeEnum](ResolutionTypeEnum.md) | Type de décision prise sur le point de l'ordre du jour.  |
| type_label | 0..1 <br/> [String](String.md) | Libellé de type personnalisé lorsque les valeurs de type standard ne s'appliquent pas.  |
| vote_procedures | * <br/> [String](String.md) | Modalités du vote, p. ex. vote secret ou vote ouvert.  |
| documents | * <br/> [Work](Work.md) | Liste des documents (FRBR Works) liés à l'entité.  |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [resolutions](resolutions.md) | range | [Resolution](Resolution.md) |
| [AgendaItem](AgendaItem.md) | [has_resolution](has_resolution.md) | range | [Resolution](Resolution.md) |
| [ProtocolItem](ProtocolItem.md) | [has_resolution](has_resolution.md) | range | [Resolution](Resolution.md) |



















</div>