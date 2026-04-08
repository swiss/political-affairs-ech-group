---
search:
  boost: 5.0
---

# Slot: occupations 


_[de] Berufe oder Tätigkeiten der Person._

_[en] Occupations or professions of the person._

__



<div data-search-exclude markdown="1">



URI: [act:occupation](https://ld.ech.ch/schema/0294/actors/occupation)
Alias: occupations

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | [de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften u... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Occupation](Occupation.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [act:occupation](https://ld.ech.ch/schema/0294/actors/occupation) |

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
| self | act:occupation |
| native | act:occupations |




## LinkML Source

<details>
```yaml
name: occupations
description: '[de] Berufe oder Tätigkeiten der Person.

  [en] Occupations or professions of the person.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:occupation
alias: occupations
domain_of:
- Person
range: Occupation
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>