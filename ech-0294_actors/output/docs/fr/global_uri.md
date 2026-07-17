---
search:
  boost: 5.0
---

# Slot: global_uri 


_A unique, globally valid URI for the entity._

__



<div data-search-exclude markdown="1">



URI: [mcm:globalURI](https://ld.ech.ch/schema/0292/meta-common/globalURI)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [HasIdentification](HasIdentification.md) | A mixin class that provides slots for the identification of an entity |  no  |
| [IsProcessStep](IsProcessStep.md) | A mixin class for a single step in a multi-stage process (e |  no  |
| [Container](Container.md) | Container for political actors, groups, and relationships |  no  |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |
| [Group](Group.md) | A political group, organization, or body (e |  no  |
| [Membership](Membership.md) | A membership relationship between a person and a group, representing formal a... |  no  |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |
| [PersonReference](PersonReference.md) | Lightweight reference to a person with key identification data at time of lin... |  no  |
| [GroupReference](GroupReference.md) | Lightweight reference to a group with key identification data at time of link... |  no  |






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
description: 'A unique, globally valid URI for the entity.

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