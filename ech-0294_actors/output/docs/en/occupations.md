---
search:
  boost: 5.0
---

# Slot: occupations 


_Occupations or professions of the person._

__



<div data-search-exclude markdown="1">



URI: [act:occupation](https://ld.ech.ch/schema/0294/actors/occupation)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Occupation](Occupation.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [act:occupation](https://ld.ech.ch/schema/0294/actors/occupation) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: occupations
annotations:
  description_de:
    tag: description_de
    value: 'Berufe oder Tätigkeiten der Person.

      '
description: 'Occupations or professions of the person.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:occupation
domain_of:
- Person
range: Occupation
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>