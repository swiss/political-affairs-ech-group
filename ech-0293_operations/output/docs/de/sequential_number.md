---
search:
  boost: 5.0
---

# Slot: sequential_number 


_Laufende Nummer der Sitzung, die zur Sortierung verwendet wird._




<div data-search-exclude markdown="1">



URI: [ops:sequential_number](https://ch.paf.link/schema/operations/sequential_number)
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
    value: 'Laufende Nummer der Sitzung, die zur Sortierung verwendet wird.

      '
  description_fr:
    tag: description_fr
    value: 'Numéro séquentiel de la séance, utilisé pour le tri.

      '
description: 'Laufende Nummer der Sitzung, die zur Sortierung verwendet wird.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Session
- Meeting
range: integer

```
</details></div>