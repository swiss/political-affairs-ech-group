---
search:
  boost: 5.0
---

# Slot: agenda_item_number 


_[en] Sequential number of the agenda item (string type to support roman numerals)._

_[de] Laufnummer des Traktandums (String-Typ zur Unterstützung römischer Ziffern)._

__



<div data-search-exclude markdown="1">



URI: [ops:agenda_item_number](https://ch.paf.link/schema/operations/agenda_item_number)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AgendaItem](AgendaItem.md) | [en] An agenda item of a meeting |  no  |
| [ProtocolItem](ProtocolItem.md) | [en] An agenda item as actually recorded in the protocol |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AgendaItem](AgendaItem.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: agenda_item_number
description: '[en] Sequential number of the agenda item (string type to support roman
  numerals).

  [de] Laufnummer des Traktandums (String-Typ zur Unterstützung römischer Ziffern).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: string

```
</details></div>