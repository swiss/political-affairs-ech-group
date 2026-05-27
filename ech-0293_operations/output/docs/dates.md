---
search:
  boost: 5.0
---

# Slot: dates 

<div data-search-exclude markdown="1">



URI: [meta:dates](https://ch.paf.link/schema/meta/dates)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Expression](Expression.md) |  |  no  |
| [Manifestation](Manifestation.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [Expression](Expression.md), [Manifestation](Manifestation.md) |
| Slot URI | [meta:dates](https://ch.paf.link/schema/meta/dates) |

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
| self | meta:dates |
| native | ops:dates |




## LinkML Source

<details>
```yaml
name: dates
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:dates
domain_of:
- Expression
- Manifestation
range: Date
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>