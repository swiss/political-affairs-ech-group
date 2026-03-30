

# Slot: is_native 


_[de] Gibt an, ob es sich um die Muttersprache handelt._

_[en] Indicates if this is the native language._

__





URI: [act:isNative](https://ld.ech.ch/schema/0294/actors/isNative)
Alias: is_native

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LanguageProficiency](LanguageProficiency.md) | [de] Sprachkenntnisse einer Person mit Angabe der Sprache und ob es sich um d... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [LanguageProficiency](LanguageProficiency.md) |
| Slot URI | [act:isNative](https://ld.ech.ch/schema/0294/actors/isNative) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:isNative |
| native | act:is_native |




## LinkML Source

<details>
```yaml
name: is_native
description: '[de] Gibt an, ob es sich um die Muttersprache handelt.

  [en] Indicates if this is the native language.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:isNative
alias: is_native
domain_of:
- LanguageProficiency
range: boolean

```
</details>