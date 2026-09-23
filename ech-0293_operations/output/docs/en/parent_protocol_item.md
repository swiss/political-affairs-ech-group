---
search:
  boost: 5.0
---

# Slot: parent_protocol_item 


_The recorded agenda item (ProtocolItem) under which the voting or election took place. Omitted when the vote was taken without an agenda item; the link to the sitting is then given by parent_protocol and parent_meeting alone._




<div data-search-exclude markdown="1">



URI: [ops:parentProtocolItem](https://ch.paf.link/schema/operations/parentProtocolItem)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | A voting on a substantive question: the subject (question), the procedure, th... |  no  |
| [Election](Election.md) | An election in which a parliamentary body appoints one or several persons to ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ProtocolItem](ProtocolItem.md) |
| Domain Of | [Voting](Voting.md), [Election](Election.md) |
| Slot URI | [ops:parentProtocolItem](https://ch.paf.link/schema/operations/parentProtocolItem) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: parent_protocol_item
annotations:
  description_de:
    tag: description_de
    value: 'Das protokollierte Traktandum (ProtocolItem), unter dem abgestimmt oder
      gewählt wurde. Entfällt, wenn ohne Traktandierung abgestimmt wurde; die Zuordnung
      zur Sitzung ergibt sich dann allein aus parent_protocol und parent_meeting.

      '
  description_fr:
    tag: description_fr
    value: 'Le point consigné au procès-verbal (ProtocolItem) sous lequel le vote
      ou l''élection a eu lieu. Absent lorsque le vote a eu lieu sans point de l''ordre
      du jour ; le rattachement à la séance découle alors uniquement de parent_protocol
      et parent_meeting.

      '
description: 'The recorded agenda item (ProtocolItem) under which the voting or election
  took place. Omitted when the vote was taken without an agenda item; the link to
  the sitting is then given by parent_protocol and parent_meeting alone.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:parentProtocolItem
domain_of:
- Voting
- Election
range: ProtocolItem

```
</details></div>