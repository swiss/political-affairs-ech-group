

## Classe: HasReferenceIdentification 


_Une classe mixin qui fournit les slots par lesquels une référence désigne l'entité vers laquelle elle pointe. Contrairement à `HasIdentification`, elle n'identifie pas l'objet référençant lui-même ; c'est pourquoi `global_uri` n'y est ni identifiant ni obligatoire : un système qui ne dispose que de l'identifiant local de l'entité référencée indique celui-ci. Une classe de référence utilisant ce mixin doit exiger au moins l'un des deux._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Identifiant local de l'entité référencée. Il est résolu au sein de la même livraison.  |
| global_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | L'URI unique et globalement valide de l'entité référencée. Contrairement à un local_id, elle est également résoluble au-delà de la livraison.  |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, p. ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans.  |



### Utilisation de mixin

[PersonReference](PersonReference.md), [GroupReference](GroupReference.md)





















</div>