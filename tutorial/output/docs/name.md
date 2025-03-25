

# Slot: name



URI: [dcterm:title](http://purl.org/dc/terms/title)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AgendaItem](AgendaItem.md) |  |  no  |
| [Session](Session.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/session




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterm:title |
| native | chpaf:name |




## LinkML Source

<details>
```yaml
name: name
from_schema: https://ch.paf.link/schema/session
rank: 1000
slot_uri: dcterm:title
alias: name
domain_of:
- Session
- AgendaItem
range: string
required: true

```
</details>