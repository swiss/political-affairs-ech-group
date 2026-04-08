---
search:
  boost: 5.0
---

# Slot: genders 


_[de] Geschlecht der Person._

_[en] Gender of the person._

__



<div data-search-exclude markdown="1">



URI: [act:gender](https://ld.ech.ch/schema/0294/actors/gender)
Alias: genders

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | [de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften u... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Gender](Gender.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [act:gender](https://ld.ech.ch/schema/0294/actors/gender) |

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
| self | act:gender |
| native | act:genders |




## LinkML Source

<details>
```yaml
name: genders
description: '[de] Geschlecht der Person.

  [en] Gender of the person.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:gender
alias: genders
domain_of:
- Person
range: Gender
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>