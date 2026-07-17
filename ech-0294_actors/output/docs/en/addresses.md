---
search:
  boost: 5.0
---

# Slot: addresses 


_Addresses with type (private, business, local)._

__



<div data-search-exclude markdown="1">



URI: [act:address](https://ld.ech.ch/schema/0294/actors/address)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |
| [Group](Group.md) | A political group, organization, or body (e |  no  |






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





## LinkML Source

<details>
```yaml
name: addresses
annotations:
  description_de:
    tag: description_de
    value: 'Adressen mit Typ (privat, geschäftlich, lokal).

      '
description: 'Addresses with type (private, business, local).

  '
examples:
- value: '[{''address_type'': ''businessAddress'', ''address_URI'': ''https://ld.admin.ch/address/12345'',
    ''street_address'': ''Bundesplatz 3'', ''postal_code'': ''3003'', ''postal_locality'':
    ''Bern''}, {''address_type'': ''privateAddress'', ''postal_locality'': ''Zürich''}]'
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:address
domain_of:
- Person
- Group
range: Address
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>