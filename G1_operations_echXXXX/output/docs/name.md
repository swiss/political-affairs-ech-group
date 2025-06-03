

# Slot: name 



URI: [ops:name](https://ch.paf.link/schema/operations/name)
Alias: name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Session](Session.md) |  |  no  |
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
| self | ops:name |
| native | ops:name |




## LinkML Source

<details>
```yaml
name: name
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: name
domain_of:
- Legislature
- Session
- Meeting
range: MultilingualString
multivalued: true
inlined: true
inlined_as_list: true

```
</details>