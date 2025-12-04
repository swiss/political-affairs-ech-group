

# Slot: date_end_planned 


_[en] Planned end date of the meeting or session._

_[de] Geplantes Enddatum der Sitzung oder Session._

__





URI: [ops:date_end_planned](https://ch.paf.link/schema/operations/date_end_planned)
Alias: date_end_planned

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Session](Session.md) | [en] A parliamentary session that groups multiple meetings and spans a specif... |  no  |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |






## Properties

* Range: [Date](Date.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ops:date_end_planned |
| native | ops:date_end_planned |




## LinkML Source

<details>
```yaml
name: date_end_planned
description: '[en] Planned end date of the meeting or session.

  [de] Geplantes Enddatum der Sitzung oder Session.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: date_end_planned
domain_of:
- Session
- Meeting
range: date

```
</details>