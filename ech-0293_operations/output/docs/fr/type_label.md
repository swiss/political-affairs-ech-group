---
search:
  boost: 5.0
---

# Slot: type_label 


_Libellé de type personnalisé lorsque les valeurs de type standard ne s'appliquent pas._




<div data-search-exclude markdown="1">



URI: [ops:type_label](https://ch.paf.link/schema/operations/type_label)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Resolution](Resolution.md) | Une décision prise sur un point de l'ordre du jour, y compris les procédures ... |  no  |
| [Voting](Voting.md) | Une procédure de vote avec les voix individuelles et les résultats |  no  |
| [IndividualVote](IndividualVote.md) | Une voix individuelle exprimée par un membre lors d'une procédure de vote |  no  |
| [Election](Election.md) | Une procédure d'élection visant à pourvoir des fonctions par des personnes |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Resolution](Resolution.md), [Voting](Voting.md), [IndividualVote](IndividualVote.md), [Election](Election.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: type_label
annotations:
  description_de:
    tag: description_de
    value: 'Benutzerdefinierte Typbezeichnung, wenn Standardtypwerte nicht zutreffen.

      '
  description_fr:
    tag: description_fr
    value: 'Libellé de type personnalisé lorsque les valeurs de type standard ne s''appliquent
      pas.

      '
description: 'Libellé de type personnalisé lorsque les valeurs de type standard ne
  s''appliquent pas.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Resolution
- Voting
- IndividualVote
- Election
range: string

```
</details></div>