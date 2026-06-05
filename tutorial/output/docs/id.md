---
search:
  boost: 5.0
---

# Slot: id 

<div data-search-exclude markdown="1">



URI: [tutorial:id](https://ch.paf.link/schema/tutorial/id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Session](Session.md) |  |  no  |
| [AgendaItem](AgendaItem.md) |  |  no  |
| [Vote](Vote.md) |  |  no  |
| [Container](Container.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Session](Session.md), [AgendaItem](AgendaItem.md), [Vote](Vote.md), [Container](Container.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |











## Examples

| Value |
| --- |
| tutorial:s2025 |
| tutorial:s2025-1 |
| tutorial:s2025-1_t1 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/tutorial




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tutorial:id |
| native | tutorial:id |




## LinkML Source

<details>
```yaml
name: id
examples:
- value: tutorial:s2025
- value: tutorial:s2025-1
- value: tutorial:s2025-1_t1
from_schema: https://ch.paf.link/schema/tutorial
rank: 1000
identifier: true
domain_of:
- Session
- AgendaItem
- Vote
- Container
range: string
required: true

```
</details></div>