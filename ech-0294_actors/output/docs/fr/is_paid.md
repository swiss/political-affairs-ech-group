---
search:
  boost: 5.0
---

# Slot: is_paid 


_Indique si le poste est rémunéré._

__



<div data-search-exclude markdown="1">



URI: [act:isPaid](https://ld.ech.ch/schema/0294/actors/isPaid)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | Un lien d'intérêts (conflit d'intérêts, financement politique) d'une personne... |  no  |
| [Occupation](Occupation.md) | Métier ou profession d'une personne indiquant un libellé, un code ISCO-19, si... |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [Boolean](Boolean.md) |
| Domaine de | [InterestLink](InterestLink.md), [Occupation](Occupation.md) |
| URI du slot | [act:isPaid](https://ld.ech.ch/schema/0294/actors/isPaid) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |









## Exemples

| Valeur |
| --- |
| False |
| True |





## Source LinkML

<details>
```yaml
name: is_paid
annotations:
  description_de:
    tag: description_de
    value: 'Gibt an, ob die Position bezahlt ist.

      '
  description_fr:
    tag: description_fr
    value: 'Indique si le poste est rémunéré.

      '
description: 'Indique si le poste est rémunéré.

  '
examples:
- value: 'False'
- value: 'True'
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:isPaid
domain_of:
- InterestLink
- Occupation
range: boolean

```
</details></div>