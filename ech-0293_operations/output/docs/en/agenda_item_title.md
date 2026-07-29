---
search:
  boost: 5.0
---

# Slot: agenda_item_title 


_Title of the agenda item._




<div data-search-exclude markdown="1">



URI: [ops:agenda_item_title](https://ch.paf.link/schema/operations/agenda_item_title)
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
| Range | [MultilingualString](MultilingualString.md) |
| Domain Of | [AgendaItem](AgendaItem.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: agenda_item_title
annotations:
  description_de:
    tag: description_de
    value: 'Titel des Traktandums.

      '
  description_fr:
    tag: description_fr
    value: 'Titre du point de l''ordre du jour.

      '
description: 'Title of the agenda item.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: MultilingualString
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>