---
search:
  boost: 5.0
---

# Slot: agenda_item_description 


_Sous-titre ou description détaillée du point de l'ordre du jour._




<div data-search-exclude markdown="1">



URI: [ops:agenda_item_description](https://ch.paf.link/schema/operations/agenda_item_description)
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
| Plage | [MultilingualString](MultilingualString.md) |
| Domaine de | [AgendaItem](AgendaItem.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: agenda_item_description
annotations:
  description_de:
    tag: description_de
    value: 'Untertitel oder ausführliche Beschreibung des Traktandums.

      '
  description_fr:
    tag: description_fr
    value: 'Sous-titre ou description détaillée du point de l''ordre du jour.

      '
description: 'Sous-titre ou description détaillée du point de l''ordre du jour.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: MultilingualString
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>