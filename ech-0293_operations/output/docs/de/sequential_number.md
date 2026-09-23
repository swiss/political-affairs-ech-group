---
search:
  boost: 5.0
---

# Slot: sequential_number 


_Laufende Nummer der Session oder Sitzung als Ganzzahl, die zur Sortierung verwendet wird._




<div data-search-exclude markdown="1">



URI: [ops:sequential_number](https://ch.paf.link/schema/operations/sequential_number)
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
| Wertebereich | [Integer](Integer.md) |
| Domäne von | [Session](Session.md), [Meeting](Meeting.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: sequential_number
annotations:
  description_de:
    tag: description_de
    value: 'Laufende Nummer der Session oder Sitzung als Ganzzahl, die zur Sortierung
      verwendet wird.

      '
  description_fr:
    tag: description_fr
    value: 'Numéro d''ordre de la session ou de la séance sous forme de nombre entier,
      utilisé pour le tri.

      '
description: 'Laufende Nummer der Session oder Sitzung als Ganzzahl, die zur Sortierung
  verwendet wird.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: integer

```
</details></div>