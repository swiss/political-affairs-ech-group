---
search:
  boost: 5.0
---

# Slot: total_count 


_Nombre total de membres de l'organe (valeur de référence pour le calcul du quorum)._




<div data-search-exclude markdown="1">



URI: [ops:total_count](https://ch.paf.link/schema/operations/total_count)
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
name: total_count
annotations:
  description_de:
    tag: description_de
    value: 'Gesamtzahl aller Mitglieder des Gremiums (Bezugsgrösse für Quorum-Berechnungen).

      '
  description_fr:
    tag: description_fr
    value: 'Nombre total de membres de l''organe (valeur de référence pour le calcul
      du quorum).

      '
description: 'Nombre total de membres de l''organe (valeur de référence pour le calcul
  du quorum).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Attendance
range: integer

```
</details></div>