

# Slot: id 



URI: [dcterm:identifier](http://purl.org/dc/terms/identifier)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MeetingItem](MeetingItem.md) |  |  no  |
| [Container](Container.md) |  |  no  |
| [Session](Session.md) |  |  no  |
| [Meeting](Meeting.md) |  |  no  |
| [Legislature](Legislature.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterm:identifier |
| native | ops:id |




## LinkML Source

<details>
```yaml
name: id
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: dcterm:identifier
identifier: true
alias: id
domain_of:
- Container
- Legislature
- Session
- Meeting
- MeetingItem
range: string
required: true

```
</details>