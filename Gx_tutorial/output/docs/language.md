

# Slot: language 


_[en] Language code in ISO 639-1 format [de] Sprachcode im ISO 639-1-Format_

__





URI: [dcterm:language](http://purl.org/dc/terms/language)
Alias: language

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MultilingualString](MultilingualString.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Required: True

* Regex pattern: `^[a-z]{2}$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/tutorial




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterm:language |
| native | tutorial:language |




## LinkML Source

<details>
```yaml
name: language
description: '[en] Language code in ISO 639-1 format [de] Sprachcode im ISO 639-1-Format

  '
from_schema: https://ch.paf.link/schema/tutorial
rank: 1000
slot_uri: dcterm:language
alias: language
domain_of:
- MultilingualString
range: string
required: true
pattern: ^[a-z]{2}$

```
</details>