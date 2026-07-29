---
search:
  boost: 5.0
---

# Slot: attendances 


_Collection of attendance records._




<div data-search-exclude markdown="1">



URI: [ops:attendance](https://ch.paf.link/schema/operations/attendance)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) | Container for the records of public council operations: legislatures, session... |  no  |






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












## LinkML Source

<details>
```yaml
name: attendances
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der Anwesenheitslisten.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des listes de présence.

      '
description: 'Collection of attendance records.

  '
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