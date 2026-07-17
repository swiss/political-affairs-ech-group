---
search:
  boost: 5.0
---

# Slot: occupation_code 


_ISCO-19 code of the occupation._

__



<div data-search-exclude markdown="1">



URI: [act:occupationCode](https://ld.ech.ch/schema/0294/actors/occupationCode)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Occupation](Occupation.md) | Occupation or profession of a person indicating a label, an ISCO-19 code, whe... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Occupation](Occupation.md) |
| Slot URI | [act:occupationCode](https://ld.ech.ch/schema/0294/actors/occupationCode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: occupation_code
annotations:
  description_de:
    tag: description_de
    value: 'ISCO-19 Code der Tätigkeit.

      '
description: 'ISCO-19 code of the occupation.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:occupationCode
domain_of:
- Occupation
range: string

```
</details></div>