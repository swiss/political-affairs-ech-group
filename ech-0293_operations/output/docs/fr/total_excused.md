---
search:
  boost: 5.0
---

# Slot: total_excused 


_Nombre total d'absences excusées._




<div data-search-exclude markdown="1">



URI: [ops:total_excused](https://ch.paf.link/schema/operations/total_excused)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Attendance](Attendance.md) | Liste de présence agrégée pour une séance (nombre de membres présents, absent... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Integer](Integer.md) |
| Domaine de | [Attendance](Attendance.md) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |












## Source LinkML

<details>
```yaml
name: total_excused
annotations:
  description_de:
    tag: description_de
    value: 'Gesamtzahl der entschuldigten Abwesenheiten.

      '
  description_fr:
    tag: description_fr
    value: 'Nombre total d''absences excusées.

      '
description: 'Nombre total d''absences excusées.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Attendance
range: integer

```
</details></div>