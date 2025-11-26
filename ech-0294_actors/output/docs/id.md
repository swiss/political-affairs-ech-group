

# Slot: id 


_Wikidata-ID preferred_





URI: [act:id](https://ch.paf.link/schema/actors/id)
Alias: id

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
| self | act:id |
| native | act:id |




## LinkML Source

<details>
```yaml
name: id
description: Wikidata-ID preferred
from_schema: https://ch.paf.link/schema/actors
rank: 1000
identifier: true
alias: id
owner: Person
domain_of:
- Person
range: string
required: true

```
</details>