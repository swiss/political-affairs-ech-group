---
search:
  boost: 5.0
---

# Slot: country 


_[de] ISO 3166 Ländercode._

_[en] ISO 3166 country code._

__



<div data-search-exclude markdown="1">



URI: [act:country](https://ld.ech.ch/schema/0294/actors/country)
Alias: country

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Citizenship](Citizenship.md) | [de] Staatsangehörigkeit einer Person unter Angabe des Landes und der zeitlic... |  no  |






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












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:country |
| native | act:country |




## LinkML Source

<details>
```yaml
name: country
description: '[de] ISO 3166 Ländercode.

  [en] ISO 3166 country code.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:country
alias: country
domain_of:
- Citizenship
range: string
pattern: ^[A-Z]{2}$

```
</details></div>