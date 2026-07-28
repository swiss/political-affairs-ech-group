---
search:
  boost: 5.0
---

# Slot: agenda_item_type 


_[en] Type of agenda item, distinguishing individual items from groups._

_[de] Art des Traktandums, unterscheidet Einzeltraktanden von Traktandengruppen._

__



<div data-search-exclude markdown="1">



URI: [ops:agenda_item_type](https://ch.paf.link/schema/operations/agenda_item_type)
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
| Range | [AgendaItemTypeEnum](AgendaItemTypeEnum.md) |
| Domain Of | [AgendaItem](AgendaItem.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| item |





## LinkML Source

<details>
```yaml
name: agenda_item_type
description: '[en] Type of agenda item, distinguishing individual items from groups.

  [de] Art des Traktandums, unterscheidet Einzeltraktanden von Traktandengruppen.

  '
examples:
- value: item
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: AgendaItemTypeEnum

```
</details></div>