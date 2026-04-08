---
search:
  boost: 5.0
---

# Slot: birth_date 


_[de] Genaues Geburtsdatum._

_[en] Exact date of birth if available and public. This field has precedence over the field `birthYear`._

__



<div data-search-exclude markdown="1">



URI: [schema:birthDate](http://schema.org/birthDate)
Alias: birth_date

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | [de] Eine Person mit Identifikatoren, Namen, Adressen, Staatsbürgerschaften u... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [schema:birthDate](http://schema.org/birthDate) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:birthDate |
| native | act:birth_date |




## LinkML Source

<details>
```yaml
name: birth_date
description: '[de] Genaues Geburtsdatum.

  [en] Exact date of birth if available and public. This field has precedence over
  the field `birthYear`.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: schema:birthDate
alias: birth_date
domain_of:
- Person
range: date

```
</details></div>