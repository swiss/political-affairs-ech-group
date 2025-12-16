

# Slot: landing_page 


_[en] URL providing further information._

_[de] URL mit weiteren Informationen._

__





URI: [ops:landingPage](https://ch.paf.link/schema/operations/landingPage)
Alias: landing_page

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AgendaItem](AgendaItem.md) | [en] An agenda item of a meeting |  no  |
| [Voting](Voting.md) | [en] A voting procedure with individual votes and results |  no  |
| [Speech](Speech.md) | [en] A speech or statement made during a meeting (also called Votum or speake... |  no  |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |
| [Legislature](Legislature.md) | [en] Term of office of a parliament as a legislative assembly |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:landingPage |
| native | ops:landing_page |




## LinkML Source

<details>
```yaml
name: landing_page
description: '[en] URL providing further information.

  [de] URL mit weiteren Informationen.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: ops:landingPage
alias: landing_page
domain_of:
- Legislature
- Meeting
- AgendaItem
- Voting
- Election
- Speech
range: string

```
</details>