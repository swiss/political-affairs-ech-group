---
search:
  boost: 5.0
---

# Slot: position 


_Integer position within the superordinate sequence._




<div data-search-exclude markdown="1">



URI: [ops:position](https://ch.paf.link/schema/operations/position)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Session](Session.md) | A parliamentary session that groups multiple meetings and spans a specific ti... |  no  |
| [Meeting](Meeting.md) | A general meeting class used for Sessions, Comittee Meetings, individual sess... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Session](Session.md), [Meeting](Meeting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: position
annotations:
  description_de:
    tag: description_de
    value: 'Ganzzahlige Position innerhalb der übergeordneten Reihenfolge.

      '
  description_fr:
    tag: description_fr
    value: 'Position (nombre entier) au sein de la séquence supérieure.

      '
description: 'Integer position within the superordinate sequence.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>