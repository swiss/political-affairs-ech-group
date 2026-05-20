---
search:
  boost: 5.0
---

# Slot: individual_votes 


_Collection of individual vote records_



<div data-search-exclude markdown="1">



URI: [ops:individualVote](https://ch.paf.link/schema/operations/individualVote)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [IndividualVote](IndividualVote.md) |
| Domain Of | [Container](Container.md) |
| Slot URI | [ops:individualVote](https://ch.paf.link/schema/operations/individualVote) |

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
| self | ops:individualVote |
| native | ops:individual_votes |




## LinkML Source

<details>
```yaml
name: individual_votes
description: Collection of individual vote records
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:individualVote
domain_of:
- Container
range: IndividualVote
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>