

# Slot: persons 


_[en] Collection of persons._

_[de] Sammlung von Personen._

__





URI: [act:person](https://ch.paf.link/schema/actors/person)
Alias: persons

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) | [en] Root container holding all political actors, groups, and relationships |  no  |






## Properties

* Range: [Person](Person.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:person |
| native | act:persons |




## LinkML Source

<details>
```yaml
name: persons
description: '[en] Collection of persons.

  [de] Sammlung von Personen.

  '
from_schema: https://ch.paf.link/schema/actors
rank: 1000
slot_uri: act:person
alias: persons
domain_of:
- Container
range: Person
multivalued: true
inlined: true
inlined_as_list: true

```
</details>