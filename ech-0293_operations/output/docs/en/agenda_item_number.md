---
search:
  boost: 5.0
---

# Slot: agenda_item_number 


_Sequential number of the agenda item (string type to support roman numerals)._




<div data-search-exclude markdown="1">



URI: [ops:agenda_item_number](https://ch.paf.link/schema/operations/agenda_item_number)
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
name: agenda_item_number
annotations:
  description_de:
    tag: description_de
    value: 'Laufnummer des Traktandums (String-Typ zur Unterstützung römischer Ziffern).

      '
  description_fr:
    tag: description_fr
    value: 'Numéro d''ordre du point de l''ordre du jour (type chaîne, afin de permettre
      les chiffres romains).

      '
description: 'Sequential number of the agenda item (string type to support roman numerals).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- AgendaItem
range: string

```
</details></div>