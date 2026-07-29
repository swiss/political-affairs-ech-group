---
search:
  boost: 5.0
---

# Slot: state_name 


_Description personnalisée de l'état de la séance._




<div data-search-exclude markdown="1">



URI: [ops:state_name](https://ch.paf.link/schema/operations/state_name)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |  no  |
| [AgendaItem](AgendaItem.md) | Un point de l'ordre du jour d'une séance |  no  |
| [ProtocolItem](ProtocolItem.md) | Un point de l'ordre du jour tel qu'il a effectivement été consigné au procès-... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Meeting](Meeting.md), [AgendaItem](AgendaItem.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: state_name
annotations:
  description_de:
    tag: description_de
    value: 'Benutzerdefinierte Zustandsbeschreibung für die Sitzung.

      '
  description_fr:
    tag: description_fr
    value: 'Description personnalisée de l''état de la séance.

      '
description: 'Description personnalisée de l''état de la séance.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
- AgendaItem
range: string

```
</details></div>