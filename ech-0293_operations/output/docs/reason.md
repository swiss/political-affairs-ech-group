---
search:
  boost: 5.0
---

# Slot: reason 


_[en] Reason for absence or lateness (free-text, multilingual)._

_[de] Grund für Abwesenheit oder Verspätung (Freitext, mehrsprachig)._

__



<div data-search-exclude markdown="1">



URI: [ops:reason](https://ch.paf.link/schema/operations/reason)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IndividualAttendance](IndividualAttendance.md) | [en] Individual attendance record for a specific person at a meeting (linked ... |  no  |






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










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:reason |
| native | ops:reason |




## LinkML Source

<details>
```yaml
name: reason
description: '[en] Reason for absence or lateness (free-text, multilingual).

  [de] Grund für Abwesenheit oder Verspätung (Freitext, mehrsprachig).

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