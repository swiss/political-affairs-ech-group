---
search:
  boost: 5.0
---

# Slot: name 

<div data-search-exclude markdown="1">



URI: [schema:name](http://schema.org/name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Session](Session.md) |  |  no  |
| [AgendaItem](AgendaItem.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MultilingualValue](MultilingualValue.md) |
| Domain Of | [Session](Session.md), [AgendaItem](AgendaItem.md) |
| Slot URI | [schema:name](http://schema.org/name) |

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
| self | schema:name |
| native | tutorial:name |




## LinkML Source

<details>
```yaml
name: name
from_schema: https://ch.paf.link/schema/tutorial
rank: 1000
slot_uri: schema:name
domain_of:
- Session
- AgendaItem
range: MultilingualValue
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>