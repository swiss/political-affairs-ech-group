

# Slot: majority_count 


_[en] Number of votes required for the relevant majority threshold._

_[de] Anzahl der Stimmen, die für die relevante Mehrheitsschwelle erforderlich sind._

__





URI: [ops:majority_count](https://ch.paf.link/schema/operations/majority_count)
Alias: majority_count

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
| Range | [Integer](Integer.md) |
| Domain Of | [Voting](Voting.md), [Election](Election.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:majority_count |
| native | ops:majority_count |




## LinkML Source

<details>
```yaml
name: majority_count
description: '[en] Number of votes required for the relevant majority threshold.

  [de] Anzahl der Stimmen, die für die relevante Mehrheitsschwelle erforderlich sind.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: majority_count
domain_of:
- Voting
- Election
range: integer

```
</details>