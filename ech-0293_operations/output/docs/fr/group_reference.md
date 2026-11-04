---
search:
  boost: 5.0
---

# Slot: group_reference 


_Référence abrégée à un groupe ou à un organe selon eCH-0294, retenant ses caractéristiques au moment de la mise en relation._




<div data-search-exclude markdown="1">



URI: [actors:groupReference](https://ld.ech.ch/schema/0294/actors/groupReference)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | Durée du mandat d'un parlement en tant qu'assemblée législative |  yes  |
| [Meeting](Meeting.md) | La séance individuelle d'un organe — le niveau auquel les points de l'ordre d... |  yes  |
| [Voting](Voting.md) | Un vote sur une question matérielle : l'objet du vote (la question), la procé... |  yes  |
| [Election](Election.md) | Une élection par laquelle un organe parlementaire désigne une ou plusieurs pe... |  yes  |
| [Attendance](Attendance.md) | Liste de présence agrégée pour une séance (nombre de membres présents, absent... |  yes  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [GroupReference](GroupReference.md) |
| Domaine de | [Legislature](Legislature.md), [Meeting](Meeting.md), [Voting](Voting.md), [Election](Election.md), [Attendance](Attendance.md) |
| URI du slot | [actors:groupReference](https://ld.ech.ch/schema/0294/actors/groupReference) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: group_reference
annotations:
  description_de:
    tag: description_de
    value: 'Kurzreferenz auf eine Gruppe oder ein Organ gemäss eCH-0294, welche deren
      Merkmale zum Zeitpunkt der Verknüpfung festhält.

      '
  description_fr:
    tag: description_fr
    value: 'Référence abrégée à un groupe ou à un organe selon eCH-0294, retenant
      ses caractéristiques au moment de la mise en relation.

      '
description: 'Référence abrégée à un groupe ou à un organe selon eCH-0294, retenant
  ses caractéristiques au moment de la mise en relation.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: actors:groupReference
domain_of:
- Legislature
- Meeting
- Voting
- Election
- Attendance
range: GroupReference
inlined: true

```
</details></div>