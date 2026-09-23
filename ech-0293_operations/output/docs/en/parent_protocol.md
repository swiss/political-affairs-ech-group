---
search:
  boost: 5.0
---

# Slot: parent_protocol 


_The protocol in which the voting or election is recorded. A vote is held during the sitting and is therefore anchored in the minutes, not in the agenda planned beforehand._




<div data-search-exclude markdown="1">



URI: [ops:parentProtocol](https://ch.paf.link/schema/operations/parentProtocol)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | A voting procedure with individual votes and results |  no  |
| [Election](Election.md) | An election procedure for selecting persons to positions |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Protocol](Protocol.md) |
| Domain Of | [Voting](Voting.md), [Election](Election.md) |
| Slot URI | [ops:parentProtocol](https://ch.paf.link/schema/operations/parentProtocol) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: parent_protocol
annotations:
  description_de:
    tag: description_de
    value: 'Das Protokoll, in dem die Abstimmung oder Wahl festgehalten ist. Abgestimmt
      wird im Verlauf der Sitzung; die Abstimmung hängt deshalb am Protokoll und nicht
      an der vorgängig geplanten Traktandenliste.

      '
  description_fr:
    tag: description_fr
    value: 'Le procès-verbal dans lequel le vote ou l''élection est consigné. Un vote
      a lieu au cours de la séance et se rattache donc au procès-verbal et non à l''ordre
      du jour planifié à l''avance.

      '
description: 'The protocol in which the voting or election is recorded. A vote is
  held during the sitting and is therefore anchored in the minutes, not in the agenda
  planned beforehand.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:parentProtocol
domain_of:
- Voting
- Election
range: Protocol

```
</details></div>