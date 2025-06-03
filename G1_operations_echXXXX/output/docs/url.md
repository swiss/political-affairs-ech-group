

# Slot: url 



URI: [ops:url](https://ch.paf.link/schema/operations/url)
Alias: url

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Session](Session.md) |  |  no  |
| [MeetingItem](MeetingItem.md) |  |  no  |
| [Legislature](Legislature.md) |  |  no  |
| [Meeting](Meeting.md) |  |  no  |







## Properties

* Range: [MultilingualString](MultilingualString.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:url |
| native | ops:url |




## LinkML Source

<details>
```yaml
name: url
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: url
domain_of:
- Legislature
- Session
- Meeting
- MeetingItem
range: MultilingualString
multivalued: true
inlined: true
inlined_as_list: true

```
</details>