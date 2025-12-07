

# Slot: affair_id 


_[en] The connection to the affairs (business items) of the agenda item._

_[de] Die Verbindung zu den Geschäften (Geschäftsgegenständen) des Tagesordnungspunkts._

__





URI: [ops:affair_id](https://ch.paf.link/schema/operations/affair_id)
Alias: affair_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |
| [AgendaItem](AgendaItem.md) | [en] An agenda item of a meeting |  no  |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:affair_id |
| native | ops:affair_id |




## LinkML Source

<details>
```yaml
name: affair_id
description: '[en] The connection to the affairs (business items) of the agenda item.

  [de] Die Verbindung zu den Geschäften (Geschäftsgegenständen) des Tagesordnungspunkts.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: affair_id
domain_of:
- AgendaItem
- Voting
- Election
range: string

```
</details>