

# Slot: datetime_begin 


_[en] The date and time when the meeting or voting begins._

_[de] Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt._

__





URI: [ops:datetime_begin](https://ch.paf.link/schema/operations/datetime_begin)
Alias: datetime_begin

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Speech](Speech.md) | [en] A speech or statement made during a meeting (also called Votum or speake... |  no  |
| [Attendance](Attendance.md) | [en] Attendance record for a meeting or voting session |  no  |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |






## Properties

* Range: [Datetime](Datetime.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:datetime_begin |
| native | ops:datetime_begin |




## LinkML Source

<details>
```yaml
name: datetime_begin
description: '[en] The date and time when the meeting or voting begins.

  [de] Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung beginnt.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: datetime_begin
domain_of:
- Voting
- Election
- Attendance
- Speech
range: datetime

```
</details>