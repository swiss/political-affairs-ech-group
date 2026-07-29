---
search:
  boost: 5.0
---

# Slot: documents 


_Liste des documents (FRBR Works) liés à l'entité._




<div data-search-exclude markdown="1">



URI: [meta:documents](https://ch.paf.link/schema/meta/documents)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | Durée du mandat d'un parlement en tant qu'assemblée législative |  no  |
| [Session](Session.md) | Une session parlementaire qui regroupe plusieurs séances et s'étend sur une p... |  no  |
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |  no  |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance |  no  |
| [Protocol](Protocol.md) | Le procès-verbal établi après la séance |  no  |
| [Resolution](Resolution.md) | Une décision prise sur un point de l'ordre du jour, y compris les procédures ... |  no  |
| [Voting](Voting.md) | Une procédure de vote avec les voix individuelles et les résultats |  no  |
| [Election](Election.md) | Une procédure d'élection visant à pourvoir des fonctions par des personnes |  no  |
| [Speech](Speech.md) | Une intervention prononcée au cours d'une séance (également appelée prise de ... |  no  |
| [Motion](Motion.md) | Une proposition formelle déposée au cours des délibérations |  no  |
| [ProtocolItem](ProtocolItem.md) | Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Work](Work.md) |
| Domaine de | [Legislature](Legislature.md), [Session](Session.md), [Meeting](Meeting.md), [AgendaItem](AgendaItem.md), [Protocol](Protocol.md), [Resolution](Resolution.md), [Voting](Voting.md), [Election](Election.md), [Speech](Speech.md), [Motion](Motion.md) |
| URI du slot | [meta:documents](https://ch.paf.link/schema/meta/documents) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: documents
annotations:
  description_de:
    tag: description_de
    value: 'Liste von Dokumenten (FRBR Works), die mit der Entität verknüpft sind.

      '
  description_fr:
    tag: description_fr
    value: 'Liste des documents (FRBR Works) liés à l''entité.

      '
description: 'Liste des documents (FRBR Works) liés à l''entité.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:documents
domain_of:
- Legislature
- Session
- Meeting
- AgendaItem
- Protocol
- Resolution
- Voting
- Election
- Speech
- Motion
range: Work
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>