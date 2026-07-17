---
search:
  boost: 5.0
---

# Slot: wikidata_uri 


_Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q39 pour la Suisse._

__



<div data-search-exclude markdown="1">



URI: [mcm:wikidataUri](https://ld.ech.ch/schema/0292/meta-common/wikidataUri)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [HasIdentification](HasIdentification.md) | Une classe mixin qui fournit des slots pour l'identification d'une entité |  no  |
| [IsProcessStep](IsProcessStep.md) | Une classe mixin pour une étape unique dans un processus |  no  |
| [Container](Container.md) | Conteneur pour les acteurs politiques, les groupes et les relations |  no  |
| [Person](Person.md) | Une personne avec des identifiants, des noms, des adresses, des nationalités ... |  no  |
| [Group](Group.md) | Un groupe, une organisation ou une collectivité politique (p |  no  |
| [Membership](Membership.md) | Une relation d'affiliation entre une personne et un groupe, représentant une ... |  no  |
| [InterestLink](InterestLink.md) | Un lien d'intérêts (conflit d'intérêts, financement politique) d'une personne... |  no  |
| [PersonReference](PersonReference.md) | Référence légère à une personne avec les principales données d'identification... |  no  |
| [GroupReference](GroupReference.md) | Référence légère à un groupe avec les principales données d'identification au... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Uriorcurie](Uriorcurie.md) |
| Domaine de | [HasIdentification](HasIdentification.md), [IsProcessStep](IsProcessStep.md) |
| URI du slot | [mcm:wikidataUri](https://ld.ech.ch/schema/0292/meta-common/wikidataUri) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: wikidata_uri
annotations:
  description_de:
    tag: description_de
    value: 'Eine URI, die auf eine Wikidata-Entität verweist, z.B. http://www.wikidata.org/entity/Q39
      für die Schweiz.

      '
  description_fr:
    tag: description_fr
    value: 'Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q39
      pour la Suisse.

      '
description: 'Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q39
  pour la Suisse.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:wikidataUri
domain_of:
- HasIdentification
- IsProcessStep
range: uriorcurie

```
</details></div>