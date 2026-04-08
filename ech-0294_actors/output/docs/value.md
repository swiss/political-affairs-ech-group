---
search:
  boost: 5.0
---

# Slot: value 


_[de] Der eigentliche Wert einer Information neben weiteren attributen wie Typ, Sprache, etc._

_[en] The value of an information besides other attributes such as type, language, etc._

__



<div data-search-exclude markdown="1">



URI: [mcm:value](https://ld.ech.ch/schema/0292/meta-common/value)
Alias: value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Contact](Contact.md) | [de] Kontaktinformation einer Person mit Angabe eines Typs (z |  no  |
| [Training](Training.md) | [de] Ausbildung oder Bildung einer Person mit Angabe eines Typs (z |  no  |
| [Name](Name.md) | [de] Ein Name mit einem Typ (z |  no  |
| [MultilingualValue](MultilingualValue.md) | [de] Ein mehrsprachiger String mit Angabe der Sprache |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Name](Name.md), [Training](Training.md), [Contact](Contact.md), [MultilingualValue](MultilingualValue.md) |
| Slot URI | [mcm:value](https://ld.ech.ch/schema/0292/meta-common/value) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:value |
| native | act:value |




## LinkML Source

<details>
```yaml
name: value
description: '[de] Der eigentliche Wert einer Information neben weiteren attributen
  wie Typ, Sprache, etc.

  [en] The value of an information besides other attributes such as type, language,
  etc.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:value
alias: value
domain_of:
- Name
- Training
- Contact
- MultilingualValue
range: string

```
</details></div>