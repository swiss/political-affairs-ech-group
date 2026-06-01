---
search:
  boost: 5.0
---

# Slot: citizenships 


_Citizenships of the person._

__



<div data-search-exclude markdown="1">



URI: [act:citizenship](https://ld.ech.ch/schema/0294/actors/citizenship)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Citizenship](Citizenship.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [act:citizenship](https://ld.ech.ch/schema/0294/actors/citizenship) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: citizenships
annotations:
  description_de:
    tag: description_de
    value: 'Staatsbürgerschaften der Person.

      '
description: 'Citizenships of the person.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:citizenship
domain_of:
- Person
range: Citizenship
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>