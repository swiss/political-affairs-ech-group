---
search:
  boost: 5.0
---

# Slot: optional 


_Indique si la séance ou le vote est facultatif._




<div data-search-exclude markdown="1">



URI: [ops:optional](https://ch.paf.link/schema/operations/optional)
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
name: optional
annotations:
  description_de:
    tag: description_de
    value: 'Gibt an, ob die Sitzung oder Abstimmung optional ist.

      '
  description_fr:
    tag: description_fr
    value: 'Indique si la séance ou le vote est facultatif.

      '
description: 'Indique si la séance ou le vote est facultatif.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
range: boolean

```
</details></div>