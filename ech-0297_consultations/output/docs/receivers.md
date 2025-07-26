

# Slot: receivers



URI: [chpaf:receiver](https://ch.paf.link/receiver)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Consultation](Consultation.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/consultation




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | chpaf:receiver |
| native | chpaf:receivers |




## LinkML Source

<details>
```yaml
name: receivers
from_schema: https://ch.paf.link/schema/consultation
rank: 1000
slot_uri: chpaf:receiver
alias: receivers
domain_of:
- Consultation
range: string
multivalued: true
inlined: true
inlined_as_list: true

```
</details>