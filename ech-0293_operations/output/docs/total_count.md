

# Slot: total_count 


_[en] Total number of members of the body (reference value for quorum calculations)._

_[de] Gesamtzahl aller Mitglieder des Gremiums (Bezugsgrösse für Quorum-Berechnungen)._

__





URI: [ops:total_count](https://ch.paf.link/schema/operations/total_count)
Alias: total_count

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










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:total_count |
| native | ops:total_count |




## LinkML Source

<details>
```yaml
name: total_count
description: '[en] Total number of members of the body (reference value for quorum
  calculations).

  [de] Gesamtzahl aller Mitglieder des Gremiums (Bezugsgrösse für Quorum-Berechnungen).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: total_count
domain_of:
- Attendance
range: integer

```
</details>