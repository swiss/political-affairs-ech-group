---
search:
  boost: 5.0
---

# Slot: expression_description 


_Descriptive text of the language version._




<div data-search-exclude markdown="1">



URI: [schema:description](http://schema.org/description)
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
| Slot URI | [schema:description](http://schema.org/description) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: expression_description
annotations:
  description_de:
    tag: description_de
    value: 'Beschreibender Text zur Sprachfassung.

      '
  description_fr:
    tag: description_fr
    value: 'Texte descriptif de la version linguistique.

      '
description: 'Descriptive text of the language version.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: schema:description
domain_of:
- Expression
range: string

```
</details></div>