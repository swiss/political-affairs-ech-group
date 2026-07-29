---
search:
  boost: 5.0
---

# Slot: total_count 


_Gesamtzahl aller Mitglieder des Gremiums (Bezugsgrösse für Quorum-Berechnungen)._




<div data-search-exclude markdown="1">



URI: [ops:total_count](https://ch.paf.link/schema/operations/total_count)
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
description: 'Gesamtzahl aller Mitglieder des Gremiums (Bezugsgrösse für Quorum-Berechnungen).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Attendance
range: integer

```
</details></div>