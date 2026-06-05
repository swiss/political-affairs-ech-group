---
search:
  boost: 5.0
---

# Slot: result 

<div data-search-exclude markdown="1">



URI: [tutorial:result](https://ch.paf.link/schema/tutorial/result)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Vote](Vote.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ResultEnum](ResultEnum.md) |
| Domain Of | [Vote](Vote.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| no |
| yes |



## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/tutorial




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tutorial:result |
| native | tutorial:result |




## LinkML Source

<details>
```yaml
name: result
examples:
- value: 'no'
- value: 'yes'
from_schema: https://ch.paf.link/schema/tutorial
rank: 1000
domain_of:
- Vote
range: result_enum

```
</details></div>