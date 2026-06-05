---
search:
  boost: 5.0
---

# Slot: agenda_items 

<div data-search-exclude markdown="1">



URI: [tutorial:agendaItem](https://ch.paf.link/schema/tutorial/agendaItem)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Session](Session.md) |  |  no  |
| [Container](Container.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AgendaItem](AgendaItem.md) |
| Domain Of | [Session](Session.md), [Container](Container.md) |
| Slot URI | [tutorial:agendaItem](https://ch.paf.link/schema/tutorial/agendaItem) |

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
| self | tutorial:agendaItem |
| native | tutorial:agenda_items |




## LinkML Source

<details>
```yaml
name: agenda_items
from_schema: https://ch.paf.link/schema/tutorial
rank: 1000
slot_uri: tutorial:agendaItem
domain_of:
- Session
- Container
range: AgendaItem
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>