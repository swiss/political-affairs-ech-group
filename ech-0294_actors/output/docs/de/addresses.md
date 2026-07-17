---
search:
  boost: 5.0
---

# Slot: addresses 


_Adressen mit Typ (privat, geschäftlich, lokal)._

__



<div data-search-exclude markdown="1">



URI: [act:address](https://ld.ech.ch/schema/0294/actors/address)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Person](Person.md) | Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften und Be... |  no  |
| [Group](Group.md) | Eine politische Gruppe, Organisation oder Körperschaft (z |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [Address](Address.md) |
| Domäne von | [Person](Person.md), [Group](Group.md) |
| Slot-URI | [act:address](https://ld.ech.ch/schema/0294/actors/address) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |
| Mehrwertig | Yes |









## Beispiele

| Wert |
| --- |
| [{'address_type': 'businessAddress', 'address_URI': 'https://ld.admin.ch/address/12345', 'street_address': 'Bundesplatz 3', 'postal_code': '3003', 'postal_locality': 'Bern'}, {'address_type': 'privateAddress', 'postal_locality': 'Zürich'}] |





## LinkML-Quelle

<details>
```yaml
name: addresses
annotations:
  description_de:
    tag: description_de
    value: 'Adressen mit Typ (privat, geschäftlich, lokal).

      '
description: 'Adressen mit Typ (privat, geschäftlich, lokal).

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