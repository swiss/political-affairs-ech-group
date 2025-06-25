

# Slot: agenda_items 



URI: [tutorial:agendaItem](https://ch.paf.link/schema/tutorial/agendaItem)
Alias: agenda_items

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Session](Session.md) |  |  no  |
| [Container](Container.md) |  |  no  |







## Properties

* Range: [AgendaItem](AgendaItem.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/tutorial




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tutorial:agendaItem |
| native | tutorial:agenda_items |




## LinkML Source

<details>
```yaml
name: agenda_items
from_schema: https://ch.paf.link/schema/tutorial
rank: 1000
slot_uri: tutorial:agendaItem
alias: agenda_items
domain_of:
- Session
- Container
range: AgendaItem
multivalued: true
inlined: true
inlined_as_list: true

```
</details>