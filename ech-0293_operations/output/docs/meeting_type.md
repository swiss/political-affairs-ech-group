---
search:
  boost: 5.0
---

# Slot: meeting_type 


_Type of the meeting, e.g. session, committee, sitting, various_



<div data-search-exclude markdown="1">



URI: [ops:meetingType](https://ch.paf.link/schema/operations/meetingType)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MeetingTypeEnum](MeetingTypeEnum.md) |
| Domain Of | [Meeting](Meeting.md) |
| Slot URI | [ops:meetingType](https://ch.paf.link/schema/operations/meetingType) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| committee |
| session |
| sitting |





## LinkML Source

<details>
```yaml
name: meeting_type
description: Type of the meeting, e.g. session, committee, sitting, various
examples:
- value: committee
- value: session
- value: sitting
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:meetingType
domain_of:
- Meeting
range: MeetingTypeEnum

```
</details></div>