

# Slot: country 


_ISO 3166 country code (can't be CH)_





URI: [act:country](https://ch.paf.link/schema/actors/country)
Alias: country

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Citizenship](Citizenship.md) |  |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:country |
| native | act:country |




## LinkML Source

<details>
```yaml
name: country
description: ISO 3166 country code (can't be CH)
from_schema: https://ch.paf.link/schema/actors
rank: 1000
alias: country
owner: Citizenship
domain_of:
- Citizenship
range: string
required: true

```
</details>