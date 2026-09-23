---
search:
  boost: 5.0
---

# Slot: parent_protocol_item 


_Le point consigné au procès-verbal (ProtocolItem) sous lequel le vote ou l'élection a eu lieu. Absent lorsque le vote a eu lieu sans point de l'ordre du jour ; le rattachement à la séance découle alors uniquement de parent_protocol et parent_meeting._




<div data-search-exclude markdown="1">



URI: [ops:parentProtocolItem](https://ch.paf.link/schema/operations/parentProtocolItem)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Voting](Voting.md) | Un vote sur une question matérielle : l'objet du vote (la question), la procé... |  no  |
| [Election](Election.md) | Une élection par laquelle un organe parlementaire désigne une ou plusieurs pe... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [ProtocolItem](ProtocolItem.md) |
| Domaine de | [Voting](Voting.md), [Election](Election.md) |
| URI du slot | [ops:parentProtocolItem](https://ch.paf.link/schema/operations/parentProtocolItem) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

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
description: 'Le point consigné au procès-verbal (ProtocolItem) sous lequel le vote
  ou l''élection a eu lieu. Absent lorsque le vote a eu lieu sans point de l''ordre
  du jour ; le rattachement à la séance découle alors uniquement de parent_protocol
  et parent_meeting.

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