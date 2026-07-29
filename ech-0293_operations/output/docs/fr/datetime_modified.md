---
search:
  boost: 5.0
---

# Slot: datetime_modified 


_La date et l'heure auxquelles une entité a été modifiée pour la dernière fois._




<div data-search-exclude markdown="1">



URI: [mcm:datetimeModified](https://ld.ech.ch/schema/0292/meta-common/datetimeModified)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [HasCreationModificationDates](HasCreationModificationDates.md) | Une classe mixin qui fournit des slots pour modéliser les dates de création e... |  no  |
| [Legislature](Legislature.md) | Durée du mandat d'un parlement en tant qu'assemblée législative |  no  |
| [Session](Session.md) | Une session parlementaire qui regroupe plusieurs séances et s'étend sur une p... |  no  |
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |  no  |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance |  no  |
| [Protocol](Protocol.md) | Le procès-verbal établi après la séance |  no  |
| [ProtocolItem](ProtocolItem.md) | Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-... |  no  |
| [Voting](Voting.md) | Une procédure de vote avec les voix individuelles et les résultats |  no  |
| [IndividualVote](IndividualVote.md) | Une voix individuelle exprimée par un membre lors d'une procédure de vote |  no  |
| [Election](Election.md) | Une procédure d'élection visant à pourvoir des fonctions par des personnes |  no  |
| [Attendance](Attendance.md) | Liste de présence agrégée pour une séance (nombre de membres présents, absent... |  no  |
| [IndividualAttendance](IndividualAttendance.md) | Constatation individuelle de la présence d'une personne à une séance (rattach... |  no  |
| [Speech](Speech.md) | Une intervention prononcée au cours d'une séance (également appelée prise de ... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Datetime](Datetime.md) |
| Domaine de | [HasCreationModificationDates](HasCreationModificationDates.md) |
| URI du slot | [mcm:datetimeModified](https://ld.ech.ch/schema/0292/meta-common/datetimeModified) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: datetime_modified
annotations:
  description_de:
    tag: description_de
    value: 'Das Datum und die Uhrzeit, an dem eine Entität zuletzt geändert wurde.

      '
  description_fr:
    tag: description_fr
    value: 'La date et l''heure auxquelles une entité a été modifiée pour la dernière
      fois.

      '
description: 'La date et l''heure auxquelles une entité a été modifiée pour la dernière
  fois.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:datetimeModified
domain_of:
- HasCreationModificationDates
range: datetime

```
</details></div>