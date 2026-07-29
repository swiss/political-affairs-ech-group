---
search:
  boost: 5.0
---

# Slot: resolution_type 


_Type of resolution taken on the agenda item._




<div data-search-exclude markdown="1">



URI: [ops:resolution_type](https://ch.paf.link/schema/operations/resolution_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Resolution](Resolution.md) | A resolution or decision taken on an agenda item, including voting procedures |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ResolutionTypeEnum](ResolutionTypeEnum.md) |
| Domain Of | [Resolution](Resolution.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: resolution_type
annotations:
  description_de:
    tag: description_de
    value: 'Art der Resolution zum Traktandum.

      '
  description_fr:
    tag: description_fr
    value: 'Type de décision prise sur le point de l''ordre du jour.

      '
description: 'Type of resolution taken on the agenda item.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Resolution
range: ResolutionTypeEnum

```
</details></div>