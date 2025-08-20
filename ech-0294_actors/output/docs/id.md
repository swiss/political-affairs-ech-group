

# Slot: id 



URI: [dcterm:identifier](http://purl.org/dc/terms/identifier)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) |  |  no  |
| [Actor](Actor.md) |  |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterm:identifier |
| native | act:id |




## LinkML Source

<details>
```yaml
name: id
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: dcterm:identifier
identifier: true
alias: id
domain_of:
- Container
- Actor
range: string
required: true

```
</details>