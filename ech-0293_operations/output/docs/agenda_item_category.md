---
search:
  boost: 5.0
---

# Slot: agenda_item_category 


_[en] Category for grouped agenda items (e.g., introduction, by department, technical agenda items)._

_[de] Kategorie für gruppierte Traktanden (z.B. Einführung, nach Departement, technische Traktanden)._

__



<div data-search-exclude markdown="1">



URI: [ops:agenda_item_category](https://ch.paf.link/schema/operations/agenda_item_category)
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










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:agenda_item_category |
| native | ops:agenda_item_category |




## LinkML Source

<details>
```yaml
name: agenda_item_category
description: '[en] Category for grouped agenda items (e.g., introduction, by department,
  technical agenda items).

  [de] Kategorie für gruppierte Traktanden (z.B. Einführung, nach Departement, technische
  Traktanden).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: string

```
</details></div>