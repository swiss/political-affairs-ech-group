---
search:
  boost: 5.0
---

# Slot: id 


_Unique identifier of the element._




<div data-search-exclude markdown="1">



URI: [ops:id](https://ch.paf.link/schema/operations/id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Work](Work.md) | FRBR Work: the abstract document as such, independent of a concrete language ... |  no  |
| [Expression](Expression.md) | FRBR Expression: a concrete language version of a Work |  no  |
| [Manifestation](Manifestation.md) | FRBR Manifestation: a concrete file format of an Expression, addressable via ... |  no  |
| [WorkContainer](WorkContainer.md) | Container for the documents (FRBR Works) of this schema |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Work](Work.md), [Expression](Expression.md), [Manifestation](Manifestation.md), [WorkContainer](WorkContainer.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |














## LinkML Source

<details>
```yaml
name: id
annotations:
  description_de:
    tag: description_de
    value: 'Eindeutiger Identifikator des Elements.

      '
  description_fr:
    tag: description_fr
    value: 'Identifiant univoque de l''élément.

      '
description: 'Unique identifier of the element.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
identifier: true
domain_of:
- Work
- Expression
- Manifestation
- WorkContainer
range: string
required: true

```
</details></div>