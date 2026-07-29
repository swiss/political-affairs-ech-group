---
search:
  boost: 5.0
---

# Slot: position 


_Position (nombre entier) au sein de la séquence supérieure._




<div data-search-exclude markdown="1">



URI: [ops:position](https://ch.paf.link/schema/operations/position)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Session](Session.md) | Une session parlementaire qui regroupe plusieurs séances et s'étend sur une p... |  no  |
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Session](Session.md), [Meeting](Meeting.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: position
annotations:
  description_de:
    tag: description_de
    value: 'Ganzzahlige Position innerhalb der übergeordneten Reihenfolge.

      '
  description_fr:
    tag: description_fr
    value: 'Position (nombre entier) au sein de la séquence supérieure.

      '
description: 'Position (nombre entier) au sein de la séquence supérieure.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>