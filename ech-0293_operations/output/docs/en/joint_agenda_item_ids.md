---
search:
  boost: 5.0
---

# Slot: joint_agenda_item_ids 


_Identifiers of the agenda items (AgendaItem or ProtocolItem) debated jointly._




<div data-search-exclude markdown="1">



URI: [ops:jointAgendaItem](https://ch.paf.link/schema/operations/jointAgendaItem)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [JointDebate](JointDebate.md) | A joint debate: several agenda items are deliberated together |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [JointDebate](JointDebate.md) |
| Slot URI | [ops:jointAgendaItem](https://ch.paf.link/schema/operations/jointAgendaItem) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: joint_agenda_item_ids
annotations:
  description_de:
    tag: description_de
    value: 'Identifikatoren der gemeinsam behandelten Traktanden (AgendaItem oder
      ProtocolItem).

      '
  description_fr:
    tag: description_fr
    value: 'Identifiants des points de l''ordre du jour traités conjointement (AgendaItem
      ou ProtocolItem).

      '
description: 'Identifiers of the agenda items (AgendaItem or ProtocolItem) debated
  jointly.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:jointAgendaItem
domain_of:
- JointDebate
range: string
multivalued: true

```
</details></div>