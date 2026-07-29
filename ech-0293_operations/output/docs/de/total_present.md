---
search:
  boost: 5.0
---

# Slot: total_present 


_Gesamtzahl der anwesenden Mitglieder._




<div data-search-exclude markdown="1">



URI: [ops:total_present](https://ch.paf.link/schema/operations/total_present)
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
name: total_present
annotations:
  description_de:
    tag: description_de
    value: 'Gesamtzahl der anwesenden Mitglieder.

      '
  description_fr:
    tag: description_fr
    value: 'Nombre total de membres présents.

      '
description: 'Gesamtzahl der anwesenden Mitglieder.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Attendance
range: integer

```
</details></div>