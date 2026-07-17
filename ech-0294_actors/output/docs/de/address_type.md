---
search:
  boost: 5.0
---

# Slot: address_type 


_Typ der Adresse._

__



<div data-search-exclude markdown="1">



URI: [act:addressType](https://ld.ech.ch/schema/0294/actors/addressType)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Address](Address.md) | Eine Adresse mit einem Typ (z |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [AddressTypeEnum](AddressTypeEnum.md) |
| Domäne von | [Address](Address.md) |
| Slot-URI | [act:addressType](https://ld.ech.ch/schema/0294/actors/addressType) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| businessAddress |





## LinkML-Quelle

<details>
```yaml
name: address_type
annotations:
  description_de:
    tag: description_de
    value: 'Typ der Adresse.

      '
  description_fr:
    tag: description_fr
    value: 'Type d''adresse.

      '
description: 'Typ der Adresse.

  '
examples:
- value: businessAddress
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:addressType
domain_of:
- Address
range: AddressTypeEnum

```
</details></div>