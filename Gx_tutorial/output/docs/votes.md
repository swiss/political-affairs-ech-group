

# Slot: votes 



URI: [chpaf:vote](https://ch.paf.link/vote)
Alias: votes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AgendaItem](AgendaItem.md) |  |  no  |







## Properties

* Range: [Vote](Vote.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/session




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | chpaf:vote |
| native | chpaf:votes |




## LinkML Source

<details>
```yaml
name: votes
from_schema: https://ch.paf.link/schema/session
rank: 1000
slot_uri: chpaf:vote
alias: votes
domain_of:
- AgendaItem
range: Vote
multivalued: true
inlined: true
inlined_as_list: true

```
</details>