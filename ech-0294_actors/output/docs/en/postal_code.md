---
search:
  boost: 5.0
---

# Slot: postal_code 


_Postal code._

__



<div data-search-exclude markdown="1">



URI: [act:postalCode](https://ld.ech.ch/schema/0294/actors/postalCode)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Address](Address.md) | An address with a type (e |  no  |






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












## LinkML Source

<details>
```yaml
name: postal_code
annotations:
  description_de:
    tag: description_de
    value: 'Postleitzahl.

      '
description: 'Postal code.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:postalCode
domain_of:
- Address
range: integer

```
</details></div>