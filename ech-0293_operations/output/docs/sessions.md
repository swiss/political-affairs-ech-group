

# Slot: sessions 



URI: [ops:session](https://ch.paf.link/schema/operations/session)
Alias: sessions

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Session](Session.md) |
| Domain Of | [Container](Container.md) |
| Slot URI | [ops:session](https://ch.paf.link/schema/operations/session) |

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
| self | ops:session |
| native | ops:sessions |




## LinkML Source

<details>
```yaml
name: sessions
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:session
alias: sessions
domain_of:
- Container
range: Session
multivalued: true
inlined: true
inlined_as_list: true

```
</details>