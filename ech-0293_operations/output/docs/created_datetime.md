

# Slot: created_datetime 


_The time this record was created_





URI: [ops:created_datetime](https://ch.paf.link/schema/operations/created_datetime)
Alias: created_datetime

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Session](Session.md) |  |  no  |
| [Meeting](Meeting.md) |  |  no  |
| [Legislature](Legislature.md) |  |  no  |
| [MeetingItem](MeetingItem.md) |  |  no  |







## Properties

* Range: [Datetime](Datetime.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:created_datetime |
| native | ops:created_datetime |




## LinkML Source

<details>
```yaml
name: created_datetime
description: The time this record was created
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: created_datetime
domain_of:
- Legislature
- Session
- Meeting
- MeetingItem
range: datetime

```
</details>