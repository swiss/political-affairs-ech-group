---
search:
  boost: 5.0
---

# Slot: has_resolution 


_La décision prise sur ce point de l'ordre du jour._




<div data-search-exclude markdown="1">



URI: [ops:has_resolution](https://ch.paf.link/schema/operations/has_resolution)
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
| Plage | [Resolution](Resolution.md) |
| Domaine de | [AgendaItem](AgendaItem.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: has_resolution
annotations:
  description_de:
    tag: description_de
    value: 'Die Resolution oder Entscheidung zu diesem Traktandum.

      '
  description_fr:
    tag: description_fr
    value: 'La décision prise sur ce point de l''ordre du jour.

      '
description: 'La décision prise sur ce point de l''ordre du jour.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: Resolution

```
</details></div>