

# Slot: function 


_Function of the person (e.g. president, member)_





URI: [act:function](https://ch.paf.link/schema/actors/function)
Alias: function

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonReference](PersonReference.md) | Reference to a person acting in a specific role or function |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:function |
| native | act:function |




## LinkML Source

<details>
```yaml
name: function
description: Function of the person (e.g. president, member)
from_schema: https://ch.paf.link/schema/actors
rank: 1000
alias: function
owner: PersonReference
domain_of:
- PersonReference
range: string

```
</details>