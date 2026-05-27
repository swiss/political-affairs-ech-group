---
search:
  boost: 5.0
---

# Slot: address_type 


_[de] Typ der Adresse._

_[en] Type of address._

__



<div data-search-exclude markdown="1">



URI: [act:addressType](https://ld.ech.ch/schema/0294/actors/addressType)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Address](Address.md) | [de] Eine Adresse mit einem Typ (z |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AddressTypeEnum](AddressTypeEnum.md) |
| Domain Of | [Address](Address.md) |
| Slot URI | [act:addressType](https://ld.ech.ch/schema/0294/actors/addressType) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| businessAddress |
| privateAddress |





## LinkML Source

<details>
```yaml
name: address_type
description: '[de] Typ der Adresse.

  [en] Type of address.

  '
examples:
- value: businessAddress
- value: privateAddress
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:addressType
domain_of:
- Address
range: AddressTypeEnum

```
</details></div>