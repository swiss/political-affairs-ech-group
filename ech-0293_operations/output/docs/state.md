---
search:
  boost: 5.0
---

# Slot: state 

<div data-search-exclude markdown="1">



URI: [ops:state](https://ch.paf.link/schema/operations/state)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StateEnum](StateEnum.md) |
| Domain Of | [Meeting](Meeting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:state |
| native | ops:state |




## LinkML Source

<details>
```yaml
name: state
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
range: StateEnum

```
</details></div>