---
search:
  boost: 5.0
---

# Slot: state 


_Aktueller Status der Sitzung (geplant, abgesagt, verschoben)._




<div data-search-exclude markdown="1">



URI: [ops:state](https://ch.paf.link/schema/operations/state)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sess... |  no  |






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
    value: 'Aktueller Status der Sitzung (geplant, abgesagt, verschoben).

      '
  description_fr:
    tag: description_fr
    value: 'État actuel de la séance (planifiée, annulée, reportée).

      '
description: 'Aktueller Status der Sitzung (geplant, abgesagt, verschoben).

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