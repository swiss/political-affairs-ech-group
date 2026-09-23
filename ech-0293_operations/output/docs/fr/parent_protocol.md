---
search:
  boost: 5.0
---

# Slot: parent_protocol 


_Le procès-verbal dans lequel le vote ou l'élection est consigné. Un vote a lieu au cours de la séance et se rattache donc au procès-verbal et non à l'ordre du jour planifié à l'avance._




<div data-search-exclude markdown="1">



URI: [ops:parentProtocol](https://ch.paf.link/schema/operations/parentProtocol)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Voting](Voting.md) | Une procédure de vote avec les voix individuelles et les résultats |  no  |
| [Election](Election.md) | Une procédure d'élection visant à pourvoir des fonctions par des personnes |  no  |






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
      wird im Verlauf der Sitzung; die Abstimmung hängt deshalb am Protokoll und nicht
      an der vorgängig geplanten Traktandenliste.

      '
  description_fr:
    tag: description_fr
    value: 'Le procès-verbal dans lequel le vote ou l''élection est consigné. Un vote
      a lieu au cours de la séance et se rattache donc au procès-verbal et non à l''ordre
      du jour planifié à l''avance.

      '
description: 'Le procès-verbal dans lequel le vote ou l''élection est consigné. Un
  vote a lieu au cours de la séance et se rattache donc au procès-verbal et non à
  l''ordre du jour planifié à l''avance.

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