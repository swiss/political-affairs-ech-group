---
search:
  boost: 5.0
---

# Slot: agenda_item_type 


_Type de point de l'ordre du jour, distinguant les points isolés des groupes de points._




<div data-search-exclude markdown="1">



URI: [ops:agenda_item_type](https://ch.paf.link/schema/operations/agenda_item_type)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance |  no  |
| [ProtocolItem](ProtocolItem.md) | Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [AgendaItemTypeEnum](AgendaItemTypeEnum.md) |
| Domaine de | [AgendaItem](AgendaItem.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |









## Exemples

| Valeur |
| --- |
| item |





## Source LinkML

<details>
```yaml
name: agenda_item_type
annotations:
  description_de:
    tag: description_de
    value: 'Art des Traktandums, unterscheidet Einzeltraktanden von Traktandengruppen.

      '
  description_fr:
    tag: description_fr
    value: 'Type de point de l''ordre du jour, distinguant les points isolés des groupes
      de points.

      '
description: 'Type de point de l''ordre du jour, distinguant les points isolés des
  groupes de points.

  '
examples:
- value: item
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: AgendaItemTypeEnum

```
</details></div>