

# Slot: phone



URI: [personinfo:phone](https://w3id.org/linkml/examples/personinfo/phone)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[\d\(\)\-]+$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/linkml/examples/personinfo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | personinfo:phone |
| native | personinfo:phone |




## LinkML Source

<details>
```yaml
name: phone
from_schema: https://w3id.org/linkml/examples/personinfo
rank: 1000
alias: phone
owner: Person
domain_of:
- Person
range: string
pattern: ^[\d\(\)\-]+$

```
</details>