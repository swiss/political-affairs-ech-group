---
search:
  boost: 5.0
---

# Slot: leading_actor_id 


_The leading department for the agenda item._




<div data-search-exclude markdown="1">



URI: [ops:leading_actor_id](https://ch.paf.link/schema/operations/leading_actor_id)
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
| Range | [String](String.md) |
| Domain Of | [AgendaItem](AgendaItem.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: leading_actor_id
annotations:
  description_de:
    tag: description_de
    value: 'Das federführende Departement für das Traktandum.

      '
  description_fr:
    tag: description_fr
    value: 'Le département responsable du point de l''ordre du jour.

      '
description: 'The leading department for the agenda item.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: string

```
</details></div>