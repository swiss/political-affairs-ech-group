---
search:
  boost: 5.0
---

# Slot: state_name 


_[en] Custom state description for the meeting._

_[de] Benutzerdefinierte Zustandsbeschreibung für die Sitzung._

__



<div data-search-exclude markdown="1">



URI: [ops:state_name](https://ch.paf.link/schema/operations/state_name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |
| [AgendaItem](AgendaItem.md) | [en] An agenda item of a meeting |  no  |
| [ProtocolItem](ProtocolItem.md) | [en] An agenda item as actually recorded in the protocol |  no  |






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
description: '[en] Custom state description for the meeting.

  [de] Benutzerdefinierte Zustandsbeschreibung für die Sitzung.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Meeting
- AgendaItem
range: string

```
</details></div>