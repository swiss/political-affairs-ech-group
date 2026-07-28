---
search:
  boost: 5.0
---

# Slot: total_absent 


_[en] Total number of absent members. Distinction between absent/excused absent - presence is tracked on attendance list._

_[de] Gesamtzahl abwesender Mitglieder. Unterscheidung zwischen abwesend/entschuldigt abwesend - Anwesenheit wird auf Anwesenheitsliste verfolgt._

__



<div data-search-exclude markdown="1">



URI: [ops:total_absent](https://ch.paf.link/schema/operations/total_absent)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |
| [Attendance](Attendance.md) | [en] Aggregated attendance record for a meeting (number of members present, a... |  no  |






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
description: '[en] Total number of absent members. Distinction between absent/excused
  absent - presence is tracked on attendance list.

  [de] Gesamtzahl abwesender Mitglieder. Unterscheidung zwischen abwesend/entschuldigt
  abwesend - Anwesenheit wird auf Anwesenheitsliste verfolgt.

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