---
search:
  boost: 5.0
---

# Slot: text_type 


_Type of text (raw draft, edited version)._




<div data-search-exclude markdown="1">



URI: [ops:text_type](https://ch.paf.link/schema/operations/text_type)
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
| final |





## LinkML Source

<details>
```yaml
name: text_type
annotations:
  description_de:
    tag: description_de
    value: 'Typ des Textes (Rohfassung, bearbeitete Fassung).

      '
  description_fr:
    tag: description_fr
    value: 'Type de texte (version brute, version éditée).

      '
description: 'Type of text (raw draft, edited version).

  '
examples:
- value: final
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Speech
range: string

```
</details></div>