

## Classe: JointDebate 


_Une délibération commune : plusieurs points de l'ordre du jour sont traités ensemble, par exemple des affaires connexes délibérées dans un seul et même débat. La délibération commune est rattachée à un point de l'ordre du jour (AgendaItem), à un point du procès-verbal (ProtocolItem), à une séance (Meeting) ou à une session (Session) et renvoie, par leurs identifiants, aux points traités conjointement. Rattachée à une séance ou à une session, elle peut aussi réunir des points répartis sur plusieurs positions de l'ordre du jour ou sur plusieurs séances._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| joint_agenda_item_ids | * <br/> [String](String.md) | Identifiants des points de l'ordre du jour traités conjointement (AgendaItem ou ProtocolItem).  |





### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Session](Session.md) | [joint_debates](joint_debates.md) | range | [JointDebate](JointDebate.md) |
| [Meeting](Meeting.md) | [joint_debates](joint_debates.md) | range | [JointDebate](JointDebate.md) |
| [IsAgendaItem](IsAgendaItem.md) | [joint_debates](joint_debates.md) | range | [JointDebate](JointDebate.md) |
| [AgendaItem](AgendaItem.md) | [joint_debates](joint_debates.md) | range | [JointDebate](JointDebate.md) |
| [ProtocolItem](ProtocolItem.md) | [joint_debates](joint_debates.md) | range | [JointDebate](JointDebate.md) |



















</div>