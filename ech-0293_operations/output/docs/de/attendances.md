---
search:
  boost: 5.0
---

# Slot: attendances 


_Sammlung der Anwesenheitslisten._




<div data-search-exclude markdown="1">



URI: [ops:attendance](https://ch.paf.link/schema/operations/attendance)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Container](Container.md) | Container für die Daten des öffentlichen Ratsbetriebs: Legislaturperioden, Se... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Attendance](Attendance.md) |
| Domäne von | [Container](Container.md) |
| Slot-URI | [ops:attendance](https://ch.paf.link/schema/operations/attendance) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

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
description: 'Sammlung der Anwesenheitslisten.

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