---
search:
  boost: 5.0
---

# Slot: state_id 


_State identifier (reference to state enum or custom state)._




<div data-search-exclude markdown="1">



URI: [ops:state_id](https://ch.paf.link/schema/operations/state_id)
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
name: state_id
annotations:
  description_de:
    tag: description_de
    value: 'Zustands-Identifikator (Verweis auf das Status-Enum oder auf einen eigenen
      Zustand).

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant d''état (renvoi à l''énumération des états ou à un état propre).

      '
description: 'State identifier (reference to state enum or custom state).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: string

```
</details></div>