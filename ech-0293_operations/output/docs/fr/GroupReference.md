

## Classe: GroupReference 


_Référence abrégée à un groupe avec les principales données d'identification au moment de la liaison. Le groupe référencé est désigné par `local_id` ou `global_uri` ; au moins l'un des deux est requis. Un `local_id` est résolu au sein de la même livraison, un `global_uri` également au-delà._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| label | 0..1 <br/> [String](String.md) | Attribuer un label à une information structurée (par ex. nom d'affichage, poste, etc.).  |
| abbreviation | * <br/> [MultilingualValue](MultilingualValue.md) | Abréviation (peut être multilingue).  |
| local_id | 0..1 <br/> [String](String.md) | Identifiant local de l'entité référencée. Il est résolu au sein de la même livraison. <br/><br/>Héritage : [HasReferenceIdentification](HasReferenceIdentification.md) |
| global_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | L'URI unique et globalement valide de l'entité référencée. Contrairement à un local_id, elle est également résoluble au-delà de la livraison. <br/><br/>Héritage : [HasReferenceIdentification](HasReferenceIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, p. ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasReferenceIdentification](HasReferenceIdentification.md) |

##### Contraintes


Au moins l'un des champs suivants doit être renseigné :

- [local_id](local_id.md)
- [global_uri](global_uri.md)










### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Legislature](Legislature.md) | [actor_id](actor_id.md) | range | [GroupReference](GroupReference.md) |
| [Meeting](Meeting.md) | [group_id](group_id.md) | range | [GroupReference](GroupReference.md) |
| [Meeting](Meeting.md) | [actor_id](actor_id.md) | range | [GroupReference](GroupReference.md) |
| [Voting](Voting.md) | [actor_id](actor_id.md) | range | [GroupReference](GroupReference.md) |
| [Election](Election.md) | [actor_id](actor_id.md) | range | [GroupReference](GroupReference.md) |
| [Attendance](Attendance.md) | [actor_id](actor_id.md) | range | [GroupReference](GroupReference.md) |



















</div>