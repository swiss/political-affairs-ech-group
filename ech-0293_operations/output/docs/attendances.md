---
search:
  boost: 5.0
---

# Slot: attendances 


_Collection of attendance records_



<div data-search-exclude markdown="1">



URI: [ops:attendance](https://ch.paf.link/schema/operations/attendance)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Attendance](Attendance.md) |
| Domain Of | [Container](Container.md) |
| Slot URI | [ops:attendance](https://ch.paf.link/schema/operations/attendance) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










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
domain_of:
- Container
range: Attendance
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>