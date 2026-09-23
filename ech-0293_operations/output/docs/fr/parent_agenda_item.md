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
| [IsAgendaItem](IsAgendaItem.md) | Une classe mixin qui fournit les éléments d'un point de l'ordre du jour : dés... |  no  |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance |  no  |
| [ProtocolItem](ProtocolItem.md) | Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [IsAgendaItem](IsAgendaItem.md) |

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
- IsAgendaItem
range: string

```
</details></div>