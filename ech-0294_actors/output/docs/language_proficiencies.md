---
search:
  boost: 5.0
---

# Slot: language_proficiencies 


_Language proficiencies of the person._

__



<div data-search-exclude markdown="1">



URI: [act:languageProficiency](https://ld.ech.ch/schema/0294/actors/languageProficiency)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | A person with identifiers, names, addresses, citizenships, and occupations |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LanguageProficiency](LanguageProficiency.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [act:languageProficiency](https://ld.ech.ch/schema/0294/actors/languageProficiency) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: language_proficiencies
annotations:
  description_de:
    tag: description_de
    value: 'Sprachkompetenzen der Person.

      '
description: 'Language proficiencies of the person.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:languageProficiency
domain_of:
- Person
range: LanguageProficiency
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>