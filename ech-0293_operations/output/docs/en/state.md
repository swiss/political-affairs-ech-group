---
search:
  boost: 5.0
---

# Slot: state 


_Current state of the meeting (planned, canceled, postponed)._




<div data-search-exclude markdown="1">



URI: [ops:state](https://ch.paf.link/schema/operations/state)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | A general meeting class used for Sessions, Comittee Meetings, individual sess... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StateEnum](StateEnum.md) |
| Domain Of | [Meeting](Meeting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| planned |





## LinkML Source

<details>
```yaml
name: state
annotations:
  description_de:
    tag: description_de
    value: 'Aktueller Status der Sitzung (geplant, abgesagt, verschoben).

      '
  description_fr:
    tag: description_fr
    value: 'État actuel de la séance (planifiée, annulée, reportée).

      '
description: 'Current state of the meeting (planned, canceled, postponed).

  '
examples:
- value: planned
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
range: StateEnum

```
</details></div>