

# Slot: meeting_items 



URI: [ops:meetingItem](https://ch.paf.link/schema/operations/meetingItem)
Alias: meeting_items

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) |  |  no  |







## Properties

* Range: [MeetingItem](MeetingItem.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:meetingItem |
| native | ops:meeting_items |




## LinkML Source

<details>
```yaml
name: meeting_items
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:meetingItem
alias: meeting_items
domain_of:
- Container
range: MeetingItem
multivalued: true
inlined: true
inlined_as_list: true

```
</details>