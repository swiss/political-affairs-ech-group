

# Slot: votings 


_Collection of voting records_





URI: [ops:voting](https://ch.paf.link/schema/operations/voting)
Alias: votings

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) |  |  no  |






## Properties

* Range: [Voting](Voting.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:voting |
| native | ops:votings |




## LinkML Source

<details>
```yaml
name: votings
description: Collection of voting records
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:voting
alias: votings
domain_of:
- Container
range: Voting
multivalued: true
inlined: true
inlined_as_list: true

```
</details>