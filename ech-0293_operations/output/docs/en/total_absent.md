---
search:
  boost: 5.0
---

# Slot: total_absent 


_Total number of absent members. Distinction between absent/excused absent - presence is tracked on attendance list._




<div data-search-exclude markdown="1">



URI: [ops:total_absent](https://ch.paf.link/schema/operations/total_absent)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | A voting procedure with individual votes and results |  no  |
| [Election](Election.md) | An election procedure for selecting persons to positions |  no  |
| [Attendance](Attendance.md) | Aggregated attendance record for a meeting (number of members present, absent... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Voting](Voting.md), [Election](Election.md), [Attendance](Attendance.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: total_absent
annotations:
  description_de:
    tag: description_de
    value: 'Gesamtzahl abwesender Mitglieder. Unterscheidung zwischen abwesend/entschuldigt
      abwesend - Anwesenheit wird auf Anwesenheitsliste verfolgt.

      '
  description_fr:
    tag: description_fr
    value: 'Nombre total de membres absents. La distinction entre absent et absent
      excusé se fait dans la liste de présence.

      '
description: 'Total number of absent members. Distinction between absent/excused absent
  - presence is tracked on attendance list.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
- Election
- Attendance
range: integer

```
</details></div>