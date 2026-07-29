---
search:
  boost: 5.0
---

# Slot: manifestations 


_The file forms (Manifestations) of an Expression._




<div data-search-exclude markdown="1">



URI: [meta:manifestations](https://ch.paf.link/schema/meta/manifestations)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Expression](Expression.md) | FRBR Expression: a concrete language version of a Work |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Manifestation](Manifestation.md) |
| Domain Of | [Expression](Expression.md) |
| Slot URI | [meta:manifestations](https://ch.paf.link/schema/meta/manifestations) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: manifestations
annotations:
  description_de:
    tag: description_de
    value: 'Die Dateiformen (Manifestations) einer Expression.

      '
  description_fr:
    tag: description_fr
    value: 'Les formes de fichier (Manifestations) d''une Expression.

      '
description: 'The file forms (Manifestations) of an Expression.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:manifestations
domain_of:
- Expression
range: Manifestation
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>