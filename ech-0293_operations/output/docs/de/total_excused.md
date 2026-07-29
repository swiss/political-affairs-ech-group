---
search:
  boost: 5.0
---

# Slot: total_excused 


_Gesamtzahl der entschuldigten Abwesenheiten._




<div data-search-exclude markdown="1">



URI: [ops:total_excused](https://ch.paf.link/schema/operations/total_excused)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Attendance](Attendance.md) | Aggregierte Anwesenheitsliste für eine Sitzung (Anzahl Anwesende, Abwesende, ... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Integer](Integer.md) |
| Domäne von | [Attendance](Attendance.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

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
description: 'Gesamtzahl der entschuldigten Abwesenheiten.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Attendance
range: integer

```
</details></div>