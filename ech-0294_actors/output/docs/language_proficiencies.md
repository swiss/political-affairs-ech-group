

# Slot: language_proficiencies 


_[de] Sprachkompetenzen der Person._

_[en] Language proficiencies of the person._

__





URI: [act:languageProficiency](https://ld.ech.ch/schema/0294/actors/languageProficiency)
Alias: language_proficiencies

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | [de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften u... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LanguageProficiency](LanguageProficiency.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [act:languageProficiency](https://ld.ech.ch/schema/0294/actors/languageProficiency) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:languageProficiency |
| native | act:language_proficiencies |




## LinkML Source

<details>
```yaml
name: language_proficiencies
description: '[de] Sprachkompetenzen der Person.

  [en] Language proficiencies of the person.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:languageProficiency
alias: language_proficiencies
domain_of:
- Person
range: LanguageProficiency
multivalued: true
inlined: true
inlined_as_list: true

```
</details>