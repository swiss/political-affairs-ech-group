

# Slot: id 



URI: [tutorial:id](https://ch.paf.link/schema/tutorial/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Vote](Vote.md) |  |  no  |
| [Container](Container.md) |  |  no  |
| [AgendaItem](AgendaItem.md) |  |  no  |
| [Session](Session.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/tutorial




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tutorial:id |
| native | tutorial:id |




## LinkML Source

<details>
```yaml
name: id
from_schema: https://ch.paf.link/schema/tutorial
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