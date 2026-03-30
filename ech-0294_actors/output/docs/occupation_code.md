

# Slot: occupation_code 


_[de] ISCO-19 Code der Tätigkeit._

_[en] ISCO-19 code of the occupation._

__





URI: [act:occupationCode](https://ld.ech.ch/schema/0294/actors/occupationCode)
Alias: occupation_code

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
| Slot URI | [act:occupationCode](https://ld.ech.ch/schema/0294/actors/occupationCode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:occupationCode |
| native | act:occupation_code |




## LinkML Source

<details>
```yaml
name: occupation_code
description: '[de] ISCO-19 Code der Tätigkeit.

  [en] ISCO-19 code of the occupation.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:occupationCode
alias: occupation_code
domain_of:
- Occupation
range: string

```
</details>