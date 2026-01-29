

# Slot: total_absent 


_[en] Total number of absent members. Distinction between absent/excused absent - presence is tracked on attendance list._

_[de] Gesamtzahl abwesender Mitglieder. Unterscheidung zwischen abwesend/entschuldigt abwesend - Anwesenheit wird auf Anwesenheitsliste verfolgt._

__





URI: [ops:total_absent](https://ch.paf.link/schema/operations/total_absent)
Alias: total_absent

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |
| [Attendance](Attendance.md) | [en] Attendance record for a meeting or voting session |  no  |






## Properties

* Range: [Integer](Integer.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:total_absent |
| native | ops:total_absent |




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
alias: total_absent
domain_of:
- Voting
- Election
- Attendance
range: integer

```
</details>