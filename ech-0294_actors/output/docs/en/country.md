---
search:
  boost: 5.0
---

# Slot: country 


_ISO 3166-1 alpha-2 country code._

__



<div data-search-exclude markdown="1">



URI: [act:country](https://ld.ech.ch/schema/0294/actors/country)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Citizenship](Citizenship.md) | Citizenship (also used for Nationality) of a person indicating the country an... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Citizenship](Citizenship.md) |
| Slot URI | [act:country](https://ld.ech.ch/schema/0294/actors/country) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[A-Z]{2}$` |











## Examples

| Value |
| --- |
| CH |





## LinkML Source

<details>
```yaml
name: country
annotations:
  description_de:
    tag: description_de
    value: 'ISO 3166-1 alpha-2 Ländercode.

      '
  description_fr:
    tag: description_fr
    value: 'Code de pays ISO 3166-1 alpha-2.

      '
description: 'ISO 3166-1 alpha-2 country code.

  '
examples:
- value: CH
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:country
domain_of:
- Citizenship
range: string
pattern: ^[A-Z]{2}$

```
</details></div>