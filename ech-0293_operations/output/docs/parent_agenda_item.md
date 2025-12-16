

# Slot: parent_agenda_item 


_[en] If needed, this slot builds a hierarchy of agenda items._

_[de] Wenn erforderlich, baut dieser Slot eine Hierarchie von Tagesordnungspunkten auf._

__





URI: [ops:parent_agenda_item](https://ch.paf.link/schema/operations/parent_agenda_item)
Alias: parent_agenda_item

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |
| [AgendaItem](AgendaItem.md) | [en] An agenda item of a meeting |  no  |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:parent_agenda_item |
| native | ops:parent_agenda_item |




## LinkML Source

<details>
```yaml
name: parent_agenda_item
description: '[en] If needed, this slot builds a hierarchy of agenda items.

  [de] Wenn erforderlich, baut dieser Slot eine Hierarchie von Tagesordnungspunkten
  auf.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: parent_agenda_item
domain_of:
- AgendaItem
- Voting
- Election
range: string

```
</details>