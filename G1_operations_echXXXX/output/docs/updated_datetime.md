

# Slot: updated_datetime 


_The last time this record was updated_





URI: [ops:updated_datetime](https://ch.paf.link/schema/operations/updated_datetime)
Alias: updated_datetime

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MeetingItem](MeetingItem.md) |  |  no  |
| [Meeting](Meeting.md) |  |  no  |
| [Session](Session.md) |  |  no  |
| [Legislature](Legislature.md) |  |  no  |







## Properties

* Range: [Datetime](Datetime.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:updated_datetime |
| native | ops:updated_datetime |




## LinkML Source

<details>
```yaml
name: updated_datetime
description: The last time this record was updated
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: updated_datetime
domain_of:
- Legislature
- Session
- Meeting
- MeetingItem
range: datetime

```
</details>