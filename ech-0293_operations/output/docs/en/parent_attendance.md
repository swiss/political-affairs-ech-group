---
search:
  boost: 5.0
---

# Slot: parent_attendance 


_The Attendance aggregate this individual attendance record belongs to._




<div data-search-exclude markdown="1">



URI: [ops:parentAttendance](https://ch.paf.link/schema/operations/parentAttendance)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IndividualAttendance](IndividualAttendance.md) | Individual attendance record for a specific person at a meeting (linked via t... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Attendance](Attendance.md) |
| Domain Of | [IndividualAttendance](IndividualAttendance.md) |
| Slot URI | [ops:parentAttendance](https://ch.paf.link/schema/operations/parentAttendance) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

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
description: 'The Attendance aggregate this individual attendance record belongs to.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:parentAttendance
domain_of:
- IndividualAttendance
range: Attendance

```
</details></div>