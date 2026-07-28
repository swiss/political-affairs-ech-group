---
search:
  boost: 5.0
---

# Slot: names 


_Noms de la personne avec type et valeur._

__



<div data-search-exclude markdown="1">



URI: [act:name](https://ld.ech.ch/schema/0294/actors/name)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Person](Person.md) | Une personne avec des identifiants, des noms, des adresses, des nationalités ... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Name](Name.md) |
| Domaine de | [Person](Person.md) |
| URI du slot | [act:name](https://ld.ech.ch/schema/0294/actors/name) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |
| Multivalué | Yes |












## Source LinkML

<details>
```yaml
name: names
annotations:
  description_de:
    tag: description_de
    value: 'Namen der Person mit Typ und Wert.

      '
  description_fr:
    tag: description_fr
    value: 'Noms de la personne avec type et valeur.

      '
description: 'Noms de la personne avec type et valeur.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:name
domain_of:
- Person
range: Name
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>