---
search:
  boost: 5.0
---

# Slot: leading_actor_id 


_Le département responsable du point de l'ordre du jour._




<div data-search-exclude markdown="1">



URI: [ops:leading_actor_id](https://ch.paf.link/schema/operations/leading_actor_id)
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
name: leading_actor_id
annotations:
  description_de:
    tag: description_de
    value: 'Das federführende Departement für das Traktandum.

      '
  description_fr:
    tag: description_fr
    value: 'Le département responsable du point de l''ordre du jour.

      '
description: 'Le département responsable du point de l''ordre du jour.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: string

```
</details></div>