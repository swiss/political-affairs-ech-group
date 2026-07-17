---
search:
  boost: 5.0
---

# Slot: pronouns 


_Pronouns used by the person._

__



<div data-search-exclude markdown="1">



URI: [act:pronouns](https://ld.ech.ch/schema/0294/actors/pronouns)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Gender](Gender.md) | Gender of a person indicating a gender code and temporal validity |  no  |






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
description: 'Pronouns used by the person.

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