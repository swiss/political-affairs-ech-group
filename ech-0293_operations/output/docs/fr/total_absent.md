---
search:
  boost: 5.0
---

# Slot: total_absent 


_Nombre total de membres absents. La distinction entre absent et absent excusé se fait dans la liste de présence._




<div data-search-exclude markdown="1">



URI: [ops:total_absent](https://ch.paf.link/schema/operations/total_absent)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Voting](Voting.md) | Une procédure de vote avec les voix individuelles et les résultats |  no  |
| [Election](Election.md) | Une procédure d'élection visant à pourvoir des fonctions par des personnes |  no  |
| [Attendance](Attendance.md) | Liste de présence agrégée pour une séance (nombre de membres présents, absent... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Integer](Integer.md) |
| Domaine de | [Voting](Voting.md), [Election](Election.md), [Attendance](Attendance.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: total_absent
annotations:
  description_de:
    tag: description_de
    value: 'Gesamtzahl abwesender Mitglieder. Unterscheidung zwischen abwesend/entschuldigt
      abwesend - Anwesenheit wird auf Anwesenheitsliste verfolgt.

      '
  description_fr:
    tag: description_fr
    value: 'Nombre total de membres absents. La distinction entre absent et absent
      excusé se fait dans la liste de présence.

      '
description: 'Nombre total de membres absents. La distinction entre absent et absent
  excusé se fait dans la liste de présence.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
- Election
- Attendance
range: integer

```
</details></div>