---
search:
  boost: 5.0
---

# Slot: trainings 


_[de] Ausbildungen oder Bildungen der Person._

_[en] Trainings or educations of the person._

__



<div data-search-exclude markdown="1">



URI: [act:training](https://ld.ech.ch/schema/0294/actors/training)
Alias: trainings

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | [de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften u... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Training](Training.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [act:training](https://ld.ech.ch/schema/0294/actors/training) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | act:training |
| native | act:trainings |




## LinkML Source

<details>
```yaml
name: trainings
description: '[de] Ausbildungen oder Bildungen der Person.

  [en] Trainings or educations of the person.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:training
alias: trainings
domain_of:
- Person
range: Training
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>