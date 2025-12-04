

# Slot: meeting_type 


_Type of the meeting, e.g. session, committee, sitting, various_





URI: [ops:meetingType](https://ch.paf.link/schema/operations/meetingType)
Alias: meeting_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |






## Properties

* Range: [MeetingTypeEnum](MeetingTypeEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:meetingType |
| native | ops:meeting_type |




## LinkML Source

<details>
```yaml
name: meeting_type
description: Type of the meeting, e.g. session, committee, sitting, various
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:meetingType
alias: meeting_type
domain_of:
- Meeting
range: meeting_type_enum

```
</details>