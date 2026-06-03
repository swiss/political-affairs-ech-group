---
search:
  boost: 5.0
---

# Slot: date_begin_actual 


_The actual start date of an event or occurrence with time duration._

__



<div data-search-exclude markdown="1">



URI: [mcm:dateBeginActual](https://ld.ech.ch/schema/0292/meta-common/dateBeginActual)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IsEventWithDuration](IsEventWithDuration.md) | A mixin class that provides slots for modeling events or occurrences with tim... |  no  |
| [Legislature](Legislature.md) | [en] Term of office of a parliament as a legislative assembly |  no  |
| [Session](Session.md) | [en] A parliamentary session that groups multiple meetings and spans a specif... |  no  |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |
| [AgendaItem](AgendaItem.md) | [en] An agenda item of a meeting |  no  |
| [ProtocolItem](ProtocolItem.md) | [en] An agenda item as actually recorded in the protocol |  no  |
| [IsProcessStep](IsProcessStep.md) | A mixin class for a single step in a multi-stage process (e |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [IsEventWithDuration](IsEventWithDuration.md) |
| Slot URI | [mcm:dateBeginActual](https://ld.ech.ch/schema/0292/meta-common/dateBeginActual) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| description_de | Das tatsächliche Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer.
 |




### Schema Source


* from schema: https://ch.paf.link/schema/operations




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:dateBeginActual |
| native | ops:date_begin_actual |




## LinkML Source

<details>
```yaml
name: date_begin_actual
annotations:
  description_de:
    tag: description_de
    value: 'Das tatsächliche Startdatum eines Ereignisses oder Vorkommnissen mit Zeitdauer.

      '
description: 'The actual start date of an event or occurrence with time duration.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:dateBeginActual
domain_of:
- IsEventWithDuration
range: date

```
</details></div>