---
search:
  boost: 5.0
---

# Slot: death_date 


_Exact date of death._

__



<div data-search-exclude markdown="1">



URI: [schema:deathDate](http://schema.org/deathDate)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |






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












## LinkML Source

<details>
```yaml
name: death_date
annotations:
  description_de:
    tag: description_de
    value: 'Genaues Todesdatum.

      '
description: 'Exact date of death.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: schema:deathDate
domain_of:
- Person
range: date

```
</details></div>