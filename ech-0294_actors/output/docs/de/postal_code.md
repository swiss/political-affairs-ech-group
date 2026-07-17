---
search:
  boost: 5.0
---

# Slot: postal_code 


_Postleitzahl._

__



<div data-search-exclude markdown="1">



URI: [act:postalCode](https://ld.ech.ch/schema/0294/actors/postalCode)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Address](Address.md) | Eine Adresse mit einem Typ (z |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Integer](Integer.md) |
| Domäne von | [Address](Address.md) |
| Slot-URI | [act:postalCode](https://ld.ech.ch/schema/0294/actors/postalCode) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |












## LinkML-Quelle

<details>
```yaml
name: postal_code
annotations:
  description_de:
    tag: description_de
    value: 'Postleitzahl.

      '
  description_fr:
    tag: description_fr
    value: 'Code postal.

      '
description: 'Postleitzahl.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:postalCode
domain_of:
- Address
range: integer

```
</details></div>