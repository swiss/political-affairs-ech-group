---
search:
  boost: 5.0
---

# Slot: postal_locality 


_Ort._

__



<div data-search-exclude markdown="1">



URI: [act:postalLocality](https://ld.ech.ch/schema/0294/actors/postalLocality)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Address](Address.md) | Eine Adresse mit einem Typ (z |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [String](String.md) |
| Domäne von | [Address](Address.md) |
| Slot-URI | [act:postalLocality](https://ld.ech.ch/schema/0294/actors/postalLocality) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| Basel-Stadt |





## LinkML-Quelle

<details>
```yaml
name: postal_locality
annotations:
  description_de:
    tag: description_de
    value: 'Ort.

      '
  description_fr:
    tag: description_fr
    value: 'Localité.

      '
description: 'Ort.

  '
examples:
- value: Basel-Stadt
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:postalLocality
domain_of:
- Address
range: string

```
</details></div>