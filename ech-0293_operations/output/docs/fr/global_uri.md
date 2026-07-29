---
search:
  boost: 5.0
---

# Slot: global_uri 


_Une URI unique et globalement valide pour l'entité._




<div data-search-exclude markdown="1">



URI: [mcm:globalURI](https://ld.ech.ch/schema/0292/meta-common/globalURI)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [HasIdentification](HasIdentification.md) | Une classe mixin qui fournit des slots pour l'identification d'une entité |  no  |
| [IsProcessStep](IsProcessStep.md) | Une classe mixin pour une étape unique dans un processus |  no  |
| [Container](Container.md) | Conteneur pour les données de l'activité publique des conseils : législatures... |  no  |
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
| [TextSegment](TextSegment.md) | Un segment de texte tel qu'un renvoi ou un intertitre dans un procès-verbal d... |  no  |
| [Motion](Motion.md) | Une proposition formelle déposée au cours des délibérations |  no  |
| [Media](Media.md) | Fichiers médias ou documents (y compris les procès-verbaux en PDF/HTML/WORD o... |  no  |
| [PersonReference](PersonReference.md) | Référence légère à une personne avec les principales données d'identification... |  no  |
| [GroupReference](GroupReference.md) | Référence légère à un groupe avec les principales données d'identification au... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Uriorcurie](Uriorcurie.md) |
| Domaine de | [HasIdentification](HasIdentification.md), [IsProcessStep](IsProcessStep.md) |
| URI du slot | [mcm:globalURI](https://ld.ech.ch/schema/0292/meta-common/globalURI) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Requis | Yes |
### Caractéristiques du slot

| Propriété | Valeur |
| --- | --- |
| Identifiant | Yes |














## Source LinkML

<details>
```yaml
name: global_uri
annotations:
  description_de:
    tag: description_de
    value: 'Eine eindeutige, global gültige URI für die Entität.

      '
  description_fr:
    tag: description_fr
    value: 'Une URI unique et globalement valide pour l''entité.

      '
description: 'Une URI unique et globalement valide pour l''entité.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:globalURI
identifier: true
domain_of:
- HasIdentification
- IsProcessStep
range: uriorcurie
required: true

```
</details></div>