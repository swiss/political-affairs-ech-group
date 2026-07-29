---
search:
  boost: 5.0
---

# Slot: tie_breaker 


_Indique si une voix prépondérante a été utilisée lors du vote._




<div data-search-exclude markdown="1">



URI: [ops:tie_breaker](https://ch.paf.link/schema/operations/tie_breaker)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Voting](Voting.md) | Une procédure de vote avec les voix individuelles et les résultats |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Boolean](Boolean.md) |
| Domaine de | [Voting](Voting.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: tie_breaker
annotations:
  description_de:
    tag: description_de
    value: 'Gibt an, ob ein Stichentscheid bei der Abstimmung verwendet wurde.

      '
  description_fr:
    tag: description_fr
    value: 'Indique si une voix prépondérante a été utilisée lors du vote.

      '
description: 'Indique si une voix prépondérante a été utilisée lors du vote.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
range: boolean

```
</details></div>