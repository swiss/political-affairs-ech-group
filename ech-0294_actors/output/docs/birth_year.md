---
search:
  boost: 5.0
---

# Slot: birth_year 


_Year of birth. Only to be used, if there is no full `birthDate` available._

__



<div data-search-exclude markdown="1">



URI: [act:birthYear](https://ld.ech.ch/schema/0294/actors/birthYear)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [act:birthYear](https://ld.ech.ch/schema/0294/actors/birthYear) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: birth_year
annotations:
  description_de:
    tag: description_de
    value: 'Geburtsjahr. Nur zu verwenden, wenn kein vollständiges `birthDate` vorhanden
      ist.

      '
description: 'Year of birth. Only to be used, if there is no full `birthDate` available.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:birthYear
domain_of:
- Person
range: integer

```
</details></div>