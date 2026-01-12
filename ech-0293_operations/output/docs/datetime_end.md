

# Slot: datetime_end 


_[en] The date and time when the meeting or voting ends._

_[de] Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung endet._

__





URI: [ops:datetime_end](https://ch.paf.link/schema/operations/datetime_end)
Alias: datetime_end

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |
| [Speech](Speech.md) | [en] A speech or statement made during a meeting (also called Votum or speake... |  no  |






## Properties

* Range: [Datetime](Datetime.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:datetime_end |
| native | ops:datetime_end |




## LinkML Source

<details>
```yaml
name: datetime_end
description: '[en] The date and time when the meeting or voting ends.

  [de] Das Datum und die Uhrzeit, zu der die Sitzung oder Abstimmung endet.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: datetime_end
domain_of:
- Voting
- Election
- Speech
range: datetime

```
</details>