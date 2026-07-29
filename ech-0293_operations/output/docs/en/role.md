---
search:
  boost: 5.0
---

# Slot: role 


_Role of the person (e.g., commission speaker)._




<div data-search-exclude markdown="1">



URI: [ops:role](https://ch.paf.link/schema/operations/role)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Speech](Speech.md) | A speech or statement made during a meeting (also called Votum or speaker seg... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Speech](Speech.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| speaker |





## LinkML Source

<details>
```yaml
name: role
annotations:
  description_de:
    tag: description_de
    value: 'Rolle der Person (z.B. Kommissionssprecherin oder Kommissionssprecher).

      '
  description_fr:
    tag: description_fr
    value: 'Rôle de la personne (p. ex. rapporteuse ou rapporteur de commission).

      '
description: 'Role of the person (e.g., commission speaker).

  '
examples:
- value: speaker
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Speech
range: string

```
</details></div>