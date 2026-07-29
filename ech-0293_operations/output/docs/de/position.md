---
search:
  boost: 5.0
---

# Slot: position 


_Ganzzahlige Position innerhalb der übergeordneten Reihenfolge._




<div data-search-exclude markdown="1">



URI: [ops:position](https://ch.paf.link/schema/operations/position)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Session](Session.md) | Eine Parlamentssession, die mehrere Sitzungen gruppiert und sich über einen b... |  no  |
| [Meeting](Meeting.md) | Eine allgemeine Sitzungsklasse, die für Sessionen, Kommissionssitzungen, Sess... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Session](Session.md), [Meeting](Meeting.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: position
annotations:
  description_de:
    tag: description_de
    value: 'Ganzzahlige Position innerhalb der übergeordneten Reihenfolge.

      '
  description_fr:
    tag: description_fr
    value: 'Position (nombre entier) au sein de la séquence supérieure.

      '
description: 'Ganzzahlige Position innerhalb der übergeordneten Reihenfolge.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>