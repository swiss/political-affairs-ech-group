---
search:
  boost: 5.0
---

# Slot: election_type 


_Type of election procedure_



<div data-search-exclude markdown="1">



URI: [ops:election_type](https://ch.paf.link/schema/operations/election_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ElectionTypeEnum](ElectionTypeEnum.md) |
| Domain Of | [Election](Election.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: election_type
description: Type of election procedure
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Election
range: ElectionTypeEnum

```
</details></div>