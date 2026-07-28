

## Classe: RoleType 


_Rôle d'une personne dans une affiliation ou une fonction (p. ex. membre, président, suppléant). Si un rôle ne figure pas dans le vocabulaire RoleEnum proposé, la valeur « other » peut être utilisée, et un libellé descriptif doit être fourni dans le slot `role_label`. Le libellé peut également être utilisé lorsqu'une désignation spécifique est nécessaire, même s'il existe une valeur sémantique appropriée dans `role_type_enum` ; il doit être fourni lorsque `role_type_enum` est réglé sur « other »._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| role_type_enum | 0..1 <br/> [RoleEnum](RoleEnum.md) | Rôle de la personne dans l'affiliation ou la fonction.  |
| role_label | 0..1 <br/> [String](String.md) | Libellé de rôle spécifique. À utiliser lorsqu'un nom de rôle spécifique est nécessaire, même s'il existe une valeur sémantique appropriée dans `role_type_enum` ; fournir ce libellé lorsque « role_type_enum » est réglé sur « other ».  |

##### Contraintes


Au moins l'un des champs suivants doit être renseigné :

- [role_type_enum](role_type_enum.md)
- [role_label](role_label.md)










### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](Membership.md) | [role_type](role_type.md) | range | [RoleType](RoleType.md) |




##### Règles


- Si le type de rôle est « other », un libellé descriptif doit être fourni.

















</div>