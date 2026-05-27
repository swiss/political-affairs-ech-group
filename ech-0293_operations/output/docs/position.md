---
search:
  boost: 5.0
---

# Slot: position 

<div data-search-exclude markdown="1">



URI: [ops:position](https://ch.paf.link/schema/operations/position)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Session](Session.md) | [en] A parliamentary session that groups multiple meetings and spans a specif... |  no  |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Session](Session.md), [Meeting](Meeting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:position |
| native | ops:position |




## LinkML Source

<details>
```yaml
name: position
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>