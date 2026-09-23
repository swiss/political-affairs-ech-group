---
search:
  boost: 5.0
---

# Slot: parent_meeting 


_Identifiant de la séance à laquelle cet enregistrement se rattache. Pour une séance, il désigne la séance supérieure ; pour un vote, une élection, une intervention, une liste de présence ou un procès-verbal, la séance au cours de laquelle l'enregistrement est né. Les points de l'ordre du jour ne le portent pas : ils sont imbriqués dans leur séance._




<div data-search-exclude markdown="1">



URI: [ops:parent_meeting](https://ch.paf.link/schema/operations/parent_meeting)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | La séance individuelle d'un organe — le niveau auquel les points de l'ordre d... |  no  |
| [Protocol](Protocol.md) | Le procès-verbal d'une séance, établi après celle-ci et tenu exactement une f... |  no  |
| [Voting](Voting.md) | Un vote sur une question matérielle : l'objet du vote (la question), la procé... |  no  |
| [Election](Election.md) | Une élection par laquelle un organe parlementaire désigne une ou plusieurs pe... |  no  |
| [Attendance](Attendance.md) | Liste de présence agrégée pour une séance (nombre de membres présents, absent... |  no  |
| [Speech](Speech.md) | Une intervention prononcée au cours d'une séance (également appelée prise de ... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Meeting](Meeting.md), [Protocol](Protocol.md), [Voting](Voting.md), [Election](Election.md), [Attendance](Attendance.md), [Speech](Speech.md) |

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
      bezeichnet er die übergeordnete Sitzung, bei Abstimmung, Wahl, Wortmeldung,
      Anwesenheitsliste oder Protokoll die Sitzung, in der der Eintrag entstanden
      ist. Traktanden führen ihn nicht: Sie sind in ihre Sitzung eingebettet.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant de la séance à laquelle cet enregistrement se rattache. Pour
      une séance, il désigne la séance supérieure ; pour un vote, une élection, une
      intervention, une liste de présence ou un procès-verbal, la séance au cours
      de laquelle l''enregistrement est né. Les points de l''ordre du jour ne le portent
      pas : ils sont imbriqués dans leur séance.

      '
description: 'Identifiant de la séance à laquelle cet enregistrement se rattache.
  Pour une séance, il désigne la séance supérieure ; pour un vote, une élection, une
  intervention, une liste de présence ou un procès-verbal, la séance au cours de laquelle
  l''enregistrement est né. Les points de l''ordre du jour ne le portent pas : ils
  sont imbriqués dans leur séance.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
- Protocol
- Voting
- Election
- Attendance
- Speech
range: string

```
</details></div>