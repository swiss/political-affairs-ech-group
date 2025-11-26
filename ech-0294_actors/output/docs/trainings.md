

# Slot: trainings 



URI: [act:training](https://ch.paf.link/schema/actors/training)
Alias: trainings

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |






## Properties

* Range: [Training](Training.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:training |
| native | act:trainings |




## LinkML Source

<details>
```yaml
name: trainings
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: act:training
alias: trainings
owner: Person
domain_of:
- Person
range: Training
multivalued: true
inlined: true
inlined_as_list: true

```
</details>