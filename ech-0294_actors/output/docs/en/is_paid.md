---
search:
  boost: 5.0
---

# Slot: is_paid 


_Indicates if the position is paid._

__



<div data-search-exclude markdown="1">



URI: [act:isPaid](https://ld.ech.ch/schema/0294/actors/isPaid)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |
| [Occupation](Occupation.md) | Occupation or profession of a person indicating a label, an ISCO-19 code, whe... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [InterestLink](InterestLink.md), [Occupation](Occupation.md) |
| Slot URI | [act:isPaid](https://ld.ech.ch/schema/0294/actors/isPaid) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| False |
| True |





## LinkML Source

<details>
```yaml
name: is_paid
annotations:
  description_de:
    tag: description_de
    value: 'Gibt an, ob die Position bezahlt ist.

      '
  description_fr:
    tag: description_fr
    value: 'Indique si le poste est rémunéré.

      '
description: 'Indicates if the position is paid.

  '
examples:
- value: 'False'
- value: 'True'
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:isPaid
domain_of:
- InterestLink
- Occupation
range: boolean

```
</details></div>