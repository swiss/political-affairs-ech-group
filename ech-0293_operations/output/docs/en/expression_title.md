---
search:
  boost: 5.0
---

# Slot: expression_title 


_Title of the language version._




<div data-search-exclude markdown="1">



URI: [meta:title](https://ch.paf.link/schema/meta/title)
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
| Slot URI | [meta:title](https://ch.paf.link/schema/meta/title) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |












## LinkML Source

<details>
```yaml
name: expression_title
annotations:
  description_de:
    tag: description_de
    value: 'Titel der Sprachfassung.

      '
  description_fr:
    tag: description_fr
    value: 'Titre de la version linguistique.

      '
description: 'Title of the language version.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:title
domain_of:
- Expression
range: string
required: true

```
</details></div>