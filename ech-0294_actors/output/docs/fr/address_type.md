---
search:
  boost: 5.0
---

# Slot: address_type 


_Type d'adresse._

__



<div data-search-exclude markdown="1">



URI: [act:addressType](https://ld.ech.ch/schema/0294/actors/addressType)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Address](Address.md) | Une adresse avec un type (p |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [AddressTypeEnum](AddressTypeEnum.md) |
| Domaine de | [Address](Address.md) |
| URI du slot | [act:addressType](https://ld.ech.ch/schema/0294/actors/addressType) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |









## Exemples

| Valeur |
| --- |
| businessAddress |





## Source LinkML

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
description: 'Type d''adresse.

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