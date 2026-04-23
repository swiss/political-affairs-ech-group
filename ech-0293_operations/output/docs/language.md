

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
| [Speech](Speech.md) | [en] A speech or statement made during a meeting (also called Votum or speake... |  no  |
| [MultilingualValue](MultilingualValue.md) | [de] Ein mehrsprachiger String mit Angabe der Sprache |  no  |
| [MultilingualString](MultilingualString.md) | [en] A string that can contain text in multiple languages |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Speech](Speech.md), [MultilingualString](MultilingualString.md), [MultilingualValue](MultilingualValue.md) |
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


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:language |
| native | ops:language |




## LinkML Source

<details>
```yaml
name: language
description: '[de] Sprachcode im ISO 639-1 Format.

  [en] Language code in ISO 639-1 format.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:language
alias: language
domain_of:
- Speech
- MultilingualString
- MultilingualValue
range: string
pattern: ^[a-z]{2}$

```
</details>