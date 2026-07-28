---
search:
  boost: 5.0
---

# Slot: addresses 


_Adresses avec type (privée, professionnelle, locale)._

__



<div data-search-exclude markdown="1">



URI: [act:address](https://ld.ech.ch/schema/0294/actors/address)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Person](Person.md) | Une personne avec des identifiants, des noms, des adresses, des nationalités ... |  no  |
| [Group](Group.md) | Un groupe, une organisation ou une collectivité politique (p |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Address](Address.md) |
| Domaine de | [Person](Person.md), [Group](Group.md) |
| URI du slot | [act:address](https://ld.ech.ch/schema/0294/actors/address) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |









## Exemples

| Valeur |
| --- |
| [{'address_type': 'businessAddress', 'address_URI': 'https://ld.admin.ch/address/12345', 'street_address': 'Bundesplatz 3', 'postal_code': '3003', 'postal_locality': 'Bern'}, {'address_type': 'privateAddress', 'postal_locality': 'Zürich'}] |





## Source LinkML

<details>
```yaml
name: addresses
annotations:
  description_de:
    tag: description_de
    value: 'Adressen mit Typ (privat, geschäftlich, lokal).

      '
  description_fr:
    tag: description_fr
    value: 'Adresses avec type (privée, professionnelle, locale).

      '
description: 'Adresses avec type (privée, professionnelle, locale).

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