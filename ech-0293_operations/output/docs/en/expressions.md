---
search:
  boost: 5.0
---

# Slot: expressions 


_The language versions (Expressions) of a Work._




<div data-search-exclude markdown="1">



URI: [meta:expressions](https://ch.paf.link/schema/meta/expressions)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Work](Work.md) | FRBR Work: the abstract document as such, independent of a concrete language ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Expression](Expression.md) |
| Domain Of | [Work](Work.md) |
| Slot URI | [meta:expressions](https://ch.paf.link/schema/meta/expressions) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: expressions
annotations:
  description_de:
    tag: description_de
    value: 'Die Sprachfassungen (Expressions) eines Works.

      '
  description_fr:
    tag: description_fr
    value: 'Les versions linguistiques (Expressions) d''un Work.

      '
description: 'The language versions (Expressions) of a Work.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:expressions
domain_of:
- Work
range: Expression
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>