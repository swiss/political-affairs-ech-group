

# Slot: addresses 


_[en] Addresses (private, business, local)._

_[de] Adressen (privat, geschäftlich, lokal)._

__





URI: [act:address](https://ch.paf.link/schema/actors/address)
Alias: addresses

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | [en] A person with identifiers, names, addresses, citizenships, and occupatio... |  no  |
| [Group](Group.md) | [en] A political group, organization, or body (e |  no  |






## Properties

* Range: [Address](Address.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:address |
| native | act:addresses |




## LinkML Source

<details>
```yaml
name: addresses
description: '[en] Addresses (private, business, local).

  [de] Adressen (privat, geschäftlich, lokal).

  '
from_schema: https://ch.paf.link/schema/actors
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