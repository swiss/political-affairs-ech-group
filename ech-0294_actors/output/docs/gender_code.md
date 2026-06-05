---
search:
  boost: 5.0
---

# Slot: gender_code 


_Gender code. Recommended values: male, female, diverse._

__



<div data-search-exclude markdown="1">



URI: [act:genderCode](https://ld.ech.ch/schema/0294/actors/genderCode)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Gender](Gender.md) | Gender of a person indicating a gender code and temporal validity |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GenderCodeEnum](GenderCodeEnum.md) |
| Domain Of | [Gender](Gender.md) |
| Slot URI | [act:genderCode](https://ld.ech.ch/schema/0294/actors/genderCode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: gender_code
annotations:
  description_de:
    tag: description_de
    value: 'Geschlechtscode. Empfohlene Werte: male, female, diverse .

      '
description: 'Gender code. Recommended values: male, female, diverse.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:genderCode
domain_of:
- Gender
range: GenderCodeEnum

```
</details></div>