---
search:
  boost: 5.0
---

# Slot: total_absent 


_Number of absent members who could not take part. Whether an absence was excused is tracked on the attendance list (Attendance)._




<div data-search-exclude markdown="1">



URI: [ops:total_absent](https://ch.paf.link/schema/operations/total_absent)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | A voting on a substantive question: the subject (question), the procedure, th... |  no  |
| [Election](Election.md) | An election in which a parliamentary body appoints one or several persons to ... |  no  |
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
    value: 'Anzahl abwesender Mitglieder, die nicht teilnehmen konnten. Ob eine Abwesenheit
      entschuldigt war, hält die Anwesenheitsliste (Attendance) fest.

      '
  description_fr:
    tag: description_fr
    value: 'Nombre de membres absents qui n''ont pas pu participer. La liste de présence
      (Attendance) indique si une absence était excusée.

      '
description: 'Number of absent members who could not take part. Whether an absence
  was excused is tracked on the attendance list (Attendance).

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