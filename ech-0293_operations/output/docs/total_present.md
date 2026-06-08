---
search:
  boost: 5.0
---

# Slot: total_present 


_Total number of members present_



<div data-search-exclude markdown="1">



URI: [ops:total_present](https://ch.paf.link/schema/operations/total_present)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Attendance](Attendance.md) | [en] Aggregated attendance record for a meeting (number of members present, a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Attendance](Attendance.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: total_present
description: Total number of members present
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Attendance
range: integer

```
</details></div>