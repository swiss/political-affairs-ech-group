

# Slot: addresses 


_place of residence and work_





URI: [act:address](https://ch.paf.link/schema/actors/address)
Alias: addresses

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |






## Properties

* Range: [Address](Address.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:address |
| native | act:addresses |




## LinkML Source

<details>
```yaml
name: addresses
description: place of residence and work
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: act:address
alias: addresses
owner: Person
domain_of:
- Person
range: Address
multivalued: true
inlined: true
inlined_as_list: true

```
</details>