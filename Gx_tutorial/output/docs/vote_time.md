

# Slot: vote_time 


_[en] The date and time when the vote was cast. [de] Das Datum und die Uhrzeit, zu der die Abstimmung abgegeben wurde._

__





URI: [tutorial:voteTime](https://ch.paf.link/schema/tutorial/voteTime)
Alias: vote_time

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Vote](Vote.md) |  |  no  |







## Properties

* Range: [Datetime](Datetime.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ch.paf.link/schema/tutorial




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tutorial:voteTime |
| native | tutorial:vote_time |




## LinkML Source

<details>
```yaml
name: vote_time
description: '[en] The date and time when the vote was cast. [de] Das Datum und die
  Uhrzeit, zu der die Abstimmung abgegeben wurde.

  '
from_schema: https://ch.paf.link/schema/tutorial
rank: 1000
slot_uri: tutorial:voteTime
alias: vote_time
domain_of:
- Vote
range: datetime

```
</details>