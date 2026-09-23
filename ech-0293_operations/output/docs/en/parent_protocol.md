---
search:
  boost: 5.0
---

# Slot: parent_protocol 


_The protocol in which the voting or election is recorded. A vote is held during the sitting and is therefore anchored in the minutes, not in the agenda planned beforehand: what was put on the agenda does not yet say what was actually voted on. Conversely, the protocol lists its votings and elections (votings, elections)._




<div data-search-exclude markdown="1">



URI: [ops:parentProtocol](https://ch.paf.link/schema/operations/parentProtocol)
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
      wird im Verlauf der Sitzung, weshalb die Abstimmung im Protokoll und nicht in
      der vorgängig geplanten Traktandenliste verankert ist: Was traktandiert wurde,
      sagt noch nicht, worüber tatsächlich abgestimmt wurde. Umgekehrt führt das Protokoll
      seine Abstimmungen und Wahlen als Listen (votings, elections).

      '
  description_fr:
    tag: description_fr
    value: 'Le procès-verbal dans lequel le vote ou l''élection est consigné. Le vote
      a lieu au cours de la séance et se rattache donc au procès-verbal, et non à
      l''ordre du jour planifié à l''avance : ce qui a été mis à l''ordre du jour
      ne dit pas encore sur quoi il a effectivement été voté. Inversement, le procès-verbal
      reprend ses votes et élections sous forme de listes (votings, elections).

      '
description: 'The protocol in which the voting or election is recorded. A vote is
  held during the sitting and is therefore anchored in the minutes, not in the agenda
  planned beforehand: what was put on the agenda does not yet say what was actually
  voted on. Conversely, the protocol lists its votings and elections (votings, elections).

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