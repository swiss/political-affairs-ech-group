---
search:
  boost: 5.0
---

# Slot: parent_meeting 


_Identifiant de la séance liée qui regroupe la séance courante._




<div data-search-exclude markdown="1">



URI: [ops:parent_meeting](https://ch.paf.link/schema/operations/parent_meeting)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |  no  |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance |  no  |
| [Protocol](Protocol.md) | Le procès-verbal établi après la séance |  no  |
| [Voting](Voting.md) | Une procédure de vote avec les voix individuelles et les résultats |  no  |
| [Election](Election.md) | Une procédure d'élection visant à pourvoir des fonctions par des personnes |  no  |
| [Attendance](Attendance.md) | Liste de présence agrégée pour une séance (nombre de membres présents, absent... |  no  |
| [ProtocolItem](ProtocolItem.md) | Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Meeting](Meeting.md), [AgendaItem](AgendaItem.md), [Protocol](Protocol.md), [Voting](Voting.md), [Election](Election.md), [Attendance](Attendance.md) |

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
    value: 'Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant de la séance liée qui regroupe la séance courante.

      '
description: 'Identifiant de la séance liée qui regroupe la séance courante.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
- AgendaItem
- Protocol
- Voting
- Election
- Attendance
range: string

```
</details></div>