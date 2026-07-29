---
search:
  boost: 5.0
---

# Slot: parent_attendance 


_Das Attendance-Aggregat, zu dem dieser einzelne Anwesenheits-Eintrag gehört._




<div data-search-exclude markdown="1">



URI: [ops:parentAttendance](https://ch.paf.link/schema/operations/parentAttendance)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [IndividualAttendance](IndividualAttendance.md) | Einzelne Anwesenheitsfeststellung einer Person an einer Sitzung (verknüpft üb... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Attendance](Attendance.md) |
| Domäne von | [IndividualAttendance](IndividualAttendance.md) |
| Slot-URI | [ops:parentAttendance](https://ch.paf.link/schema/operations/parentAttendance) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

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
description: 'Das Attendance-Aggregat, zu dem dieser einzelne Anwesenheits-Eintrag
  gehört.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:parentAttendance
domain_of:
- IndividualAttendance
range: Attendance

```
</details></div>