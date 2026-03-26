

# Slot: meetings 



URI: [ops:meeting](https://ch.paf.link/schema/operations/meeting)
Alias: meetings

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) |  |  no  |
| [Session](Session.md) | [en] A parliamentary session that groups multiple meetings and spans a specif... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Meeting](Meeting.md) |
| Domain Of | [Container](Container.md), [Session](Session.md) |
| Slot URI | [ops:meeting](https://ch.paf.link/schema/operations/meeting) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:meeting |
| native | ops:meetings |




## LinkML Source

<details>
```yaml
name: meetings
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:meeting
alias: meetings
domain_of:
- Container
- Session
range: Meeting
multivalued: true
inlined: true
inlined_as_list: true

```
</details>