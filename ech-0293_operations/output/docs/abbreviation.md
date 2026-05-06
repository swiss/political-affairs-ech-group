

# Slot: abbreviation 



URI: [ops:abbreviation](https://ch.paf.link/schema/operations/abbreviation)
Alias: abbreviation

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
| self | ops:abbreviation |
| native | ops:abbreviation |




## LinkML Source

<details>
```yaml
name: abbreviation
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: abbreviation
domain_of:
- Session
- Meeting
range: string

```
</details>