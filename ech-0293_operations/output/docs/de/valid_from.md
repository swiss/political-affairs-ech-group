---
search:
  boost: 5.0
---

# Slot: valid_from 


_Das Datum, ab dem die Information gültig ist._




<div data-search-exclude markdown="1">



URI: [schema:validFrom](http://schema.org/validFrom)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [HasTemporalValidity](HasTemporalValidity.md) | Eine Mixin-Klasse, die Slots für die Modellierung einer zeitlichen Gültigkeit... |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Date](Date.md) |
| Domäne von | [HasTemporalValidity](HasTemporalValidity.md) |
| Slot-URI | [schema:validFrom](http://schema.org/validFrom) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: valid_from
annotations:
  description_de:
    tag: description_de
    value: 'Das Datum, ab dem die Information gültig ist.

      '
  description_fr:
    tag: description_fr
    value: 'La date à partir de laquelle l''information est valable.

      '
description: 'Das Datum, ab dem die Information gültig ist.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: schema:validFrom
domain_of:
- HasTemporalValidity
range: date

```
</details></div>