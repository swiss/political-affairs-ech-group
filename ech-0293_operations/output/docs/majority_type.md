

# Slot: majority_type 


_[en] Type of majority required for the vote (absolute, two-thirds, etc.)._

_[de] Art der für die Abstimmung erforderlichen Mehrheit (absolut, Zweidrittel usw.)._

__





URI: [ops:majority_type](https://ch.paf.link/schema/operations/majority_type)
Alias: majority_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |






## Properties

* Range: [MajorityTypeEnum](MajorityTypeEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:majority_type |
| native | ops:majority_type |




## LinkML Source

<details>
```yaml
name: majority_type
description: '[en] Type of majority required for the vote (absolute, two-thirds, etc.).

  [de] Art der für die Abstimmung erforderlichen Mehrheit (absolut, Zweidrittel usw.).

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: majority_type
domain_of:
- Voting
- Election
range: majority_type_enum

```
</details>