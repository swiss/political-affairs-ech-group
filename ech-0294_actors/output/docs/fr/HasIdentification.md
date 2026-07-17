

## Classe: HasIdentification 


_Une classe mixin qui fournit des slots pour l'identification d'une entité._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil.  |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité.  |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q39 pour la Suisse.  |



### Utilisation de mixin

| mixed into | description |
| --- | --- |
| [Container](Container.md) | Conteneur pour les acteurs politiques, les groupes et les relations |
| [Person](Person.md) | Une personne avec des identifiants, des noms, des adresses, des nationalités ... |
| [Group](Group.md) | Un groupe, une organisation ou une collectivité politique (p |
| [Membership](Membership.md) | Une relation d'affiliation entre une personne et un groupe, représentant une ... |
| [InterestLink](InterestLink.md) | Un lien d'intérêts (conflit d'intérêts, financement politique) d'une personne... |
| [PersonReference](PersonReference.md) | Référence légère à une personne avec les principales données d'identification... |
| [GroupReference](GroupReference.md) | Référence légère à un groupe avec les principales données d'identification au... |





















</div>