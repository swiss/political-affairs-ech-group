

# Slot: name 



URI: [ops:name](https://ch.paf.link/schema/operations/name)
Alias: name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |
| [Legislature](Legislature.md) | [en] Term of office of a parliament as a legislative assembly |  no  |
| [Session](Session.md) | [en] A parliamentary session that groups multiple meetings and spans a specif... |  no  |






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