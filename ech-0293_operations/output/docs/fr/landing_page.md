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
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |  no  |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance |  no  |
| [Voting](Voting.md) | Une procédure de vote avec les voix individuelles et les résultats |  no  |
| [Election](Election.md) | Une procédure d'élection visant à pourvoir des fonctions par des personnes |  no  |
| [Speech](Speech.md) | Une intervention prononcée au cours d'une séance (également appelée prise de ... |  no  |
| [ProtocolItem](ProtocolItem.md) | Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Legislature](Legislature.md), [Meeting](Meeting.md), [AgendaItem](AgendaItem.md), [Voting](Voting.md), [Election](Election.md), [Speech](Speech.md) |
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
- AgendaItem
- Voting
- Election
- Speech
range: string

```
</details></div>