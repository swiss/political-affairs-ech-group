---
search:
  boost: 5.0
---

# Slot: training_type 


_Typ der Ausbildung oder Bildung._

__



<div data-search-exclude markdown="1">



URI: [act:trainingType](https://ld.ech.ch/schema/0294/actors/trainingType)
<!-- no inheritance hierarchy -->





## Anwendbare Klassen

| Name | Beschreibung | Ändert Slot |
| --- | --- | --- |
| [Training](Training.md) | Ausbildung oder Bildung einer Person mit Angabe eines Typs (z |  no  |






## Eigenschaften

### Typ und Wertebereich

| Eigenschaft | Wert |
| --- | --- |
| Wertebereich | [TrainingTypeEnum](TrainingTypeEnum.md) |
| Domäne von | [Training](Training.md) |
| Slot-URI | [act:trainingType](https://ld.ech.ch/schema/0294/actors/trainingType) |

### Kardinalität und Anforderungen

| Eigenschaft | Wert |
| --- | --- |









## Beispiele

| Wert |
| --- |
| 3223 |





## LinkML-Quelle

<details>
```yaml
name: training_type
annotations:
  description_de:
    tag: description_de
    value: 'Typ der Ausbildung oder Bildung.

      '
  description_fr:
    tag: description_fr
    value: 'Type de formation ou d''éducation.

      '
description: 'Typ der Ausbildung oder Bildung.

  '
examples:
- value: '3223'
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:trainingType
domain_of:
- Training
range: TrainingTypeEnum

```
</details></div>