---
search:
  boost: 5.0
---

# Slot: majority_type 


_Type de majorité requise pour le vote (absolue, deux tiers, etc.)._




<div data-search-exclude markdown="1">



URI: [ops:majority_type](https://ch.paf.link/schema/operations/majority_type)
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
| Plage | [MajorityTypeEnum](MajorityTypeEnum.md) |
| Domaine de | [Voting](Voting.md), [Election](Election.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |









## Exemples

| Valeur |
| --- |
| absolute |
| other |





## Source LinkML

<details>
```yaml
name: majority_type
annotations:
  description_de:
    tag: description_de
    value: 'Art der für die Abstimmung erforderlichen Mehrheit (absolut, Zweidrittel
      usw.).

      '
  description_fr:
    tag: description_fr
    value: 'Type de majorité requise pour le vote (absolue, deux tiers, etc.).

      '
description: 'Type de majorité requise pour le vote (absolue, deux tiers, etc.).

  '
examples:
- value: absolute
- value: other
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
- Election
range: MajorityTypeEnum

```
</details></div>