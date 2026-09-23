---
search:
  boost: 5.0
---

# Slot: state_id 


_State identifier of the agenda item (reference to a state enumeration or a custom state), e.g. pending (not yet dealt with), in_progress, completed, postponed (to a later meeting) or withdrawn._




<div data-search-exclude markdown="1">



URI: [ops:state_id](https://ch.paf.link/schema/operations/state_id)
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
name: state_id
annotations:
  description_de:
    tag: description_de
    value: 'Zustands-Identifikator des Traktandums (Verweis auf ein Status-Enum oder
      auf einen eigenen Zustand), z.B. pending (noch nicht behandelt), in_progress
      (in Beratung), completed (abgeschlossen), postponed (auf eine spätere Sitzung
      vertagt) oder withdrawn (zurückgezogen).

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant d''état du point (renvoi à une énumération des états ou à
      un état propre), p. ex. pending (pas encore traité), in_progress (en délibération),
      completed (traité), postponed (renvoyé à une séance ultérieure) ou withdrawn
      (retiré).

      '
description: 'State identifier of the agenda item (reference to a state enumeration
  or a custom state), e.g. pending (not yet dealt with), in_progress, completed, postponed
  (to a later meeting) or withdrawn.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- IsAgendaItem
range: string

```
</details></div>