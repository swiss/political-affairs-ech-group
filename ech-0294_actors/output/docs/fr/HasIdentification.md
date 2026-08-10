

## Classe: HasIdentification 


_Une classe mixin qui fournit des slots pour l'identification d'une entité. Elle est utilisée pour les entités identifiées en propre ; leur `global_uri` constitue l'identifiant et est donc obligatoire._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil.  |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité.  |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q813067 pour Beat Jans.  |



### Utilisation de mixin

[Container](Container.md), [Person](Person.md), [Group](Group.md), [Membership](Membership.md), [InterestLink](InterestLink.md), [ElectoralDistrict](ElectoralDistrict.md)





















</div>