

# Slot: votes 



URI: [tutorial:vote](https://ch.paf.link/schema/tutorial/vote)
Alias: votes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) |  |  no  |
| [AgendaItem](AgendaItem.md) |  |  no  |







## Properties

* Range: [Vote](Vote.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/tutorial




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tutorial:vote |
| native | tutorial:votes |




## LinkML Source

<details>
```yaml
name: votes
from_schema: https://ch.paf.link/schema/tutorial
rank: 1000
slot_uri: tutorial:vote
alias: votes
domain_of:
- AgendaItem
- Container
range: Vote
multivalued: true
inlined: true
inlined_as_list: true

```
</details>