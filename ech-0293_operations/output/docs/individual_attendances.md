

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

* Range: [IndividualAttendance](IndividualAttendance.md)

* Multivalued: True




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