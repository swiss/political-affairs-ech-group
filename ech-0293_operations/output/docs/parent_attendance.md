---
search:
  boost: 5.0
---

# Slot: parent_attendance 


_[en] The Attendance aggregate this individual attendance record belongs to._

_[de] Das Attendance-Aggregat, zu dem dieser einzelne Anwesenheits-Eintrag gehört._

__



<div data-search-exclude markdown="1">



URI: [ops:parentAttendance](https://ch.paf.link/schema/operations/parentAttendance)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IndividualAttendance](IndividualAttendance.md) | [en] Individual attendance record for a specific person at a meeting (linked ... |  no  |






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










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:parentAttendance |
| native | ops:parent_attendance |




## LinkML Source

<details>
```yaml
name: parent_attendance
description: '[en] The Attendance aggregate this individual attendance record belongs
  to.

  [de] Das Attendance-Aggregat, zu dem dieser einzelne Anwesenheits-Eintrag gehört.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:parentAttendance
domain_of:
- IndividualAttendance
range: Attendance

```
</details></div>