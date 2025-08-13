

# Slot: language 


_Language code in ISO 639-1 format_





URI: [act:language](https://ch.paf.link/schema/actors/language)
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
description: Language code in ISO 639-1 format
from_schema: https://ch.paf.link/schema/actors
rank: 1000
alias: language
domain_of:
- MultilingualString
range: string
required: true
pattern: ^[a-z]{2}$

```
</details>