---
search:
  boost: 5.0
---

# Slot: parent_agenda_item 


_Au besoin, ce slot permet de construire une hiérarchie de points de l'ordre du jour._




<div data-search-exclude markdown="1">



URI: [ops:parent_agenda_item](https://ch.paf.link/schema/operations/parent_agenda_item)
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
name: parent_agenda_item
annotations:
  description_de:
    tag: description_de
    value: 'Wenn erforderlich, baut dieser Slot eine Hierarchie von Traktanden auf.

      '
  description_fr:
    tag: description_fr
    value: 'Au besoin, ce slot permet de construire une hiérarchie de points de l''ordre
      du jour.

      '
description: 'Au besoin, ce slot permet de construire une hiérarchie de points de
  l''ordre du jour.

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