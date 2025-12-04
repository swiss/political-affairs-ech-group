# Enum: StateEnum 




_State of the meeting_



URI: [ops:state_enum](https://ch.paf.link/schema/operations/state_enum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| planned | ops:enum/state/planned |  |
| canceled | ops:enum/state/canceled |  |
| postponed | ops:enum/state/postponed |  |




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
    meaning: ops:enum/state/planned
  canceled:
    text: canceled
    meaning: ops:enum/state/canceled
  postponed:
    text: postponed
    meaning: ops:enum/state/postponed

```
</details>