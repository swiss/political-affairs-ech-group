

# Slot: date_begin_planned 


_[en] Planned start date of the meeting or session._

_[de] Geplantes Startdatum der Sitzung oder Session._

__





URI: [ops:date_begin_planned](https://ch.paf.link/schema/operations/date_begin_planned)
Alias: date_begin_planned

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
| self | ops:date_begin_planned |
| native | ops:date_begin_planned |




## LinkML Source

<details>
```yaml
name: date_begin_planned
description: '[en] Planned start date of the meeting or session.

  [de] Geplantes Startdatum der Sitzung oder Session.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
alias: date_begin_planned
domain_of:
- Session
- Meeting
range: date

```
</details>