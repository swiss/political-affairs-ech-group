---
search:
  boost: 5.0
---

# Slot: state_id 


_Identifiant d'état (renvoi à l'énumération des états ou à un état propre)._




<div data-search-exclude markdown="1">



URI: [ops:state_id](https://ch.paf.link/schema/operations/state_id)
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
name: state_id
annotations:
  description_de:
    tag: description_de
    value: 'Zustands-Identifikator (Verweis auf das Status-Enum oder auf einen eigenen
      Zustand).

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant d''état (renvoi à l''énumération des états ou à un état propre).

      '
description: 'Identifiant d''état (renvoi à l''énumération des états ou à un état
  propre).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IsAgendaItem
range: string

```
</details></div>