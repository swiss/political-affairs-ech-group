---
search:
  boost: 5.0
---

# Slot: state 


_État actuel de la séance (planifiée, annulée, reportée)._




<div data-search-exclude markdown="1">



URI: [ops:state](https://ch.paf.link/schema/operations/state)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | Une classe générale de séance utilisée pour les sessions, les séances de comm... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [StateEnum](StateEnum.md) |
| Domaine de | [Meeting](Meeting.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |









## Exemples

| Valeur |
| --- |
| planned |





## Source LinkML

<details>
```yaml
name: state
annotations:
  description_de:
    tag: description_de
    value: 'Aktueller Status der Sitzung (geplant, abgesagt, verschoben).

      '
  description_fr:
    tag: description_fr
    value: 'État actuel de la séance (planifiée, annulée, reportée).

      '
description: 'État actuel de la séance (planifiée, annulée, reportée).

  '
examples:
- value: planned
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
range: StateEnum

```
</details></div>