---
search:
  boost: 5.0
---

# Slot: datetime_begin 


_[en] The date and time when the meeting or voting begins._

_[de] Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt._

__



<div data-search-exclude markdown="1">



URI: [ops:datetime_begin](https://ch.paf.link/schema/operations/datetime_begin)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |
| [Attendance](Attendance.md) | [en] Aggregated attendance record for a meeting (number of members present, a... |  no  |
| [Speech](Speech.md) | [en] A speech or statement made during a meeting (also called Votum or speake... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [Voting](Voting.md), [Election](Election.md), [Attendance](Attendance.md), [Speech](Speech.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: datetime_begin
description: '[en] The date and time when the meeting or voting begins.

  [de] Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
- Election
- Attendance
- Speech
range: datetime

```
</details></div>