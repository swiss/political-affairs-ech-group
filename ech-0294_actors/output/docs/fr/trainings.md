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





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Training](Training.md) |
| Domaine de | [Person](Person.md) |
| URI du slot | [act:training](https://ld.ech.ch/schema/0294/actors/training) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

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