

## Classe: PersonReference 


_Référence légère à une personne avec les principales données d'identification au moment de la liaison. Préserve l'exactitude historique même si la personne change ultérieurement._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| label | 1 <br/> [String](String.md) | Nom d'affichage court obligatoire permettant d'identifier la personne au sein de l'organisation (par ex. avec l'ajout de l'année de naissance afin de distinguer les personnes portant le même nom).  |
| label_long | 0..1 <br/> [String](String.md) | Nom d'affichage long facultatif comprenant les titres académiques et le nom officiel complet (par ex. « Dr. Maria Muster-Beispiel »).  |
| group_label | 0..1 <br/> [String](String.md) | Nom de l'organe/du groupe au moment de la liaison.  |
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q39 pour la Suisse. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](Membership.md) | [person_reference](person_reference.md) | range | [PersonReference](PersonReference.md) |
| [InterestLink](InterestLink.md) | [person_reference](person_reference.md) | range | [PersonReference](PersonReference.md) |



















</div>