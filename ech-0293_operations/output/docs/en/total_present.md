---
search:
  boost: 5.0
---

# Slot: total_present 


_Total number of members present._




<div data-search-exclude markdown="1">



URI: [ops:total_present](https://ch.paf.link/schema/operations/total_present)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Attendance](Attendance.md) | Aggregated attendance record for a meeting (number of members present, absent... |  no  |






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
annotations:
  description_de:
    tag: description_de
    value: 'Gesamtzahl der anwesenden Mitglieder.

      '
  description_fr:
    tag: description_fr
    value: 'Nombre total de membres présents.

      '
description: 'Total number of members present.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Attendance
range: integer

```
</details></div>