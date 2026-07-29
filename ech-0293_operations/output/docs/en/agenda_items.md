---
search:
  boost: 5.0
---

# Slot: agenda_items 


_Collection of agenda item records._




<div data-search-exclude markdown="1">



URI: [ops:agendaItem](https://ch.paf.link/schema/operations/agendaItem)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) | Container for the records of public council operations: legislatures, session... |  no  |
| [JointDebate](JointDebate.md) | Agenda Items which are debated together |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AgendaItem](AgendaItem.md) |
| Domain Of | [Container](Container.md), [JointDebate](JointDebate.md) |
| Slot URI | [ops:agendaItem](https://ch.paf.link/schema/operations/agendaItem) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: agenda_items
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der Traktanden.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des points de l''ordre du jour.

      '
description: 'Collection of agenda item records.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:agendaItem
domain_of:
- Container
- JointDebate
range: AgendaItem
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>