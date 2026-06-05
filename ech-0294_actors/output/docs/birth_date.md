---
search:
  boost: 5.0
---

# Slot: birth_date 


_Exact date of birth if available and public. This field has precedence over the field `birthYear`._

__



<div data-search-exclude markdown="1">



URI: [schema:birthDate](http://schema.org/birthDate)
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
| Slot URI | [schema:birthDate](http://schema.org/birthDate) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 1952-03-11 |
| 1964-07-12 |





## LinkML Source

<details>
```yaml
name: birth_date
annotations:
  description_de:
    tag: description_de
    value: 'Genaues Geburtsdatum, sofern verfügbar und öffentlich. Dieses Feld hat
      Vorrang vor dem Feld `birthYear`.

      '
description: 'Exact date of birth if available and public. This field has precedence
  over the field `birthYear`.

  '
examples:
- value: '1952-03-11'
- value: '1964-07-12'
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: schema:birthDate
domain_of:
- Person
range: date

```
</details></div>