---
search:
  boost: 5.0
---

# Slot: affair_id 


_Le lien vers les affaires rattachées au point de l'ordre du jour._




<div data-search-exclude markdown="1">



URI: [ops:affair_id](https://ch.paf.link/schema/operations/affair_id)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance |  no  |
| [Voting](Voting.md) | Une procédure de vote avec les voix individuelles et les résultats |  no  |
| [Election](Election.md) | Une procédure d'élection visant à pourvoir des fonctions par des personnes |  no  |
| [ProtocolItem](ProtocolItem.md) | Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [AgendaItem](AgendaItem.md), [Voting](Voting.md), [Election](Election.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: affair_id
annotations:
  description_de:
    tag: description_de
    value: 'Die Verbindung zu den Geschäften des Traktandums.

      '
  description_fr:
    tag: description_fr
    value: 'Le lien vers les affaires rattachées au point de l''ordre du jour.

      '
description: 'Le lien vers les affaires rattachées au point de l''ordre du jour.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
- Voting
- Election
range: string

```
</details></div>