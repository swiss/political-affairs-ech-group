---
search:
  boost: 5.0
---

# Slot: position 


_Ganzzahlige Position innerhalb der übergeordneten Reihenfolge, z.B. einer Session innerhalb der Legislaturperiode._




<div data-search-exclude markdown="1">



URI: [ops:position](https://ch.paf.link/schema/operations/position)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Session](Session.md) | Eine Session: eine zusammenhängende Sitzungsperiode innerhalb einer Legislatu... |  no  |
| [Meeting](Meeting.md) | Die einzelne Sitzung eines Organs — die Ebene, auf der Traktanden beraten, Be... |  no  |






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
    value: 'Ganzzahlige Position innerhalb der übergeordneten Reihenfolge, z.B. einer
      Session innerhalb der Legislaturperiode.

      '
  description_fr:
    tag: description_fr
    value: 'Position entière au sein de la séquence supérieure, p. ex. d''une session
      au sein de la législature.

      '
description: 'Ganzzahlige Position innerhalb der übergeordneten Reihenfolge, z.B.
  einer Session innerhalb der Legislaturperiode.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: string

```
</details></div>