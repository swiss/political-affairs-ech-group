---
search:
  boost: 5.0
---

# Slot: names 


_Names of the person with type and value._

__



<div data-search-exclude markdown="1">



URI: [act:name](https://ld.ech.ch/schema/0294/actors/name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Name](Name.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [act:name](https://ld.ech.ch/schema/0294/actors/name) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: names
annotations:
  description_de:
    tag: description_de
    value: 'Namen der Person mit Typ und Wert.

      '
description: 'Names of the person with type and value.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:name
domain_of:
- Person
range: Name
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>