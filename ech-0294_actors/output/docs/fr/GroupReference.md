

## Classe: GroupReference 


_Référence légère à un groupe avec les principales données d'identification au moment de la liaison._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| label | 0..1 <br/> [String](String.md) | Attribuer un label à une information structurée (par ex. nom d'affichage, poste, etc.).  |
| abbreviation | * <br/> [MultilingualValue](MultilingualValue.md) | Abréviation (peut être multilingue).  |
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q39 pour la Suisse. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |





### Utilisations

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Membership](Membership.md) | [group_reference](group_reference.md) | range | [GroupReference](GroupReference.md) |



















</div>