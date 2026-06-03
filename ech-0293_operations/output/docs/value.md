---
search:
  boost: 5.0
---

# Slot: value 


_The value of an information besides other attributes such as type, language, etc._

__



<div data-search-exclude markdown="1">



URI: [mcm:value](https://ld.ech.ch/schema/0292/meta-common/value)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MultilingualValue](MultilingualValue.md) | A multilingual string with language specification |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MultilingualValue](MultilingualValue.md) |
| Slot URI | [mcm:value](https://ld.ech.ch/schema/0292/meta-common/value) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| description_de | Der eigentliche Wert einer Information neben weiteren attributen wie Typ, Sprache, etc.
 |




### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:value |
| native | ops:value |




## LinkML Source

<details>
```yaml
name: value
annotations:
  description_de:
    tag: description_de
    value: 'Der eigentliche Wert einer Information neben weiteren attributen wie Typ,
      Sprache, etc.

      '
description: 'The value of an information besides other attributes such as type, language,
  etc.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:value
domain_of:
- MultilingualValue
range: string

```
</details></div>