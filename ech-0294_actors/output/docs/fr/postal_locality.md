---
search:
  boost: 5.0
---

# Slot: postal_locality 


_Localité._

__



<div data-search-exclude markdown="1">



URI: [act:postalLocality](https://ld.ech.ch/schema/0294/actors/postalLocality)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Address](Address.md) | Une adresse avec un type (p |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [String](String.md) |
| Domaine de | [Address](Address.md) |
| URI du slot | [act:postalLocality](https://ld.ech.ch/schema/0294/actors/postalLocality) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |









## Exemples

| Valeur |
| --- |
| Basel-Stadt |





## Source LinkML

<details>
```yaml
name: postal_locality
annotations:
  description_de:
    tag: description_de
    value: 'Ort.

      '
  description_fr:
    tag: description_fr
    value: 'Localité.

      '
description: 'Localité.

  '
examples:
- value: Basel-Stadt
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:postalLocality
domain_of:
- Address
range: string

```
</details></div>