

# Slot: citizenships 



URI: [act:citizenship](https://ch.paf.link/schema/actors/citizenship)
Alias: citizenships

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | [en] A person with identifiers, names, addresses, citizenships, and occupatio... |  no  |






## Properties

* Range: [Citizenship](Citizenship.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:citizenship |
| native | act:citizenships |




## LinkML Source

<details>
```yaml
name: citizenships
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: act:citizenship
alias: citizenships
domain_of:
- Person
range: Citizenship
multivalued: true
inlined: true
inlined_as_list: true

```
</details>