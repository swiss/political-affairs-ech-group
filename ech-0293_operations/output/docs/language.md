

# Slot: language 


_Language code in ISO 639-1 format_





URI: [ops:language](https://ch.paf.link/schema/operations/language)
Alias: language

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MultilingualString](MultilingualString.md) | [en] A string that can contain text in multiple languages |  no  |
| [Speech](Speech.md) | [en] A speech or statement made during a meeting (also called Votum or speake... |  no  |






## Properties

* Range: [String](String.md)

* Required: True

* Regex pattern: `^[a-z]{2}$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:language |
| native | ops:language |




## LinkML Source

<details>
```yaml
name: language
description: Language code in ISO 639-1 format
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: language
domain_of:
- Speech
- MultilingualString
range: string
required: true
pattern: ^[a-z]{2}$

```
</details>