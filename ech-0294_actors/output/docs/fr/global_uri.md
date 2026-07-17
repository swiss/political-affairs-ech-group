---
search:
  boost: 5.0
---

# Slot: global_uri 


_Une URI unique et globalement valide pour l'entité._

__



<div data-search-exclude markdown="1">



URI: [mcm:globalURI](https://ld.ech.ch/schema/0292/meta-common/globalURI)
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
| URI du slot | [mcm:globalURI](https://ld.ech.ch/schema/0292/meta-common/globalURI) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Requis | Yes |
### Caractéristiques du slot

| Propriété | Valeur |
| --- | --- |
| Identifiant | Yes |














## Source LinkML

<details>
```yaml
name: global_uri
annotations:
  description_de:
    tag: description_de
    value: 'Eine eindeutige, global gültige URI für die Entität.

      '
  description_fr:
    tag: description_fr
    value: 'Une URI unique et globalement valide pour l''entité.

      '
description: 'Une URI unique et globalement valide pour l''entité.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:globalURI
identifier: true
domain_of:
- HasIdentification
- IsProcessStep
range: uriorcurie
required: true

```
</details></div>