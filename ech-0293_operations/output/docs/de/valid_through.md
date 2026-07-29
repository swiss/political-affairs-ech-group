---
search:
  boost: 5.0
---

# Slot: valid_through 


_Das Datum, bis und mit dem die Information gültig ist._




<div data-search-exclude markdown="1">



URI: [schema:validThrough](http://schema.org/validThrough)
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
| Slot-URI | [schema:validThrough](http://schema.org/validThrough) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: valid_through
annotations:
  description_de:
    tag: description_de
    value: 'Das Datum, bis und mit dem die Information gültig ist.

      '
  description_fr:
    tag: description_fr
    value: 'La date jusqu''à laquelle l''information est valable, incluse.

      '
description: 'Das Datum, bis und mit dem die Information gültig ist.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: schema:validThrough
domain_of:
- HasTemporalValidity
range: date

```
</details></div>