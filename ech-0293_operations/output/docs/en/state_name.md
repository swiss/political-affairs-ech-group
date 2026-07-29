---
search:
  boost: 5.0
---

# Slot: state_name 


_Custom state description for the meeting._




<div data-search-exclude markdown="1">



URI: [ops:state_name](https://ch.paf.link/schema/operations/state_name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | A general meeting class used for Sessions, Comittee Meetings, individual sess... |  no  |
| [AgendaItem](AgendaItem.md) | An agenda item of a meeting |  no  |
| [ProtocolItem](ProtocolItem.md) | An agenda item as actually recorded in the protocol |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Meeting](Meeting.md), [AgendaItem](AgendaItem.md) |

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
    value: 'Benutzerdefinierte Zustandsbeschreibung für die Sitzung.

      '
  description_fr:
    tag: description_fr
    value: 'Description personnalisée de l''état de la séance.

      '
description: 'Custom state description for the meeting.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
- AgendaItem
range: string

```
</details></div>