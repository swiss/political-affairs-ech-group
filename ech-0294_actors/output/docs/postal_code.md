

# Slot: postal_code 


_[de] Postleitzahl._

_[en] Postal code._

__





URI: [act:postalCode](https://ld.ech.ch/schema/0294/actors/postalCode)
Alias: postal_code

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Address](Address.md) | [de] Eine Adresse mit einem Typ (z |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Address](Address.md) |
| Slot URI | [act:postalCode](https://ld.ech.ch/schema/0294/actors/postalCode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:postalCode |
| native | act:postal_code |




## LinkML Source

<details>
```yaml
name: postal_code
description: '[de] Postleitzahl.

  [en] Postal code.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:postalCode
alias: postal_code
domain_of:
- Address
range: integer

```
</details>