

# Slot: parent_meeting 


_[en] The linked meeting ID that groups the current meeting._

_[de] Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert._

__





URI: [ops:parent_meeting](https://ch.paf.link/schema/operations/parent_meeting)
Alias: parent_meeting

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Election](Election.md) | [en] An election procedure for selecting persons to positions |  no  |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |
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
| self | ops:parent_meeting |
| native | ops:parent_meeting |




## LinkML Source

<details>
```yaml
name: parent_meeting
description: '[en] The linked meeting ID that groups the current meeting.

  [de] Die verknüpfte Sitzungs-ID, die die aktuelle Sitzung gruppiert.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: parent_meeting
domain_of:
- Meeting
- AgendaItem
- Voting
- Election
range: string

```
</details>