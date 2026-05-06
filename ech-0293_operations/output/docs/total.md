

# Slot: total 


_[en] Total number of votes, excluding absent and president's vote._

_[de] Gesamtzahl der Stimmen, ohne abwesende und Präsidentenstimmen._

__





URI: [ops:total](https://ch.paf.link/schema/operations/total)
Alias: total

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
| self | ops:total |
| native | ops:total |




## LinkML Source

<details>
```yaml
name: total
description: '[en] Total number of votes, excluding absent and president''s vote.

  [de] Gesamtzahl der Stimmen, ohne abwesende und Präsidentenstimmen.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: total
domain_of:
- Voting
- Election
range: integer

```
</details>