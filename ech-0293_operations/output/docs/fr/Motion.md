

## Classe: Motion 


_Une proposition formelle déposée au cours des délibérations._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| title | 0..1 <br/> [String](String.md) | Titre de l'élément.  |
| description | 0..1 <br/> [String](String.md) | Texte descriptif de l'élément.  |
| documents | * <br/> [Work](Work.md) | Liste des documents (FRBR Works) liés à l'entité.  |






















</div>