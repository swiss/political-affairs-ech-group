---
search:
  boost: 5.0
---

# Slot: reason 


_Grund für Abwesenheit oder Verspätung (Freitext, mehrsprachig)._




<div data-search-exclude markdown="1">



URI: [ops:reason](https://ch.paf.link/schema/operations/reason)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [IndividualAttendance](IndividualAttendance.md) | Einzelne Anwesenheitsfeststellung einer Person an einer Sitzung (verknüpft üb... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [MultilingualString](MultilingualString.md) |
| Domäne von | [IndividualAttendance](IndividualAttendance.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |












## LinkML-Quelle

<details>
```yaml
name: reason
annotations:
  description_de:
    tag: description_de
    value: 'Grund für Abwesenheit oder Verspätung (Freitext, mehrsprachig).

      '
  description_fr:
    tag: description_fr
    value: 'Motif de l''absence ou du retard (texte libre, multilingue).

      '
description: 'Grund für Abwesenheit oder Verspätung (Freitext, mehrsprachig).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IndividualAttendance
range: MultilingualString
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>