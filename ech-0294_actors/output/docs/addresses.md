---
search:
  boost: 5.0
---

# Slot: addresses 


_[de] Adressen mit Typ (privat, geschäftlich, lokal)._

_[en] Addresses with type (private, business, local)._

__



<div data-search-exclude markdown="1">



URI: [act:address](https://ld.ech.ch/schema/0294/actors/address)
Alias: addresses

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | [de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften u... |  no  |
| [Group](Group.md) | [de] Eine politische Gruppe, Organisation oder Körperschaft (z |  no  |






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









## Examples

| Value |
| --- |
| [{'address_type': 'businessAddress', 'address_URI': 'https://ld.admin.ch/address/12345', 'street_address': 'Bundesplatz 3', 'postal_code': '3003', 'postal_locality': 'Bern'}, {'address_type': 'privateAddress', 'postal_locality': 'Zürich'}] |



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
examples:
- value: '[{''address_type'': ''businessAddress'', ''address_URI'': ''https://ld.admin.ch/address/12345'',
    ''street_address'': ''Bundesplatz 3'', ''postal_code'': ''3003'', ''postal_locality'':
    ''Bern''}, {''address_type'': ''privateAddress'', ''postal_locality'': ''Zürich''}]'
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
</details></div>