---
search:
  boost: 5.0
---

# Slot: majority_type 


_Type of majority required for the vote (absolute, two-thirds, etc.)._




<div data-search-exclude markdown="1">



URI: [ops:majority_type](https://ch.paf.link/schema/operations/majority_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | A voting procedure with individual votes and results |  no  |
| [Election](Election.md) | An election procedure for selecting persons to positions |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MajorityTypeEnum](MajorityTypeEnum.md) |
| Domain Of | [Voting](Voting.md), [Election](Election.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| absolute |
| other |





## LinkML Source

<details>
```yaml
name: majority_type
annotations:
  description_de:
    tag: description_de
    value: 'Art der für die Abstimmung erforderlichen Mehrheit (absolut, Zweidrittel
      usw.).

      '
  description_fr:
    tag: description_fr
    value: 'Type de majorité requise pour le vote (absolue, deux tiers, etc.).

      '
description: 'Type of majority required for the vote (absolute, two-thirds, etc.).

  '
examples:
- value: absolute
- value: other
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
- Election
range: MajorityTypeEnum

```
</details></div>