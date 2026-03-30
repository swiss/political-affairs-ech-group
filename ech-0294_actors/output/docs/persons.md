

# Slot: persons 


_[de] Sammlung von Personen._

_[en] Collection of persons._

__





URI: [act:person](https://ld.ech.ch/schema/0294/actors/person)
Alias: persons

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) | [de] Container für politische Akteure, Gruppen und Beziehungen |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Person](Person.md) |
| Domain Of | [Container](Container.md) |
| Slot URI | [act:person](https://ld.ech.ch/schema/0294/actors/person) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:person |
| native | act:persons |




## LinkML Source

<details>
```yaml
name: persons
description: '[de] Sammlung von Personen.

  [en] Collection of persons.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
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