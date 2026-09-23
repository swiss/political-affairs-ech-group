---
search:
  boost: 5.0
---

# Slot: landing_page 


_URL fournissant des informations complémentaires._




<div data-search-exclude markdown="1">



URI: [ops:landingPage](https://ch.paf.link/schema/operations/landingPage)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Legislature](Legislature.md) | Durée du mandat d'un parlement en tant qu'assemblée législative |  no  |
| [Meeting](Meeting.md) | La séance individuelle d'un organe — le niveau auquel les points de l'ordre d... |  no  |
| [IsAgendaItem](IsAgendaItem.md) | Une classe mixin qui fournit les éléments d'un point de l'ordre du jour : dés... |  no  |
| [Voting](Voting.md) | Un vote sur une question matérielle : l'objet du vote (la question), la procé... |  no  |
| [Election](Election.md) | Une élection par laquelle un organe parlementaire désigne une ou plusieurs pe... |  no  |
| [Speech](Speech.md) | Une intervention prononcée au cours d'une séance (également appelée prise de ... |  no  |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance, tel que planifié à l'avance |  no  |
| [ProtocolItem](ProtocolItem.md) | Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Legislature](Legislature.md), [Meeting](Meeting.md), [IsAgendaItem](IsAgendaItem.md), [Voting](Voting.md), [Election](Election.md), [Speech](Speech.md) |
| URI du slot | [ops:landingPage](https://ch.paf.link/schema/operations/landingPage) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: landing_page
annotations:
  description_de:
    tag: description_de
    value: 'URL mit weiteren Informationen.

      '
  description_fr:
    tag: description_fr
    value: 'URL fournissant des informations complémentaires.

      '
description: 'URL fournissant des informations complémentaires.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:landingPage
domain_of:
- Legislature
- Meeting
- IsAgendaItem
- Voting
- Election
- Speech
range: string

```
</details></div>