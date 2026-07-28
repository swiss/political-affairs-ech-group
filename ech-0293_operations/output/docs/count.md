---
search:
  boost: 5.0
---

# Slot: count 


_[en] The count of votes for the total other category._

_[de] Die Anzahl der Stimmen für die Kategorie "Andere"._

__



<div data-search-exclude markdown="1">



URI: [ops:count](https://ch.paf.link/schema/operations/count)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TotalOther](TotalOther.md) | [en] Additional vote counts when multiple options are presented (e |  no  |






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
description: '[en] The count of votes for the total other category.

  [de] Die Anzahl der Stimmen für die Kategorie "Andere".

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- TotalOther
range: integer

```
</details></div>