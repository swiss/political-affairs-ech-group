---
search:
  boost: 5.0
---

# Slot: affair_id 


_The connection to the affairs (business items) of the agenda item._




<div data-search-exclude markdown="1">



URI: [ops:affair_id](https://ch.paf.link/schema/operations/affair_id)
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
name: affair_id
annotations:
  description_de:
    tag: description_de
    value: 'Die Verbindung zu den Geschäften des Traktandums.

      '
  description_fr:
    tag: description_fr
    value: 'Le lien vers les affaires rattachées au point de l''ordre du jour.

      '
description: 'The connection to the affairs (business items) of the agenda item.

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