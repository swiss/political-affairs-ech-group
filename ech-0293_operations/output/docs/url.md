

# Slot: url 



URI: [ops:url](https://ch.paf.link/schema/operations/url)
Alias: url

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Media](Media.md) | [en] Media files or documents (including protocols in PDF/HTML/WORD or links ... |  no  |
| [Session](Session.md) | [en] A parliamentary session that groups multiple meetings and spans a specif... |  no  |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |






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
- Session
- Meeting
- Media
range: MultilingualString
multivalued: true
inlined: true
inlined_as_list: true

```
</details>