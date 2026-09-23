---
search:
  boost: 5.0
---

# Slot: state_name 


_Diverging, free-text status designation, where the status enumeration does not suffice._




<div data-search-exclude markdown="1">



URI: [ops:state_name](https://ch.paf.link/schema/operations/state_name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | The individual sitting of a body — the level at which agenda items are delibe... |  yes  |
| [IsAgendaItem](IsAgendaItem.md) | A mixin class that provides the elements of an agenda item: designation, type... |  no  |
| [AgendaItem](AgendaItem.md) | An agenda item of a meeting as planned beforehand |  no  |
| [ProtocolItem](ProtocolItem.md) | An agenda item as actually recorded in the protocol |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Meeting](Meeting.md), [IsAgendaItem](IsAgendaItem.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: state_name
annotations:
  description_de:
    tag: description_de
    value: 'Abweichende, freitextliche Statusbezeichnung, wo die Status-Aufzählung
      nicht genügt.

      '
  description_fr:
    tag: description_fr
    value: 'Désignation de statut divergente, en texte libre, là où l''énumération
      des statuts ne suffit pas.

      '
description: 'Diverging, free-text status designation, where the status enumeration
  does not suffice.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
- IsAgendaItem
range: string

```
</details></div>