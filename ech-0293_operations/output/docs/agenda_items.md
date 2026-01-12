

# Slot: agenda_items 



URI: [ops:agendaItem](https://ch.paf.link/schema/operations/agendaItem)
Alias: agenda_items

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) |  |  no  |
| [JointDebate](JointDebate.md) | [en] Agenda Items which are debated together |  no  |






## Properties

* Range: [AgendaItem](AgendaItem.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:agendaItem |
| native | ops:agenda_items |




## LinkML Source

<details>
```yaml
name: agenda_items
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:agendaItem
alias: agenda_items
domain_of:
- Container
- JointDebate
range: AgendaItem
multivalued: true
inlined: true
inlined_as_list: true

```
</details>