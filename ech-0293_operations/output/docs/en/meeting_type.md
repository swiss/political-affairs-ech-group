---
search:
  boost: 5.0
---

# Slot: meeting_type 


_Type of the meeting, e.g. session, committee, sitting, various._




<div data-search-exclude markdown="1">



URI: [ops:meetingType](https://ch.paf.link/schema/operations/meetingType)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | A general meeting class used for Sessions, Comittee Meetings, individual sess... |  no  |






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
annotations:
  description_de:
    tag: description_de
    value: 'Art der Sitzung, z.B. Session, Kommission, Sessionssitzung, Verschiedenes.

      '
  description_fr:
    tag: description_fr
    value: 'Type de séance, p. ex. session, commission, séance de session, divers.

      '
description: 'Type of the meeting, e.g. session, committee, sitting, various.

  '
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