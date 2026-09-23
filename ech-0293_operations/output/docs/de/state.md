---
search:
  boost: 5.0
---

# Slot: state 


_Ob die Sitzung überhaupt wie vorgesehen stattfindet (geplant, abgesagt, verschoben). Eine abweichende, freitextliche Bezeichnung nimmt `state_name` auf._




<div data-search-exclude markdown="1">



URI: [ops:state](https://ch.paf.link/schema/operations/state)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | Die einzelne Sitzung eines Organs — die Ebene, auf der Traktanden beraten, Be... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [StateEnum](StateEnum.md) |
| Domäne von | [Meeting](Meeting.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| planned |





## LinkML-Quelle

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
description: 'Ob die Sitzung überhaupt wie vorgesehen stattfindet (geplant, abgesagt,
  verschoben). Eine abweichende, freitextliche Bezeichnung nimmt `state_name` auf.

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