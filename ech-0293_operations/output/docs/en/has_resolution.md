---
search:
  boost: 5.0
---

# Slot: has_resolution 


_The resolution or decision taken on this agenda item._




<div data-search-exclude markdown="1">



URI: [ops:has_resolution](https://ch.paf.link/schema/operations/has_resolution)
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
| Range | [Resolution](Resolution.md) |
| Domain Of | [AgendaItem](AgendaItem.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: has_resolution
annotations:
  description_de:
    tag: description_de
    value: 'Die Resolution oder Entscheidung zu diesem Traktandum.

      '
  description_fr:
    tag: description_fr
    value: 'La décision prise sur ce point de l''ordre du jour.

      '
description: 'The resolution or decision taken on this agenda item.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: Resolution

```
</details></div>