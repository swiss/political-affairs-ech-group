---
search:
  boost: 5.0
---

# Slot: agenda_item_number 


_Number of the agenda item on the agenda, e.g. "2.1" or "3" (string type to also support roman numerals)._




<div data-search-exclude markdown="1">



URI: [ops:agenda_item_number](https://ch.paf.link/schema/operations/agenda_item_number)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IsAgendaItem](IsAgendaItem.md) | A mixin class that provides the elements of an agenda item: designation, type... |  no  |
| [AgendaItem](AgendaItem.md) | An agenda item of a meeting as planned beforehand |  no  |
| [ProtocolItem](ProtocolItem.md) | An agenda item as actually recorded in the protocol |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [IsAgendaItem](IsAgendaItem.md) |

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
    value: 'Nummer des Traktandums auf der Traktandenliste, z.B. „2.1“ oder „3“ (Zeichenkette,
      damit auch römische Ziffern möglich sind).

      '
  description_fr:
    tag: description_fr
    value: 'Numéro du point sur l''ordre du jour, p. ex. « 2.1 » ou « 3 » (chaîne
      de caractères, afin de permettre aussi les chiffres romains).

      '
description: 'Number of the agenda item on the agenda, e.g. "2.1" or "3" (string type
  to also support roman numerals).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IsAgendaItem
range: string

```
</details></div>