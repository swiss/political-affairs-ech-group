---
search:
  boost: 5.0
---

# Slot: training_type 


_Type of training or education._

__



<div data-search-exclude markdown="1">



URI: [act:trainingType](https://ld.ech.ch/schema/0294/actors/trainingType)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Training](Training.md) | Training or education of a person indicating a type (e |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TrainingTypeEnum](TrainingTypeEnum.md) |
| Domain Of | [Training](Training.md) |
| Slot URI | [act:trainingType](https://ld.ech.ch/schema/0294/actors/trainingType) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 3223 |





## LinkML Source

<details>
```yaml
name: training_type
annotations:
  description_de:
    tag: description_de
    value: 'Typ der Ausbildung oder Bildung.

      '
description: 'Type of training or education.

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