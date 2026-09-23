---
search:
  boost: 5.0
---

# Slot: total_absent 


_Anzahl abwesender Mitglieder, die nicht teilnehmen konnten. Ob eine Abwesenheit entschuldigt war, hält die Anwesenheitsliste (Attendance) fest._




<div data-search-exclude markdown="1">



URI: [ops:total_absent](https://ch.paf.link/schema/operations/total_absent)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Voting](Voting.md) | Eine Abstimmung über eine Sachfrage: der Abstimmungsgegenstand (Frage), das V... |  no  |
| [Election](Election.md) | Eine Wahl, mit der ein parlamentarisches Organ eine oder mehrere Personen für... |  no  |
| [Attendance](Attendance.md) | Aggregierte Anwesenheitsliste für eine Sitzung (Anzahl Anwesende, Abwesende, ... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Integer](Integer.md) |
| Domäne von | [Voting](Voting.md), [Election](Election.md), [Attendance](Attendance.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

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
description: 'Anzahl abwesender Mitglieder, die nicht teilnehmen konnten. Ob eine
  Abwesenheit entschuldigt war, hält die Anwesenheitsliste (Attendance) fest.

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