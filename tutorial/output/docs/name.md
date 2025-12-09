

# Slot: name 



URI: [schema:name](http://schema.org/name)
Alias: name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AgendaItem](AgendaItem.md) |  |  no  |
| [Session](Session.md) |  |  no  |






## Properties

* Range: [MultilingualString](MultilingualString.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/tutorial




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:name |
| native | tutorial:name |




## LinkML Source

<details>
```yaml
name: name
from_schema: https://ch.paf.link/schema/tutorial
rank: 1000
slot_uri: schema:name
alias: name
domain_of:
- Session
- AgendaItem
range: MultilingualString
multivalued: true
inlined: true
inlined_as_list: true

```
</details>