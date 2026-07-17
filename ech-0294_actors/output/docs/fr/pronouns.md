---
search:
  boost: 5.0
---

# Slot: pronouns 


_Pronoms utilisés par la personne._

__



<div data-search-exclude markdown="1">



URI: [act:pronouns](https://ld.ech.ch/schema/0294/actors/pronouns)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Gender](Gender.md) | Sexe d'une personne indiquant un code de sexe et la validité temporelle |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Gender](Gender.md) |
| URI du slot | [act:pronouns](https://ld.ech.ch/schema/0294/actors/pronouns) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: pronouns
annotations:
  description_de:
    tag: description_de
    value: 'Von der Person verwendete Pronomen.

      '
  description_fr:
    tag: description_fr
    value: 'Pronoms utilisés par la personne.

      '
description: 'Pronoms utilisés par la personne.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:pronouns
domain_of:
- Gender
range: string
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>