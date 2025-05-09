

# Slot: id 



URI: [chpaf:id](https://ch.paf.link/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Vote](Vote.md) |  |  no  |
| [Session](Session.md) |  |  no  |
| [AgendaItem](AgendaItem.md) |  |  no  |
| [Container](Container.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/session




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | chpaf:id |
| native | chpaf:id |




## LinkML Source

<details>
```yaml
name: id
from_schema: https://ch.paf.link/schema/session
rank: 1000
identifier: true
alias: id
domain_of:
- Session
- AgendaItem
- Vote
- Container
range: string
required: true

```
</details>