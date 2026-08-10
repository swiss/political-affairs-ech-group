

## Classe: PersonReference 


_Référence abrégée à une personne avec les principales données d'identification au moment de la liaison. Préserve l'exactitude historique même si la personne change ultérieurement. La personne référencée est désignée par `local_id` ou `global_uri` ; au moins l'un des deux est requis._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Identifiant local de l'entité référencée. Il est résolu au sein de la même livraison. <br/><br/>Héritage : [HasReferenceIdentification](HasReferenceIdentification.md) |
| global_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | L'URI unique et globalement valide de l'entité référencée. Contrairement à un local_id, elle est également résoluble au-delà de la livraison. <br/><br/>Héritage : [HasReferenceIdentification](HasReferenceIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, p. ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasReferenceIdentification](HasReferenceIdentification.md) |
| label | 1 <br/> [String](String.md) | Nom d'affichage court obligatoire permettant d'identifier la personne au sein de l'organisation (par ex. avec l'ajout de l'année de naissance afin de distinguer les personnes portant le même nom).  |
| label_long | 0..1 <br/> [String](String.md) | Nom d'affichage long facultatif comprenant les titres académiques et le nom officiel complet (par ex. « Dr. Maria Muster-Beispiel »).  |
| group_label | 0..1 <br/> [String](String.md) | Nom de l'organe/du groupe au moment de la liaison.  |

##### Contraintes


Au moins l'un des champs suivants doit être renseigné :

- [local_id](local_id.md)
- [global_uri](global_uri.md)










### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [IndividualVote](IndividualVote.md) | [actor_id](actor_id.md) | range | [PersonReference](PersonReference.md) |
| [IndividualAttendance](IndividualAttendance.md) | [actor_id](actor_id.md) | range | [PersonReference](PersonReference.md) |
| [Speech](Speech.md) | [actor_id](actor_id.md) | range | [PersonReference](PersonReference.md) |



















</div>