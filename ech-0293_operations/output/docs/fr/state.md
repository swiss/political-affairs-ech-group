---
search:
  boost: 5.0
---

# Slot: state 


_Indique si la séance a lieu comme prévu (planifiée, annulée, reportée). Une désignation divergente, en texte libre, est reprise dans `state_name`._




<div data-search-exclude markdown="1">



URI: [ops:state](https://ch.paf.link/schema/operations/state)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | La séance individuelle d'un organe — le niveau auquel les points de l'ordre d... |  no  |






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
    value: 'Ob die Sitzung überhaupt wie vorgesehen stattfindet (geplant, abgesagt,
      verschoben). Eine abweichende, freitextliche Bezeichnung nimmt `state_name`
      auf.

      '
  description_fr:
    tag: description_fr
    value: 'Indique si la séance a lieu comme prévu (planifiée, annulée, reportée).
      Une désignation divergente, en texte libre, est reprise dans `state_name`.

      '
description: 'Indique si la séance a lieu comme prévu (planifiée, annulée, reportée).
  Une désignation divergente, en texte libre, est reprise dans `state_name`.

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