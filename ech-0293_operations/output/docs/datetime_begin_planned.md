---
search:
  boost: 5.0
---

# Slot: datetime_begin_planned 


_[de] Das geplante Startdatum und die Uhrzeit eines Ereignisses oder Vorkommens mit Zeitdauer._

_[en] The planned start date and time of an event or occurrence with time duration._

__



<div data-search-exclude markdown="1">



URI: [mcm:datetimeBeginPlanned](https://ld.ech.ch/schema/0292/meta-common/datetimeBeginPlanned)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IsEventWithDuration](IsEventWithDuration.md) | [de] Eine Mixin-Klasse, die Slots für die Modellierung von Ereignissen oder V... |  no  |
| [Legislature](Legislature.md) | [en] Term of office of a parliament as a legislative assembly |  no  |
| [Session](Session.md) | [en] A parliamentary session that groups multiple meetings and spans a specif... |  no  |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |
| [AgendaItem](AgendaItem.md) | [en] An agenda item of a meeting |  no  |
| [IsProcessStep](IsProcessStep.md) | [de] Eine Mixin-Klasse für einen einzelnen Schritt in einem |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [IsEventWithDuration](IsEventWithDuration.md) |
| Slot URI | [mcm:datetimeBeginPlanned](https://ld.ech.ch/schema/0292/meta-common/datetimeBeginPlanned) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:datetimeBeginPlanned |
| native | ops:datetime_begin_planned |




## LinkML Source

<details>
```yaml
name: datetime_begin_planned
description: '[de] Das geplante Startdatum und die Uhrzeit eines Ereignisses oder
  Vorkommens mit Zeitdauer.

  [en] The planned start date and time of an event or occurrence with time duration.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:datetimeBeginPlanned
domain_of:
- IsEventWithDuration
range: datetime

```
</details></div>