

# Slot: sessions 



URI: [tutorial:session](https://ch.paf.link/schema/tutorial/session)
Alias: sessions

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) |  |  no  |







## Properties

* Range: [Session](Session.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/tutorial




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tutorial:session |
| native | tutorial:sessions |




## LinkML Source

<details>
```yaml
name: sessions
from_schema: https://ch.paf.link/schema/tutorial
rank: 1000
slot_uri: tutorial:session
alias: sessions
domain_of:
- Container
range: Session
multivalued: true
inlined: true
inlined_as_list: true

```
</details>