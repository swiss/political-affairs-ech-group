---
search:
  boost: 5.0
---

# Slot: dates 


_Dates relating to the element, each with a type indication._




<div data-search-exclude markdown="1">



URI: [meta:dates](https://ch.paf.link/schema/meta/dates)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Expression](Expression.md) | FRBR Expression: a concrete language version of a Work |  no  |
| [Manifestation](Manifestation.md) | FRBR Manifestation: a concrete file format of an Expression, addressable via ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [Expression](Expression.md), [Manifestation](Manifestation.md) |
| Slot URI | [meta:dates](https://ch.paf.link/schema/meta/dates) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |












## LinkML Source

<details>
```yaml
name: dates
annotations:
  description_de:
    tag: description_de
    value: 'Datumsangaben zum Element, jeweils mit Typangabe.

      '
  description_fr:
    tag: description_fr
    value: 'Dates relatives à l''élément, chacune assortie d''une indication de type.

      '
description: 'Dates relating to the element, each with a type indication.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: meta:dates
domain_of:
- Expression
- Manifestation
range: Date
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>