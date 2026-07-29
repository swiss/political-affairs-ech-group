---
search:
  boost: 5.0
---

# Slot: total_absent 


_Gesamtzahl abwesender Mitglieder. Unterscheidung zwischen abwesend/entschuldigt abwesend - Anwesenheit wird auf Anwesenheitsliste verfolgt._




<div data-search-exclude markdown="1">



URI: [ops:total_absent](https://ch.paf.link/schema/operations/total_absent)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Voting](Voting.md) | Ein Abstimmungsverfahren mit Einzelstimmen und Ergebnissen |  no  |
| [Election](Election.md) | Ein Wahlverfahren zur Wahl von Personen in Positionen |  no  |
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
    value: 'Gesamtzahl abwesender Mitglieder. Unterscheidung zwischen abwesend/entschuldigt
      abwesend - Anwesenheit wird auf Anwesenheitsliste verfolgt.

      '
  description_fr:
    tag: description_fr
    value: 'Nombre total de membres absents. La distinction entre absent et absent
      excusé se fait dans la liste de présence.

      '
description: 'Gesamtzahl abwesender Mitglieder. Unterscheidung zwischen abwesend/entschuldigt
  abwesend - Anwesenheit wird auf Anwesenheitsliste verfolgt.

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