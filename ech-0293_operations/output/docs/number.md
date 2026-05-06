

# Slot: number 



URI: [ops:number](https://ch.paf.link/schema/operations/number)
Alias: number

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Session](Session.md) | [en] A parliamentary session that groups multiple meetings and spans a specif... |  no  |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Session](Session.md), [Meeting](Meeting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:number |
| native | ops:number |




## LinkML Source

<details>
```yaml
name: number
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: number
domain_of:
- Session
- Meeting
range: string

```
</details>