---
search:
  boost: 5.0
---

# Slot: agenda_item_position 


_Position (nombre entier) du point de l'ordre du jour dans le déroulement de la séance._




<div data-search-exclude markdown="1">



URI: [ops:agenda_item_position](https://ch.paf.link/schema/operations/agenda_item_position)
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
| Plage | [Integer](Integer.md) |
| Domaine de | [AgendaItem](AgendaItem.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: agenda_item_position
annotations:
  description_de:
    tag: description_de
    value: 'Ganzzahlige Position des Traktandums in der Sitzungsreihenfolge.

      '
  description_fr:
    tag: description_fr
    value: 'Position (nombre entier) du point de l''ordre du jour dans le déroulement
      de la séance.

      '
description: 'Position (nombre entier) du point de l''ordre du jour dans le déroulement
  de la séance.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: integer

```
</details></div>