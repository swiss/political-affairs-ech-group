---
search:
  boost: 5.0
---

# Slot: attendances 


_Ensemble des listes de présence._




<div data-search-exclude markdown="1">



URI: [ops:attendance](https://ch.paf.link/schema/operations/attendance)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Container](Container.md) | Conteneur pour les données de l'activité publique des conseils : législatures... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Attendance](Attendance.md) |
| Domaine de | [Container](Container.md) |
| URI du slot | [ops:attendance](https://ch.paf.link/schema/operations/attendance) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: attendances
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung der Anwesenheitslisten.

      '
  description_fr:
    tag: description_fr
    value: 'Ensemble des listes de présence.

      '
description: 'Ensemble des listes de présence.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:attendance
domain_of:
- Container
range: Attendance
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>