

# Slot: language 


_[de] Sprachcode im ISO 639-1 Format._

_[en] Language code in ISO 639-1 format._

__





URI: [mcm:language](https://ld.ech.ch/schema/0292/meta-common/language)
Alias: language

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MultilingualValue](MultilingualValue.md) | [de] Ein mehrsprachiger String mit Angabe der Sprache |  no  |
| [LanguageProficiency](LanguageProficiency.md) | [de] Sprachkenntnisse einer Person mit Angabe der Sprache und ob es sich um d... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [LanguageProficiency](LanguageProficiency.md), [MultilingualValue](MultilingualValue.md) |
| Slot URI | [mcm:language](https://ld.ech.ch/schema/0292/meta-common/language) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[a-z]{2}$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:language |
| native | act:language |




## LinkML Source

<details>
```yaml
name: language
description: '[de] Sprachcode im ISO 639-1 Format.

  [en] Language code in ISO 639-1 format.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:language
alias: language
domain_of:
- LanguageProficiency
- MultilingualValue
range: string
pattern: ^[a-z]{2}$

```
</details>