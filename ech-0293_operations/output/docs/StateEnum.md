# Enum: StateEnum 




_State of the meeting_



URI: [StateEnum](StateEnum.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| planned | ops:state/planned |  |
| canceled | ops:state/canceled |  |
| postponed | ops:state/postponed |  |




## Slots

| Name | Description |
| ---  | --- |
| [state](state.md) |  |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/operations






## LinkML Source

<details>
```yaml
name: state_enum
description: State of the meeting
from_schema: https://ch.paf.link/schema/operations
rank: 1000
permissible_values:
  planned:
    text: planned
    meaning: ops:state/planned
  canceled:
    text: canceled
    meaning: ops:state/canceled
  postponed:
    text: postponed
    meaning: ops:state/postponed

```
</details>
