---
search:
  boost: 5.0
---

# Slot: protocol 


_[en] The protocol (minutes) of this meeting, recorded after the meeting._

_[de] Das nach der Sitzung erstellte Protokoll dieser Sitzung._

__



<div data-search-exclude markdown="1">



URI: [ops:protocol](https://ch.paf.link/schema/operations/protocol)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Protocol](Protocol.md) |
| Domain Of | [Meeting](Meeting.md) |
| Slot URI | [ops:protocol](https://ch.paf.link/schema/operations/protocol) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:protocol |
| native | ops:protocol |




## LinkML Source

<details>
```yaml
name: protocol
description: '[en] The protocol (minutes) of this meeting, recorded after the meeting.

  [de] Das nach der Sitzung erstellte Protokoll dieser Sitzung.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:protocol
domain_of:
- Meeting
range: Protocol
inlined: true

```
</details></div>