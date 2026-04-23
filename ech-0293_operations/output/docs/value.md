

# Slot: value 


_[de] Der eigentliche Wert einer Information neben weiteren attributen wie Typ, Sprache, etc._

_[en] The value of an information besides other attributes such as type, language, etc._

__





URI: [mcm:value](https://ld.ech.ch/schema/0292/meta-common/value)
Alias: value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MultilingualValue](MultilingualValue.md) | [de] Ein mehrsprachiger String mit Angabe der Sprache |  no  |






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
description: '[de] Der eigentliche Wert einer Information neben weiteren attributen
  wie Typ, Sprache, etc.

  [en] The value of an information besides other attributes such as type, language,
  etc.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:value
alias: value
domain_of:
- MultilingualValue
range: string

```
</details>