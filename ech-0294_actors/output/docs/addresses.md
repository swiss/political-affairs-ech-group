

# Slot: addresses 


_[de] Adressen mit Typ (privat, geschäftlich, lokal)._

_[en] Addresses with type (private, business, local)._

__





URI: [act:address](https://ld.ech.ch/schema/0294/actors/address)
Alias: addresses

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Group](Group.md) | [de] Eine politische Gruppe, Organisation oder Körperschaft (z |  no  |
| [Person](Person.md) | [de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften u... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Address](Address.md) |
| Domain Of | [Person](Person.md), [Group](Group.md) |
| Slot URI | [act:address](https://ld.ech.ch/schema/0294/actors/address) |

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
| self | act:address |
| native | act:addresses |




## LinkML Source

<details>
```yaml
name: addresses
description: '[de] Adressen mit Typ (privat, geschäftlich, lokal).

  [en] Addresses with type (private, business, local).

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:address
alias: addresses
domain_of:
- Person
- Group
range: Address
multivalued: true
inlined: true
inlined_as_list: true

```
</details>