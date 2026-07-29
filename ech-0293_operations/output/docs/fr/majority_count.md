---
search:
  boost: 5.0
---

# Slot: majority_count 


_Nombre de voix requis pour atteindre le seuil de majorité déterminant._




<div data-search-exclude markdown="1">



URI: [ops:majority_count](https://ch.paf.link/schema/operations/majority_count)
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
name: majority_count
annotations:
  description_de:
    tag: description_de
    value: 'Anzahl der Stimmen, die für die relevante Mehrheitsschwelle erforderlich
      sind.

      '
  description_fr:
    tag: description_fr
    value: 'Nombre de voix requis pour atteindre le seuil de majorité déterminant.

      '
description: 'Nombre de voix requis pour atteindre le seuil de majorité déterminant.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
- Election
range: integer

```
</details></div>