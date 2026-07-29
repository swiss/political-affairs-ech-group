---
search:
  boost: 5.0
---

# Slot: agenda_item_position 


_Integer position of the agenda item in the meeting sequence._




<div data-search-exclude markdown="1">



URI: [ops:agenda_item_position](https://ch.paf.link/schema/operations/agenda_item_position)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AgendaItem](AgendaItem.md) | An agenda item of a meeting |  no  |
| [ProtocolItem](ProtocolItem.md) | An agenda item as actually recorded in the protocol |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [AgendaItem](AgendaItem.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: agenda_item_position
annotations:
  description_de:
    tag: description_de
    value: 'Ganzzahlige Position des Traktandums in der Sitzungsreihenfolge.

      '
  description_fr:
    tag: description_fr
    value: 'Position (nombre entier) du point de l''ordre du jour dans le déroulement
      de la séance.

      '
description: 'Integer position of the agenda item in the meeting sequence.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: integer

```
</details></div>