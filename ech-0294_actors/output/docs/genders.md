

# Slot: genders 



URI: [act:gender](https://ch.paf.link/schema/actors/gender)
Alias: genders

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | [en] A person with identifiers, names, addresses, citizenships, and occupatio... |  no  |






## Properties

* Range: [Gender](Gender.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:gender |
| native | act:genders |




## LinkML Source

<details>
```yaml
name: genders
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: act:gender
alias: genders
domain_of:
- Person
range: Gender
multivalued: true
inlined: true
inlined_as_list: true

```
</details>