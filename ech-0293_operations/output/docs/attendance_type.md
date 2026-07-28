---
search:
  boost: 5.0
---

# Slot: attendance_type 


_Type of individual attendance_



<div data-search-exclude markdown="1">



URI: [ops:attendance_type](https://ch.paf.link/schema/operations/attendance_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IndividualAttendance](IndividualAttendance.md) | [en] Individual attendance record for a specific person at a meeting (linked ... |  no  |






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
description: Type of individual attendance
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IndividualAttendance
range: AttendanceTypeEnum

```
</details></div>