---
search:
  boost: 5.0
---

# Slot: gender_code 


_[de] Geschlechtscode (z.B. gemäß ISO 5218)._

_[en] Gender code (e.g., according to ISO 5218)._

__



<div data-search-exclude markdown="1">



URI: [act:genderCode](https://ld.ech.ch/schema/0294/actors/genderCode)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Gender](Gender.md) | [de] Geschlecht einer Person mit Angabe eines Geschlechtscodes und der zeitli... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Gender](Gender.md) |
| Slot URI | [act:genderCode](https://ld.ech.ch/schema/0294/actors/genderCode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| male |





## LinkML Source

<details>
```yaml
name: gender_code
description: '[de] Geschlechtscode (z.B. gemäß ISO 5218).

  [en] Gender code (e.g., according to ISO 5218).

  '
examples:
- value: male
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:genderCode
domain_of:
- Gender
range: string

```
</details></div>