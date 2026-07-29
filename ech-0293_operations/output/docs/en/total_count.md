---
search:
  boost: 5.0
---

# Slot: total_count 


_Total number of members of the body (reference value for quorum calculations)._




<div data-search-exclude markdown="1">



URI: [ops:total_count](https://ch.paf.link/schema/operations/total_count)
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
name: total_count
annotations:
  description_de:
    tag: description_de
    value: 'Gesamtzahl aller Mitglieder des Gremiums (Bezugsgrösse für Quorum-Berechnungen).

      '
  description_fr:
    tag: description_fr
    value: 'Nombre total de membres de l''organe (valeur de référence pour le calcul
      du quorum).

      '
description: 'Total number of members of the body (reference value for quorum calculations).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Attendance
range: integer

```
</details></div>