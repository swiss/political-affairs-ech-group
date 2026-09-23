---
search:
  boost: 5.0
---

# Slot: parent_meeting 


_Identifiant de la séance à laquelle cet enregistrement se rattache. Pour une séance, il désigne la séance supérieure ; pour un point de l'ordre du jour, un vote, une élection, une intervention ou un procès-verbal, la séance au cours de laquelle l'enregistrement est né._




<div data-search-exclude markdown="1">



URI: [ops:parent_meeting](https://ch.paf.link/schema/operations/parent_meeting)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |  no  |
| [IsAgendaItem](IsAgendaItem.md) | Une classe mixin qui fournit les éléments d'un point de l'ordre du jour : dés... |  no  |
| [Protocol](Protocol.md) | Le procès-verbal établi après la séance |  no  |
| [Voting](Voting.md) | Une procédure de vote avec les voix individuelles et les résultats |  no  |
| [Election](Election.md) | Une procédure d'élection visant à pourvoir des fonctions par des personnes |  no  |
| [Attendance](Attendance.md) | Liste de présence agrégée pour une séance (nombre de membres présents, absent... |  no  |
| [Speech](Speech.md) | Une intervention prononcée au cours d'une séance (également appelée prise de ... |  no  |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance |  no  |
| [ProtocolItem](ProtocolItem.md) | Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Meeting](Meeting.md), [IsAgendaItem](IsAgendaItem.md), [Protocol](Protocol.md), [Voting](Voting.md), [Election](Election.md), [Attendance](Attendance.md), [Speech](Speech.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: parent_meeting
annotations:
  description_de:
    tag: description_de
    value: 'Identifikator der Sitzung, zu der dieser Eintrag gehört. Bei einer Sitzung
      bezeichnet er die übergeordnete Sitzung, bei Traktandum, Abstimmung, Wahl, Wortmeldung
      oder Protokoll die Sitzung, in der der Eintrag entstanden ist.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant de la séance à laquelle cet enregistrement se rattache. Pour
      une séance, il désigne la séance supérieure ; pour un point de l''ordre du jour,
      un vote, une élection, une intervention ou un procès-verbal, la séance au cours
      de laquelle l''enregistrement est né.

      '
description: 'Identifiant de la séance à laquelle cet enregistrement se rattache.
  Pour une séance, il désigne la séance supérieure ; pour un point de l''ordre du
  jour, un vote, une élection, une intervention ou un procès-verbal, la séance au
  cours de laquelle l''enregistrement est né.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
- IsAgendaItem
- Protocol
- Voting
- Election
- Attendance
- Speech
range: string

```
</details></div>