---
search:
  boost: 5.0
---

# Slot: seat_nr 


_Die Sitznummer der Einzelstimme, falls zutreffend._




<div data-search-exclude markdown="1">



URI: [ops:seat_nr](https://ch.paf.link/schema/operations/seat_nr)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [IndividualVote](IndividualVote.md) | Eine Einzelstimme eines Mitglieds während eines Abstimmungsverfahrens |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [IndividualVote](IndividualVote.md) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: seat_nr
annotations:
  description_de:
    tag: description_de
    value: 'Die Sitznummer der Einzelstimme, falls zutreffend.

      '
  description_fr:
    tag: description_fr
    value: 'Le numéro de siège correspondant à la voix individuelle, le cas échéant.

      '
description: 'Die Sitznummer der Einzelstimme, falls zutreffend.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IndividualVote
range: string

```
</details></div>