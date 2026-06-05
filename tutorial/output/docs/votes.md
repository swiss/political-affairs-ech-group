---
search:
  boost: 5.0
---

# Slot: votes 

<div data-search-exclude markdown="1">



URI: [tutorial:vote](https://ch.paf.link/schema/tutorial/vote)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AgendaItem](AgendaItem.md) |  |  no  |
| [Container](Container.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Vote](Vote.md) |
| Domain Of | [AgendaItem](AgendaItem.md), [Container](Container.md) |
| Slot URI | [tutorial:vote](https://ch.paf.link/schema/tutorial/vote) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/tutorial




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tutorial:vote |
| native | tutorial:votes |




## LinkML Source

<details>
```yaml
name: votes
from_schema: https://ch.paf.link/schema/tutorial
rank: 1000
slot_uri: tutorial:vote
domain_of:
- AgendaItem
- Container
range: Vote
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>