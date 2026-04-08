---
search:
  boost: 5.0
---

# Slot: citizenships 


_[de] Staatsbürgerschaften der Person._

_[en] Citizenships of the person._

__



<div data-search-exclude markdown="1">



URI: [act:citizenship](https://ld.ech.ch/schema/0294/actors/citizenship)
Alias: citizenships

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | [de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften u... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Citizenship](Citizenship.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [act:citizenship](https://ld.ech.ch/schema/0294/actors/citizenship) |

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
| self | act:citizenship |
| native | act:citizenships |




## LinkML Source

<details>
```yaml
name: citizenships
description: '[de] Staatsbürgerschaften der Person.

  [en] Citizenships of the person.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:citizenship
alias: citizenships
domain_of:
- Person
range: Citizenship
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>