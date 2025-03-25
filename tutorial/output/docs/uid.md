

# Slot: uid



URI: [chpaf:uid](https://ch.paf.link/uid)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AgendaItem](AgendaItem.md) |  |  no  |
| [Session](Session.md) |  |  no  |
| [Vote](Vote.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/session




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | chpaf:uid |
| native | chpaf:uid |




## LinkML Source

<details>
```yaml
name: uid
from_schema: https://ch.paf.link/schema/session
rank: 1000
identifier: true
alias: uid
domain_of:
- Session
- AgendaItem
- Vote
range: string
required: true

```
</details>