---
search:
  boost: 5.0
---

# Slot: datetime_begin 


_La date et l'heure auxquelles la séance ou le vote commence._




<div data-search-exclude markdown="1">



URI: [ops:datetime_begin](https://ch.paf.link/schema/operations/datetime_begin)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Voting](Voting.md) | Une procédure de vote avec les voix individuelles et les résultats |  no  |
| [Election](Election.md) | Une procédure d'élection visant à pourvoir des fonctions par des personnes |  no  |
| [Attendance](Attendance.md) | Liste de présence agrégée pour une séance (nombre de membres présents, absent... |  no  |
| [Speech](Speech.md) | Une intervention prononcée au cours d'une séance (également appelée prise de ... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Datetime](Datetime.md) |
| Domaine de | [Voting](Voting.md), [Election](Election.md), [Attendance](Attendance.md), [Speech](Speech.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: datetime_begin
annotations:
  description_de:
    tag: description_de
    value: 'Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt.

      '
  description_fr:
    tag: description_fr
    value: 'La date et l''heure auxquelles la séance ou le vote commence.

      '
description: 'La date et l''heure auxquelles la séance ou le vote commence.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
- Election
- Attendance
- Speech
range: datetime

```
</details></div>