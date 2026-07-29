---
search:
  boost: 5.0
---

# Slot: count 


_The count of votes for the total other category._




<div data-search-exclude markdown="1">



URI: [ops:count](https://ch.paf.link/schema/operations/count)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TotalOther](TotalOther.md) | Additional vote counts when multiple options are presented (e |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [TotalOther](TotalOther.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: count
annotations:
  description_de:
    tag: description_de
    value: 'Die Anzahl der Stimmen für die Kategorie „Andere“.

      '
  description_fr:
    tag: description_fr
    value: 'Le nombre de voix pour la catégorie « autres ».

      '
description: 'The count of votes for the total other category.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- TotalOther
range: integer

```
</details></div>