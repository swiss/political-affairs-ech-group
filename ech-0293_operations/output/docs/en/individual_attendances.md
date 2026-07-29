---
search:
  boost: 5.0
---

# Slot: individual_attendances 


_Collection of individual attendance records._




<div data-search-exclude markdown="1">



URI: [ops:individualAttendance](https://ch.paf.link/schema/operations/individualAttendance)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) | Container for the records of public council operations: legislatures, session... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [IndividualAttendance](IndividualAttendance.md) |
| Domain Of | [Container](Container.md) |
| Slot URI | [ops:individualAttendance](https://ch.paf.link/schema/operations/individualAttendance) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: individual_attendances
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der einzelnen Anwesenheitsfeststellungen.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des constatations individuelles de présence.

      '
description: 'Collection of individual attendance records.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:individualAttendance
domain_of:
- Container
range: IndividualAttendance
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>