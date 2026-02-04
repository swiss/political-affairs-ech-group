

# Slot: names 



URI: [act:name](https://ch.paf.link/schema/actors/name)
Alias: names

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | [en] A person with identifiers, names, addresses, citizenships, and occupatio... |  no  |






## Properties

* Range: [Name](Name.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:name |
| native | act:names |




## LinkML Source

<details>
```yaml
name: names
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: act:name
alias: names
domain_of:
- Person
range: Name
multivalued: true
inlined: true
inlined_as_list: true

```
</details>