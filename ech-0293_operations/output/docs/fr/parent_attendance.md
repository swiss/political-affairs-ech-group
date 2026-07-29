---
search:
  boost: 5.0
---

# Slot: parent_attendance 


_L'agrégat Attendance auquel appartient cette constatation individuelle de présence._




<div data-search-exclude markdown="1">



URI: [ops:parentAttendance](https://ch.paf.link/schema/operations/parentAttendance)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [IndividualAttendance](IndividualAttendance.md) | Constatation individuelle de la présence d'une personne à une séance (rattach... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Attendance](Attendance.md) |
| Domaine de | [IndividualAttendance](IndividualAttendance.md) |
| URI du slot | [ops:parentAttendance](https://ch.paf.link/schema/operations/parentAttendance) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: parent_attendance
annotations:
  description_de:
    tag: description_de
    value: 'Das Attendance-Aggregat, zu dem dieser einzelne Anwesenheits-Eintrag gehört.

      '
  description_fr:
    tag: description_fr
    value: 'L''agrégat Attendance auquel appartient cette constatation individuelle
      de présence.

      '
description: 'L''agrégat Attendance auquel appartient cette constatation individuelle
  de présence.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:parentAttendance
domain_of:
- IndividualAttendance
range: Attendance

```
</details></div>