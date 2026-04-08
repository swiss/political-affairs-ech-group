---
search:
  boost: 5.0
---

# Slot: names 


_[en] Names of the person with type and value._

_[de] Namen der Person mit Typ und Wert._

__



<div data-search-exclude markdown="1">



URI: [act:name](https://ld.ech.ch/schema/0294/actors/name)
Alias: names

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | [de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften u... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Name](Name.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [act:name](https://ld.ech.ch/schema/0294/actors/name) |

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
| self | act:name |
| native | act:names |




## LinkML Source

<details>
```yaml
name: names
description: '[en] Names of the person with type and value.

  [de] Namen der Person mit Typ und Wert.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:name
alias: names
domain_of:
- Person
range: Name
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>