---
search:
  boost: 5.0
---

# Slot: gender_code 


_Gender code. Recommended values: male, female, diverse._

__



<div data-search-exclude markdown="1">



URI: [act:genderCode](https://ld.ech.ch/schema/0294/actors/genderCode)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Gender](Gender.md) | Gender of a person indicating a gender code and temporal validity |  no  |






## Propriétés

### Type et plage

| Propriété | Valeur |
| --- | --- |
| Plage | [GenderCodeEnum](GenderCodeEnum.md) |
| Domaine de | [Gender](Gender.md) |
| URI du slot | [act:genderCode](https://ld.ech.ch/schema/0294/actors/genderCode) |

### Cardinalité et exigences

| Propriété | Valeur |
| --- | --- |









## Exemples

| Valeur |
| --- |
| male |





## Source LinkML

<details>
```yaml
name: gender_code
annotations:
  description_de:
    tag: description_de
    value: 'Geschlechtscode. Empfohlene Werte: male, female, diverse .

      '
description: 'Gender code. Recommended values: male, female, diverse.

  '
examples:
- value: male
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:genderCode
domain_of:
- Gender
range: GenderCodeEnum

```
</details></div>