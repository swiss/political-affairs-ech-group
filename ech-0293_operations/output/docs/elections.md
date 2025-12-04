

# Slot: elections 


_Collection of election records_





URI: [ops:election](https://ch.paf.link/schema/operations/election)
Alias: elections

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) |  |  no  |






## Properties

* Range: [Election](Election.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:election |
| native | ops:elections |




## LinkML Source

<details>
```yaml
name: elections
description: Collection of election records
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:election
alias: elections
domain_of:
- Container
range: Election
multivalued: true
inlined: true
inlined_as_list: true

```
</details>