---
search:
  boost: 5.0
---

# Slot: parent_protocol 


_Le procès-verbal dans lequel le vote ou l'élection est consigné. Le vote a lieu au cours de la séance et se rattache donc au procès-verbal, et non à l'ordre du jour planifié à l'avance : ce qui a été mis à l'ordre du jour ne dit pas encore sur quoi il a effectivement été voté. Inversement, le procès-verbal reprend ses votes et élections sous forme de listes (votings, elections)._




<div data-search-exclude markdown="1">



URI: [ops:parentProtocol](https://ch.paf.link/schema/operations/parentProtocol)
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
| Plage | [Protocol](Protocol.md) |
| Domaine de | [Voting](Voting.md), [Election](Election.md) |
| URI du slot | [ops:parentProtocol](https://ch.paf.link/schema/operations/parentProtocol) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

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
description: 'Le procès-verbal dans lequel le vote ou l''élection est consigné. Le
  vote a lieu au cours de la séance et se rattache donc au procès-verbal, et non à
  l''ordre du jour planifié à l''avance : ce qui a été mis à l''ordre du jour ne dit
  pas encore sur quoi il a effectivement été voté. Inversement, le procès-verbal reprend
  ses votes et élections sous forme de listes (votings, elections).

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