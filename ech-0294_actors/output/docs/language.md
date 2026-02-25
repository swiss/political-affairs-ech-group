

# Slot: language 


_[en] Language code in ISO 639-1 format._

_[de] Sprachcode im ISO 639-1 Format._

__





URI: [act:language](https://ch.paf.link/schema/actors/language)
Alias: language

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LanguageProficiency](LanguageProficiency.md) |  |  no  |
| [MultilingualString](MultilingualString.md) | [en] A string that can contain text in multiple languages |  no  |






## Properties

* Range: [String](String.md)

* Required: True

* Regex pattern: `^[a-z]{2}$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:language |
| native | act:language |




## LinkML Source

<details>
```yaml
name: language
description: '[en] Language code in ISO 639-1 format.

  [de] Sprachcode im ISO 639-1 Format.

  '
from_schema: https://ch.paf.link/schema/actors
rank: 1000
alias: language
domain_of:
- LanguageProficiency
- MultilingualString
range: string
required: true
pattern: ^[a-z]{2}$

```
</details>