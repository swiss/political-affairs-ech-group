

# Slot: individual_votes 


_Collection of individual vote records_





URI: [ops:individualVote](https://ch.paf.link/schema/operations/individualVote)
Alias: individual_votes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) |  |  no  |






## Properties

* Range: [IndividualVote](IndividualVote.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:individualVote |
| native | ops:individual_votes |




## LinkML Source

<details>
```yaml
name: individual_votes
description: Collection of individual vote records
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:individualVote
alias: individual_votes
domain_of:
- Container
range: IndividualVote
multivalued: true
inlined: true
inlined_as_list: true

```
</details>