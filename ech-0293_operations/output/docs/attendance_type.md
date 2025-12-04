

# Slot: attendance_type 


_Type of individual attendance_





URI: [ops:attendance_type](https://ch.paf.link/schema/operations/attendance_type)
Alias: attendance_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IndividualAttendance](IndividualAttendance.md) | [en] Individual attendance record for a specific person |  no  |






## Properties

* Range: [AttendanceTypeEnum](AttendanceTypeEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:attendance_type |
| native | ops:attendance_type |




## LinkML Source

<details>
```yaml
name: attendance_type
description: Type of individual attendance
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: attendance_type
domain_of:
- IndividualAttendance
range: attendance_type_enum

```
</details>