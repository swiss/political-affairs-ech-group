---
search:
  boost: 5.0
---

# Slot: genders 


_Gender of the person._

__



<div data-search-exclude markdown="1">



URI: [act:gender](https://ld.ech.ch/schema/0294/actors/gender)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Gender](Gender.md) |
| Domaine de | [Person](Person.md) |
| URI du slot | [act:gender](https://ld.ech.ch/schema/0294/actors/gender) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: genders
annotations:
  description_de:
    tag: description_de
    value: 'Geschlecht der Person.

      '
description: 'Gender of the person.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:gender
domain_of:
- Person
range: Gender
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>