

# Slot: description 



URI: [ops:description](https://ch.paf.link/schema/operations/description)
Alias: description

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Session](Session.md) |  |  no  |
| [Meeting](Meeting.md) |  |  no  |
| [Legislature](Legislature.md) |  |  no  |
| [MeetingItem](MeetingItem.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:description |
| native | ops:description |




## LinkML Source

<details>
```yaml
name: description
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: description
domain_of:
- Legislature
- Session
- Meeting
- MeetingItem
range: string

```
</details>