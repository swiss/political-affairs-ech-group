

# Slot: attendances 


_Collection of attendance records_





URI: [ops:attendance](https://ch.paf.link/schema/operations/attendance)
Alias: attendances

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) |  |  no  |






## Properties

* Range: [Attendance](Attendance.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:attendance |
| native | ops:attendances |




## LinkML Source

<details>
```yaml
name: attendances
description: Collection of attendance records
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:attendance
alias: attendances
domain_of:
- Container
range: Attendance
multivalued: true
inlined: true
inlined_as_list: true

```
</details>