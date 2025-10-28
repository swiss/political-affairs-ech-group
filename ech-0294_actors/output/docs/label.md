

# Slot: label 


_Display name of the person_





URI: [act:label](https://ch.paf.link/schema/actors/label)
Alias: label

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:label |
| native | act:label |




## LinkML Source

<details>
```yaml
name: label
description: Display name of the person
from_schema: https://ch.paf.link/schema/actors
rank: 1000
alias: label
owner: Person
domain_of:
- Person
range: string
required: true

```
</details>