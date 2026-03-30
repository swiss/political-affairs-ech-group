

# Slot: death_date 


_[de] Genaues Todesdatum._

_[en] Exact date of death._

__





URI: [schema:deathDate](http://schema.org/deathDate)
Alias: death_date

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
| Slot URI | [schema:deathDate](http://schema.org/deathDate) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ld.ech.ch/schema/0294/actors




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:deathDate |
| native | act:death_date |




## LinkML Source

<details>
```yaml
name: death_date
description: '[de] Genaues Todesdatum.

  [en] Exact date of death.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: schema:deathDate
alias: death_date
domain_of:
- Person
range: date

```
</details>