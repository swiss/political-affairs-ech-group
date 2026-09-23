---
search:
  boost: 5.0
---

# Slot: joint_debates 


_Joint debates attached to this record: on an agenda item, the debates in which it is deliberated together with other agenda items; on a meeting or a session, the joint debates held within it._




<div data-search-exclude markdown="1">



URI: [ops:jointDebate](https://ch.paf.link/schema/operations/jointDebate)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Session](Session.md) | A session: a contiguous period of sittings within a legislature |  no  |
| [Meeting](Meeting.md) | The individual sitting of a body — the level at which agenda items are delibe... |  no  |
| [IsAgendaItem](IsAgendaItem.md) | A mixin class that provides the elements of an agenda item: designation, type... |  no  |
| [AgendaItem](AgendaItem.md) | An agenda item of a meeting as planned beforehand |  no  |
| [ProtocolItem](ProtocolItem.md) | An agenda item as actually recorded in the protocol |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [JointDebate](JointDebate.md) |
| Domain Of | [Session](Session.md), [Meeting](Meeting.md), [IsAgendaItem](IsAgendaItem.md) |
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
    value: 'An diesem Eintrag angehängte gemeinsame Beratungen: bei einem Traktandum
      die Beratungen, in denen es zusammen mit anderen Traktanden behandelt wird;
      bei einer Sitzung oder Session die darin geführten gemeinsamen Beratungen.

      '
  description_fr:
    tag: description_fr
    value: 'Délibérations communes rattachées à cet enregistrement : pour un point
      de l''ordre du jour, les délibérations dans lesquelles il est traité conjointement
      avec d''autres points ; pour une séance ou une session, les délibérations communes
      qui s''y tiennent.

      '
description: 'Joint debates attached to this record: on an agenda item, the debates
  in which it is deliberated together with other agenda items; on a meeting or a session,
  the joint debates held within it.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:jointDebate
domain_of:
- Session
- Meeting
- IsAgendaItem
range: JointDebate
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>