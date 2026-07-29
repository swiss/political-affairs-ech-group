---
search:
  boost: 5.0
---

# Slot: agenda_item_number 


_Numéro d'ordre du point de l'ordre du jour (type chaîne, afin de permettre les chiffres romains)._




<div data-search-exclude markdown="1">



URI: [ops:agenda_item_number](https://ch.paf.link/schema/operations/agenda_item_number)
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
| Plage | [String](String.md) |
| Domaine de | [AgendaItem](AgendaItem.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: agenda_item_number
annotations:
  description_de:
    tag: description_de
    value: 'Laufnummer des Traktandums (String-Typ zur Unterstützung römischer Ziffern).

      '
  description_fr:
    tag: description_fr
    value: 'Numéro d''ordre du point de l''ordre du jour (type chaîne, afin de permettre
      les chiffres romains).

      '
description: 'Numéro d''ordre du point de l''ordre du jour (type chaîne, afin de permettre
  les chiffres romains).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: string

```
</details></div>