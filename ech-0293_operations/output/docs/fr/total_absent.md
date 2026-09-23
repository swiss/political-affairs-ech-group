---
search:
  boost: 5.0
---

# Slot: total_absent 


_Nombre de membres absents qui n'ont pas pu participer. La liste de présence (Attendance) indique si une absence était excusée._




<div data-search-exclude markdown="1">



URI: [ops:total_absent](https://ch.paf.link/schema/operations/total_absent)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Voting](Voting.md) | Un vote sur une question matérielle : l'objet du vote (la question), la procé... |  no  |
| [Election](Election.md) | Une élection par laquelle un organe parlementaire désigne une ou plusieurs pe... |  no  |
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
    value: 'Anzahl abwesender Mitglieder, die nicht teilnehmen konnten. Ob eine Abwesenheit
      entschuldigt war, hält die Anwesenheitsliste (Attendance) fest.

      '
  description_fr:
    tag: description_fr
    value: 'Nombre de membres absents qui n''ont pas pu participer. La liste de présence
      (Attendance) indique si une absence était excusée.

      '
description: 'Nombre de membres absents qui n''ont pas pu participer. La liste de
  présence (Attendance) indique si une absence était excusée.

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