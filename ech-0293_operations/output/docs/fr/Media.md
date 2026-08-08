

## Classe: Media 


_Fichiers médias ou documents (y compris les procès-verbaux en PDF/HTML/WORD ou les liens vers des contenus audio/vidéo)._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans. <br/><br/>Héritage : [HasIdentification](HasIdentification.md) |
| title | 0..1 <br/> [String](String.md) | Titre de l'élément.  |
| media_type | 0..1 <br/> [String](String.md) | Type de média (audio, vidéo, document).  |
| url | * <br/> [MultilingualString](MultilingualString.md) | Page d'accueil ou adresse web complémentaire, multilingue.  |
| version | 0..1 <br/> [String](String.md) | Numéro ou identifiant de version.  |
| parent_type | 0..1 <br/> [String](String.md) | Type de l'objet parent (séance, point de l'ordre du jour, intervention, affaire).  |






















</div>