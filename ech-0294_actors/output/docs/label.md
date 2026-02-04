

# Slot: label 


_[en] Display name of the person._

_[de] Anzeigename der Person._

__





URI: [act:label](https://ch.paf.link/schema/actors/label)
Alias: label

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | [en] A person with identifiers, names, addresses, citizenships, and occupatio... |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:label |
| native | act:label |




## LinkML Source

<details>
```yaml
name: label
description: '[en] Display name of the person.

  [de] Anzeigename der Person.

  '
from_schema: https://ch.paf.link/schema/actors
rank: 1000
alias: label
domain_of:
- Person
range: string
required: true

```
</details>