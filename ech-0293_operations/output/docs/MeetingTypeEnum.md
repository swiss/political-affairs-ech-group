# Enum: MeetingTypeEnum 




_Type of the meeting_



URI: [ops:meeting_type_enum](https://ch.paf.link/schema/operations/meeting_type_enum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| session | ops:enum/meeting_type/session |  |
| committee | ops:enum/meeting_type/committee |  |
| sitting | ops:enum/meeting_type/sitting |  |
| various | ops:enum/meeting_type/various |  |




## Slots

| Name | Description |
| ---  | --- |
| [meeting_type](meeting_type.md) | Type of the meeting, e |





## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations






## LinkML Source

<details>
```yaml
name: meeting_type_enum
description: Type of the meeting
from_schema: https://ch.paf.link/schema/operations
rank: 1000
permissible_values:
  session:
    text: session
    meaning: ops:enum/meeting_type/session
  committee:
    text: committee
    meaning: ops:enum/meeting_type/committee
  sitting:
    text: sitting
    meaning: ops:enum/meeting_type/sitting
  various:
    text: various
    meaning: ops:enum/meeting_type/various

```
</details>