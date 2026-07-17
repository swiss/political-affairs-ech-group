---
search:
  boost: 5.0
---

# Slot: postal_locality 


_Locality._

__



<div data-search-exclude markdown="1">



URI: [act:postalLocality](https://ld.ech.ch/schema/0294/actors/postalLocality)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Address](Address.md) | An address with a type (e |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Address](Address.md) |
| Slot URI | [act:postalLocality](https://ld.ech.ch/schema/0294/actors/postalLocality) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| Basel-Stadt |





## LinkML Source

<details>
```yaml
name: postal_locality
annotations:
  description_de:
    tag: description_de
    value: 'Ort.

      '
description: 'Locality.

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