---
search:
  boost: 5.0
---

# Slot: persons 


_Collection of persons._

__



<div data-search-exclude markdown="1">



URI: [act:person](https://ld.ech.ch/schema/0294/actors/person)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) | Container for political actors, groups, and relationships |  no  |






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












## LinkML Source

<details>
```yaml
name: persons
annotations:
  description_de:
    tag: description_de
    value: 'Sammlung von Personen.

      '
  description_fr:
    tag: description_fr
    value: 'Collection de personnes.

      '
description: 'Collection of persons.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:person
domain_of:
- Container
range: Person
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>