---
search:
  boost: 5.0
---

# Slot: trainings 


_Trainings or educations of the person. Guideline: generally only provide the highest qualification obtained._

__



<div data-search-exclude markdown="1">



URI: [act:training](https://ld.ech.ch/schema/0294/actors/training)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Training](Training.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [act:training](https://ld.ech.ch/schema/0294/actors/training) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: trainings
annotations:
  description_de:
    tag: description_de
    value: 'Ausbildungen oder Bildungen der Person. Richtlinie: Im Grundsatz nur die
      höchste Ausbildung angeben.

      '
description: 'Trainings or educations of the person. Guideline: generally only provide
  the highest qualification obtained.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:training
domain_of:
- Person
range: Training
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>