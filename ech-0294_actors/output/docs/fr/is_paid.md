---
search:
  boost: 5.0
---

# Slot: is_paid 


_Indicates if the position is paid._

__



<div data-search-exclude markdown="1">



URI: [act:isPaid](https://ld.ech.ch/schema/0294/actors/isPaid)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [InterestLink](InterestLink.md) | An interest link (conflict of interest, political financing) of a person to a... |  no  |
| [Occupation](Occupation.md) | Occupation or profession of a person indicating a label, an ISCO-19 code, whe... |  no  |






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
description: 'Indicates if the position is paid.

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