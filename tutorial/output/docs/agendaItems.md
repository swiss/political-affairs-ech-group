

# Slot: agendaItems 



URI: [chpaf:agendaItem](https://ch.paf.link/agendaItem)
Alias: agendaItems

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Session](Session.md) |  |  no  |







## Properties

* Range: [AgendaItem](AgendaItem.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/session




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | chpaf:agendaItem |
| native | chpaf:agendaItems |




## LinkML Source

<details>
```yaml
name: agendaItems
from_schema: https://ch.paf.link/schema/session
rank: 1000
slot_uri: chpaf:agendaItem
alias: agendaItems
domain_of:
- Session
range: AgendaItem
multivalued: true
inlined: true
inlined_as_list: true

```
</details>