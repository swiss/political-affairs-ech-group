---
search:
  boost: 5.0
---

# Slot: expression_language 


_Language code in ISO 639-1 format._




<div data-search-exclude markdown="1">



URI: [dcterms:language](http://purl.org/dc/terms/language)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Expression](Expression.md) | FRBR Expression: a concrete language version of a Work |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Expression](Expression.md) |
| Slot URI | [dcterms:language](http://purl.org/dc/terms/language) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[a-z]{2}$` |














## LinkML Source

<details>
```yaml
name: expression_language
annotations:
  description_de:
    tag: description_de
    value: 'Sprachcode im ISO 639-1-Format.

      '
  description_fr:
    tag: description_fr
    value: 'Code de langue au format ISO 639-1.

      '
description: 'Language code in ISO 639-1 format.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: dcterms:language
domain_of:
- Expression
range: string
required: true
pattern: ^[a-z]{2}$

```
</details></div>