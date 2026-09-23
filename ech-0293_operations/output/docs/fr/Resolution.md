

## Classe: Resolution 


_La décision formelle prise sur un point de l'ordre du jour, y compris les procédures de vote appliquées. Elle retient ce qui a été décidé, tandis que Voting retient comment il a été décidé (procédure et rapport de voix). Toute décision ne repose pas sur un vote formel : les prises de connaissance, les adoptions tacites ou les décisions administratives interviennent sans vote._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| resolution_type | 0..1 <br/> [ResolutionTypeEnum](ResolutionTypeEnum.md) | Type de décision prise sur le point de l'ordre du jour.  |
| type_label | 0..1 <br/> [String](String.md) | Libellé de type personnalisé lorsque les valeurs de type standard ne s'appliquent pas.  |
| vote_procedures | * <br/> [String](String.md) | Procédures selon lesquelles le vote a eu lieu. Procédures ouvertes : main levée, assis-debout, vote électronique, appel nominal et, en situation de crise, vote à distance (voix communiquées à l'avance à la présidence et saisies en même temps que le vote au conseil), procédure par voie de circulation ou vote lors de séances virtuelles. Procédures secrètes : bulletin de vote, vote électronique secret. La procédure détermine si les voix individuelles peuvent être saisies.  |
| documents | * <br/> [Work](Work.md) | Liste des documents (FRBR Works) liés à l'entité.  |





### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Container](Container.md) | [resolutions](resolutions.md) | range | [Resolution](Resolution.md) |
| [IsAgendaItem](IsAgendaItem.md) | [has_resolution](has_resolution.md) | range | [Resolution](Resolution.md) |
| [AgendaItem](AgendaItem.md) | [has_resolution](has_resolution.md) | range | [Resolution](Resolution.md) |
| [ProtocolItem](ProtocolItem.md) | [has_resolution](has_resolution.md) | range | [Resolution](Resolution.md) |



















</div>