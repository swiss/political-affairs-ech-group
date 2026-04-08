---
search:
  boost: 5.0
---

# Slot: enterprise 


_[de] Name des Unternehmens._

_[en] Name of the enterprise._

__



<div data-search-exclude markdown="1">



URI: [act:enterprise](https://ld.ech.ch/schema/0294/actors/enterprise)
Alias: enterprise

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Occupation](Occupation.md) | [de] Beruf oder Tätigkeit einer Person mit Angabe eines Labels, eines ISCO-19... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Occupation](Occupation.md) |
| Slot URI | [act:enterprise](https://ld.ech.ch/schema/0294/actors/enterprise) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:enterprise |
| native | act:enterprise |




## LinkML Source

<details>
```yaml
name: enterprise
description: '[de] Name des Unternehmens.

  [en] Name of the enterprise.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:enterprise
alias: enterprise
domain_of:
- Occupation
range: string

```
</details></div>