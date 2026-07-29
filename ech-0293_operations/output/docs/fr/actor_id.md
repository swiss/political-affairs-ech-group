---
search:
  boost: 5.0
---

# Slot: actor_id 


_Référence à la personne agissante (instantané allégé au moment de la mise en relation)._




<div data-search-exclude markdown="1">



URI: [ops:actor_id](https://ch.paf.link/schema/operations/actor_id)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | Durée du mandat d'un parlement en tant qu'assemblée législative |  yes  |
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |  yes  |
| [Voting](Voting.md) | Une procédure de vote avec les voix individuelles et les résultats |  yes  |
| [IndividualVote](IndividualVote.md) | Une voix individuelle exprimée par un membre lors d'une procédure de vote |  no  |
| [Election](Election.md) | Une procédure d'élection visant à pourvoir des fonctions par des personnes |  yes  |
| [Attendance](Attendance.md) | Liste de présence agrégée pour une séance (nombre de membres présents, absent... |  yes  |
| [IndividualAttendance](IndividualAttendance.md) | Constatation individuelle de la présence d'une personne à une séance (rattach... |  no  |
| [Speech](Speech.md) | Une intervention prononcée au cours d'une séance (également appelée prise de ... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [PersonReference](PersonReference.md) |
| Domaine de | [Legislature](Legislature.md), [Meeting](Meeting.md), [Voting](Voting.md), [IndividualVote](IndividualVote.md), [Election](Election.md), [Attendance](Attendance.md), [IndividualAttendance](IndividualAttendance.md), [Speech](Speech.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: actor_id
annotations:
  description_de:
    tag: description_de
    value: 'Referenz auf die handelnde Person (leichtgewichtiger Snapshot zum Zeitpunkt
      der Verknüpfung).

      '
  description_fr:
    tag: description_fr
    value: 'Référence à la personne agissante (instantané allégé au moment de la mise
      en relation).

      '
description: 'Référence à la personne agissante (instantané allégé au moment de la
  mise en relation).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Legislature
- Meeting
- Voting
- IndividualVote
- Election
- Attendance
- IndividualAttendance
- Speech
range: PersonReference
inlined: true

```
</details></div>