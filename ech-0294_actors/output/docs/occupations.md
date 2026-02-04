

# Slot: occupations 



URI: [act:occupation](https://ch.paf.link/schema/actors/occupation)
Alias: occupations

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | [en] A person with identifiers, names, addresses, citizenships, and occupatio... |  no  |






## Properties

* Range: [Occupation](Occupation.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:occupation |
| native | act:occupations |




## LinkML Source

<details>
```yaml
name: occupations
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: act:occupation
alias: occupations
domain_of:
- Person
range: Occupation
multivalued: true
inlined: true
inlined_as_list: true

```
</details>