---
search:
  boost: 5.0
---

# Slot: agenda_item_title 


_[en] Title of the agenda item._

_[de] Titel des Traktandums._

__



<div data-search-exclude markdown="1">



URI: [ops:agenda_item_title](https://ch.paf.link/schema/operations/agenda_item_title)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AgendaItem](AgendaItem.md) | [en] An agenda item of a meeting |  no  |






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










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:agenda_item_title |
| native | ops:agenda_item_title |




## LinkML Source

<details>
```yaml
name: agenda_item_title
description: '[en] Title of the agenda item.

  [de] Titel des Traktandums.

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