

# Slot: state_name 


_[en] Custom state description for the meeting._

_[de] Benutzerdefinierte Zustandsbeschreibung für die Sitzung._

__





URI: [ops:state_name](https://ch.paf.link/schema/operations/state_name)
Alias: state_name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |
| [AgendaItem](AgendaItem.md) | [en] An agenda item of a meeting |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:state_name |
| native | ops:state_name |




## LinkML Source

<details>
```yaml
name: state_name
description: '[en] Custom state description for the meeting.

  [de] Benutzerdefinierte Zustandsbeschreibung für die Sitzung.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: state_name
domain_of:
- Meeting
- AgendaItem
range: string

```
</details>