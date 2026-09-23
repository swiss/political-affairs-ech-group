---
search:
  boost: 5.0
---

# Slot: agenda_item_position 


_Integer position of the agenda item in the meeting sequence, used for sorting and display._




<div data-search-exclude markdown="1">



URI: [ops:agenda_item_position](https://ch.paf.link/schema/operations/agenda_item_position)
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
| Range | [Integer](Integer.md) |
| Domain Of | [IsAgendaItem](IsAgendaItem.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: agenda_item_position
annotations:
  description_de:
    tag: description_de
    value: 'Ganzzahlige Position des Traktandums im Sitzungsablauf, massgebend für
      Sortierung und Darstellung.

      '
  description_fr:
    tag: description_fr
    value: 'Position entière du point dans le déroulement de la séance, déterminante
      pour le tri et l''affichage.

      '
description: 'Integer position of the agenda item in the meeting sequence, used for
  sorting and display.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IsAgendaItem
range: integer

```
</details></div>