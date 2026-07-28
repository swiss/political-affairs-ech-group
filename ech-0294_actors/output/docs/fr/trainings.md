---
search:
  boost: 5.0
---

# Slot: trainings 


_Formations ou éducations de la personne. Directive : n'indiquer en principe que la qualification la plus élevée obtenue._

__



<div data-search-exclude markdown="1">



URI: [act:training](https://ld.ech.ch/schema/0294/actors/training)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Person](Person.md) | Une personne avec des identifiants, des noms, des adresses, des nationalités ... |  no  |






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
  description_fr:
    tag: description_fr
    value: 'Formations ou éducations de la personne. Directive : n''indiquer en principe
      que la qualification la plus élevée obtenue.

      '
description: 'Formations ou éducations de la personne. Directive : n''indiquer en
  principe que la qualification la plus élevée obtenue.

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