---
search:
  boost: 5.0
---

# Slot: joint_debates 


_Joint debates in which this agenda item is deliberated together with other agenda items._




<div data-search-exclude markdown="1">



URI: [ops:jointDebate](https://ch.paf.link/schema/operations/jointDebate)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IsAgendaItem](IsAgendaItem.md) | A mixin class that provides the elements of an agenda item: designation, type... |  no  |
| [AgendaItem](AgendaItem.md) | An agenda item of a meeting |  no  |
| [ProtocolItem](ProtocolItem.md) | An agenda item as actually recorded in the protocol |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [JointDebate](JointDebate.md) |
| Domain Of | [IsAgendaItem](IsAgendaItem.md) |
| Slot URI | [ops:jointDebate](https://ch.paf.link/schema/operations/jointDebate) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: joint_debates
annotations:
  description_de:
    tag: description_de
    value: 'Gemeinsame Beratungen, in denen dieses Traktandum zusammen mit anderen
      Traktanden behandelt wird.

      '
  description_fr:
    tag: description_fr
    value: 'Délibérations communes dans lesquelles ce point de l''ordre du jour est
      traité conjointement avec d''autres points.

      '
description: 'Joint debates in which this agenda item is deliberated together with
  other agenda items.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:jointDebate
domain_of:
- IsAgendaItem
range: JointDebate
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>