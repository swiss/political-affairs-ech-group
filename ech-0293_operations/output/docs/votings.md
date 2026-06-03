---
search:
  boost: 5.0
---

# Slot: votings 


_Collection of voting records_



<div data-search-exclude markdown="1">



URI: [ops:voting](https://ch.paf.link/schema/operations/voting)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) |  |  no  |
| [Protocol](Protocol.md) | [en] The minutes of a meeting, recorded after the meeting |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Voting](Voting.md) |
| Domain Of | [Container](Container.md), [Protocol](Protocol.md) |
| Slot URI | [ops:voting](https://ch.paf.link/schema/operations/voting) |

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
| self | ops:voting |
| native | ops:votings |




## LinkML Source

<details>
```yaml
name: votings
description: Collection of voting records
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:voting
domain_of:
- Container
- Protocol
range: Voting
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>