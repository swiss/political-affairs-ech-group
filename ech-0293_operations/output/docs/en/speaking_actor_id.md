---
search:
  boost: 5.0
---

# Slot: speaking_actor_id 


_The speaker or head of the department for the agenda item._




<div data-search-exclude markdown="1">



URI: [ops:speaking_actor_id](https://ch.paf.link/schema/operations/speaking_actor_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AgendaItem](AgendaItem.md) | An agenda item of a meeting |  no  |
| [ProtocolItem](ProtocolItem.md) | An agenda item as actually recorded in the protocol |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AgendaItem](AgendaItem.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: speaking_actor_id
annotations:
  description_de:
    tag: description_de
    value: 'Der Sprecher oder die Sprecherin bzw. die Departementsvorsteherin oder
      der Departementsvorsteher für das Traktandum.

      '
  description_fr:
    tag: description_fr
    value: 'La ou le porte-parole ou la cheffe ou le chef du département pour le point
      de l''ordre du jour.

      '
description: 'The speaker or head of the department for the agenda item.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: string

```
</details></div>