---
search:
  boost: 5.0
---

# Slot: majority_type 


_[en] Type of majority required for the vote (absolute, two-thirds, etc.)._

_[de] Art der für die Abstimmung erforderlichen Mehrheit (absolut, Zweidrittel usw.)._

__



<div data-search-exclude markdown="1">



URI: [ops:majority_type](https://ch.paf.link/schema/operations/majority_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |






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





## LinkML Source

<details>
```yaml
name: majority_type
description: '[en] Type of majority required for the vote (absolute, two-thirds, etc.).

  [de] Art der für die Abstimmung erforderlichen Mehrheit (absolut, Zweidrittel usw.).

  '
examples:
- value: absolute
from_schema: https://ch.paf.link/schema/operations
rank: 1000
domain_of:
- Voting
- Election
range: MajorityTypeEnum

```
</details></div>