---
search:
  boost: 5.0
---

# Slot: parent_protocol_item 


_Das protokollierte Traktandum (ProtocolItem), unter dem abgestimmt oder gewählt wurde. Entfällt, wenn ohne Traktandierung abgestimmt wurde; die Zuordnung zur Sitzung ergibt sich dann allein aus parent_protocol und parent_meeting._




<div data-search-exclude markdown="1">



URI: [ops:parentProtocolItem](https://ch.paf.link/schema/operations/parentProtocolItem)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Voting](Voting.md) | Ein Abstimmungsverfahren mit Einzelstimmen und Ergebnissen |  no  |
| [Election](Election.md) | Ein Wahlverfahren zur Wahl von Personen in Positionen |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [ProtocolItem](ProtocolItem.md) |
| Domäne von | [Voting](Voting.md), [Election](Election.md) |
| Slot-URI | [ops:parentProtocolItem](https://ch.paf.link/schema/operations/parentProtocolItem) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

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
description: 'Das protokollierte Traktandum (ProtocolItem), unter dem abgestimmt oder
  gewählt wurde. Entfällt, wenn ohne Traktandierung abgestimmt wurde; die Zuordnung
  zur Sitzung ergibt sich dann allein aus parent_protocol und parent_meeting.

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