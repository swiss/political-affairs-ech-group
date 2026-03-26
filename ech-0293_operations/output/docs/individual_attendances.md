

# Slot: individual_attendances 


_Collection of individual attendance records_





URI: [ops:individualAttendance](https://ch.paf.link/schema/operations/individualAttendance)
Alias: individual_attendances

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [IndividualAttendance](IndividualAttendance.md) |
| Domain Of | [Container](Container.md) |
| Slot URI | [ops:individualAttendance](https://ch.paf.link/schema/operations/individualAttendance) |

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
| self | ops:individualAttendance |
| native | ops:individual_attendances |




## LinkML Source

<details>
```yaml
name: individual_attendances
description: Collection of individual attendance records
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:individualAttendance
alias: individual_attendances
domain_of:
- Container
range: IndividualAttendance
multivalued: true
inlined: true
inlined_as_list: true

```
</details>