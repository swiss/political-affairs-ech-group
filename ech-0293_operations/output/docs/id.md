---
search:
  boost: 5.0
---

# Slot: id 

<div data-search-exclude markdown="1">



URI: [ops:id](https://ch.paf.link/schema/operations/id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Work](Work.md) |  |  no  |
| [Expression](Expression.md) |  |  no  |
| [Manifestation](Manifestation.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Work](Work.md), [Expression](Expression.md), [Manifestation](Manifestation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:id |
| native | ops:id |




## LinkML Source

<details>
```yaml
name: id
from_schema: https://ch.paf.link/schema/operations
rank: 1000
identifier: true
domain_of:
- Work
- Expression
- Manifestation
range: string
required: true

```
</details></div>