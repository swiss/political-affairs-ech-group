

# Slot: parent_legislature 


_[en] The legislative body in which the meeting is based._

_[de] Der gesetzgebende Körper, auf dem die Sitzung basiert._

__





URI: [ops:parent_legislature](https://ch.paf.link/schema/operations/parent_legislature)
Alias: parent_legislature

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Session](Session.md) | [en] A parliamentary session that groups multiple meetings and spans a specif... |  no  |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:parent_legislature |
| native | ops:parent_legislature |




## LinkML Source

<details>
```yaml
name: parent_legislature
description: '[en] The legislative body in which the meeting is based.

  [de] Der gesetzgebende Körper, auf dem die Sitzung basiert.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: parent_legislature
domain_of:
- Session
- Meeting
range: string

```
</details>