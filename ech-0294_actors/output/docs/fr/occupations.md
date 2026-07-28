---
search:
  boost: 5.0
---

# Slot: occupations 


_Métiers ou professions de la personne._

__



<div data-search-exclude markdown="1">



URI: [act:occupation](https://ld.ech.ch/schema/0294/actors/occupation)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Person](Person.md) | Une personne avec des identifiants, des noms, des adresses, des nationalités ... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Occupation](Occupation.md) |
| Domaine de | [Person](Person.md) |
| URI du slot | [act:occupation](https://ld.ech.ch/schema/0294/actors/occupation) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: occupations
annotations:
  description_de:
    tag: description_de
    value: 'Berufe oder Tätigkeiten der Person.

      '
  description_fr:
    tag: description_fr
    value: 'Métiers ou professions de la personne.

      '
description: 'Métiers ou professions de la personne.

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