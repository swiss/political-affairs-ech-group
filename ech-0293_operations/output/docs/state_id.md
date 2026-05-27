---
search:
  boost: 5.0
---

# Slot: state_id 


_State identifier (reference to state enum or custom state)_



<div data-search-exclude markdown="1">



URI: [ops:state_id](https://ch.paf.link/schema/operations/state_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AgendaItem](AgendaItem.md) | [en] An agenda item of a meeting |  no  |






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
| self | ops:state_id |
| native | ops:state_id |




## LinkML Source

<details>
```yaml
name: state_id
description: State identifier (reference to state enum or custom state)
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: string

```
</details></div>