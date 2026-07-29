---
search:
  boost: 5.0
---

# Slot: reason 


_Reason for absence or lateness (free-text, multilingual)._




<div data-search-exclude markdown="1">



URI: [ops:reason](https://ch.paf.link/schema/operations/reason)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IndividualAttendance](IndividualAttendance.md) | Individual attendance record for a specific person at a meeting (linked via t... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MultilingualString](MultilingualString.md) |
| Domain Of | [IndividualAttendance](IndividualAttendance.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: reason
annotations:
  description_de:
    tag: description_de
    value: 'Grund für Abwesenheit oder Verspätung (Freitext, mehrsprachig).

      '
  description_fr:
    tag: description_fr
    value: 'Motif de l''absence ou du retard (texte libre, multilingue).

      '
description: 'Reason for absence or lateness (free-text, multilingual).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IndividualAttendance
range: MultilingualString
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>