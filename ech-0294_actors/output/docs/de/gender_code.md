---
search:
  boost: 5.0
---

# Slot: gender_code 


_Geschlechtscode. Empfohlene Werte: male, female, diverse ._

__



<div data-search-exclude markdown="1">



URI: [act:genderCode](https://ld.ech.ch/schema/0294/actors/genderCode)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Gender](Gender.md) | Geschlecht einer Person mit Angabe eines Geschlechtscodes und der zeitlichen ... |  yes  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [GenderCodeEnum](GenderCodeEnum.md) |
| Domäne von | [Gender](Gender.md) |
| Slot-URI | [act:genderCode](https://ld.ech.ch/schema/0294/actors/genderCode) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| male |





## LinkML-Quelle

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
description: 'Geschlechtscode. Empfohlene Werte: male, female, diverse .

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