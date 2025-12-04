

# Slot: voting_type 


_[en] Type of voting procedure (preliminary, final, secret, etc.)._

_[de] Art des Abstimmungsverfahrens (Zwischen-, Schlussabstimmung, geheim, etc.)._

__





URI: [ops:voting_type](https://ch.paf.link/schema/operations/voting_type)
Alias: voting_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |






## Properties

* Range: [VotingTypeEnum](VotingTypeEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:voting_type |
| native | ops:voting_type |




## LinkML Source

<details>
```yaml
name: voting_type
description: '[en] Type of voting procedure (preliminary, final, secret, etc.).

  [de] Art des Abstimmungsverfahrens (Zwischen-, Schlussabstimmung, geheim, etc.).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: voting_type
domain_of:
- Voting
range: voting_type_enum

```
</details>