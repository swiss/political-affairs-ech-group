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
| [Session](Session.md) | Une session : une période de séances continue au sein d'une législature |  no  |
| [Meeting](Meeting.md) | La séance individuelle d'un organe — le niveau auquel les points de l'ordre d... |  yes  |
| [IsAgendaItem](IsAgendaItem.md) | Une classe mixin qui fournit les éléments d'un point de l'ordre du jour : dés... |  yes  |
| [Protocol](Protocol.md) | Le procès-verbal d'une séance, établi après celle-ci et tenu exactement une f... |  no  |
| [Resolution](Resolution.md) | La décision formelle prise sur un point de l'ordre du jour, y compris les pro... |  no  |
| [Voting](Voting.md) | Un vote sur une question matérielle : l'objet du vote (la question), la procé... |  no  |
| [Election](Election.md) | Une élection par laquelle un organe parlementaire désigne une ou plusieurs pe... |  no  |
| [Speech](Speech.md) | Une intervention prononcée au cours d'une séance (également appelée prise de ... |  no  |
| [Motion](Motion.md) | Une proposition formelle déposée au cours des délibérations, par exemple une ... |  no  |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance, tel que planifié à l'avance |  no  |
| [ProtocolItem](ProtocolItem.md) | Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Work](Work.md) |
| Domaine de | [Legislature](Legislature.md), [Session](Session.md), [Meeting](Meeting.md), [IsAgendaItem](IsAgendaItem.md), [Protocol](Protocol.md), [Resolution](Resolution.md), [Voting](Voting.md), [Election](Election.md), [Speech](Speech.md), [Motion](Motion.md) |
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
- IsAgendaItem
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