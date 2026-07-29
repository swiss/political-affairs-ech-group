---
search:
  boost: 5.0
---

# Slot: attendance_type 


_Type of individual attendance._




<div data-search-exclude markdown="1">



URI: [ops:attendance_type](https://ch.paf.link/schema/operations/attendance_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IndividualAttendance](IndividualAttendance.md) | Individual attendance record for a specific person at a meeting (linked via t... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AttendanceTypeEnum](AttendanceTypeEnum.md) |
| Domain Of | [IndividualAttendance](IndividualAttendance.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: attendance_type
annotations:
  description_de:
    tag: description_de
    value: 'Art der individuellen Anwesenheit.

      '
  description_fr:
    tag: description_fr
    value: 'Type de présence individuelle.

      '
description: 'Type of individual attendance.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IndividualAttendance
range: AttendanceTypeEnum

```
</details></div>