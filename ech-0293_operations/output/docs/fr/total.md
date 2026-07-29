---
search:
  boost: 5.0
---

# Slot: total 


_Nombre total de voix, sans les absents ni la voix de la présidence._




<div data-search-exclude markdown="1">



URI: [ops:total](https://ch.paf.link/schema/operations/total)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Voting](Voting.md) | Une procédure de vote avec les voix individuelles et les résultats |  no  |
| [Election](Election.md) | Une procédure d'élection visant à pourvoir des fonctions par des personnes |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Integer](Integer.md) |
| Domaine de | [Voting](Voting.md), [Election](Election.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: total
annotations:
  description_de:
    tag: description_de
    value: 'Gesamtzahl der Stimmen, ohne abwesende und Präsidiumsstimmen.

      '
  description_fr:
    tag: description_fr
    value: 'Nombre total de voix, sans les absents ni la voix de la présidence.

      '
description: 'Nombre total de voix, sans les absents ni la voix de la présidence.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
- Election
range: integer

```
</details></div>