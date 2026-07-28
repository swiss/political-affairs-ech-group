---
search:
  boost: 5.0
---

# Slot: speaking_actor_id 


_[en] The speaker or head of the department for the agenda item._

_[de] Der Sprecher oder Departementsvorsteher für den Tagesordnungspunkt._

__



<div data-search-exclude markdown="1">



URI: [ops:speaking_actor_id](https://ch.paf.link/schema/operations/speaking_actor_id)
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
name: speaking_actor_id
description: '[en] The speaker or head of the department for the agenda item.

  [de] Der Sprecher oder Departementsvorsteher für den Tagesordnungspunkt.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: string

```
</details></div>