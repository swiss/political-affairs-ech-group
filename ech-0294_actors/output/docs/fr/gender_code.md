---
search:
  boost: 5.0
---

# Slot: gender_code 


_Code de sexe. Valeurs recommandées : male, female, diverse._

__



<div data-search-exclude markdown="1">



URI: [act:genderCode](https://ld.ech.ch/schema/0294/actors/genderCode)
<!-- no inheritance hierarchy -->





## Classes applicables

| Nom | Description | Modifie le slot |
| --- | --- | --- |
| [Gender](Gender.md) | Sexe d'une personne indiquant un code de sexe et la validité temporelle |  yes  |






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
  description_fr:
    tag: description_fr
    value: 'Code de sexe. Valeurs recommandées : male, female, diverse.

      '
description: 'Code de sexe. Valeurs recommandées : male, female, diverse.

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