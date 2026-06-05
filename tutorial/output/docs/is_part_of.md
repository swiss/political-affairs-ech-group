---
search:
  boost: 5.0
---

# Slot: is_part_of 

<div data-search-exclude markdown="1">



URI: [tutorial:is_part_of](https://ch.paf.link/schema/tutorial/is_part_of)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Vote](Vote.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Vote](Vote.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| tutorial:s2025-1_t1 |
| tutorial:s2025-2_t1 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/tutorial




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tutorial:is_part_of |
| native | tutorial:is_part_of |




## LinkML Source

<details>
```yaml
name: is_part_of
examples:
- value: tutorial:s2025-1_t1
- value: tutorial:s2025-2_t1
from_schema: https://ch.paf.link/schema/tutorial
rank: 1000
domain_of:
- Vote
range: uriorcurie

```
</details></div>