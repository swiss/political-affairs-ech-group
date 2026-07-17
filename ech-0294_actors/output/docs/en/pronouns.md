---
search:
  boost: 5.0
---

# Slot: pronouns 


_Pronouns used by the person._

__



<div data-search-exclude markdown="1">



URI: [act:pronouns](https://ld.ech.ch/schema/0294/actors/pronouns)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Gender](Gender.md) | Gender of a person indicating a gender code and temporal validity |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Gender](Gender.md) |
| Slot URI | [act:pronouns](https://ld.ech.ch/schema/0294/actors/pronouns) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: pronouns
annotations:
  description_de:
    tag: description_de
    value: 'Von der Person verwendete Pronomen.

      '
  description_fr:
    tag: description_fr
    value: 'Pronoms utilisés par la personne.

      '
description: 'Pronouns used by the person.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: act:pronouns
domain_of:
- Gender
range: string
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>