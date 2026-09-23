

## Classe: JointDebate 


_Une délibération commune : plusieurs points de l'ordre du jour sont traités ensemble. La délibération commune est rattachée à un point de l'ordre du jour (AgendaItem) ou à un point du procès-verbal (ProtocolItem) et renvoie, par leurs identifiants, aux points traités conjointement._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| joint_agenda_item_ids | * <br/> [String](String.md) | Identifiants des points de l'ordre du jour traités conjointement (AgendaItem ou ProtocolItem).  |





### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [IsAgendaItem](IsAgendaItem.md) | [joint_debates](joint_debates.md) | range | [JointDebate](JointDebate.md) |
| [AgendaItem](AgendaItem.md) | [joint_debates](joint_debates.md) | range | [JointDebate](JointDebate.md) |
| [ProtocolItem](ProtocolItem.md) | [joint_debates](joint_debates.md) | range | [JointDebate](JointDebate.md) |



















</div>