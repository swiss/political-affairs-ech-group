---
search:
  boost: 5.0
---

# Slot: parent_agenda_item 


_If needed, this slot builds a hierarchy of agenda items._




<div data-search-exclude markdown="1">



URI: [ops:parent_agenda_item](https://ch.paf.link/schema/operations/parent_agenda_item)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AgendaItem](AgendaItem.md) | An agenda item of a meeting |  no  |
| [Voting](Voting.md) | A voting procedure with individual votes and results |  no  |
| [Election](Election.md) | An election procedure for selecting persons to positions |  no  |
| [ProtocolItem](ProtocolItem.md) | An agenda item as actually recorded in the protocol |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AgendaItem](AgendaItem.md), [Voting](Voting.md), [Election](Election.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: parent_agenda_item
annotations:
  description_de:
    tag: description_de
    value: 'Wenn erforderlich, baut dieser Slot eine Hierarchie von Traktanden auf.

      '
  description_fr:
    tag: description_fr
    value: 'Au besoin, ce slot permet de construire une hiérarchie de points de l''ordre
      du jour.

      '
description: 'If needed, this slot builds a hierarchy of agenda items.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
- Voting
- Election
range: string

```
</details></div>