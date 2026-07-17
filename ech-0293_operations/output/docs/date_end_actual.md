---
search:
  boost: 5.0
---

# Slot: date_end_actual 


_The actual end date of an event or occurrence with time duration._

__



<div data-search-exclude markdown="1">



URI: [mcm:dateEndActual](https://ld.ech.ch/schema/0292/meta-common/dateEndActual)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IsEventWithDuration](IsEventWithDuration.md) | A mixin class that provides slots for modeling events or occurrences with tim... |  no  |
| [IsProcessStep](IsProcessStep.md) | A mixin class for a single step in a multi-stage process (e |  no  |
| [Legislature](Legislature.md) | [en] Term of office of a parliament as a legislative assembly |  no  |
| [Session](Session.md) | [en] A parliamentary session that groups multiple meetings and spans a specif... |  no  |
| [Meeting](Meeting.md) | [en] A general meeting class used for Sessions, Comittee Meetings, individual... |  no  |
| [AgendaItem](AgendaItem.md) | [en] An agenda item of a meeting |  no  |
| [ProtocolItem](ProtocolItem.md) | [en] An agenda item as actually recorded in the protocol |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [IsEventWithDuration](IsEventWithDuration.md), [IsProcessStep](IsProcessStep.md) |
| Slot URI | [mcm:dateEndActual](https://ld.ech.ch/schema/0292/meta-common/dateEndActual) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: date_end_actual
annotations:
  description_de:
    tag: description_de
    value: 'Das tatsächliche Enddatum eines Ereignisses oder Vorkommnissen mit Zeitdauer.

      '
  description_fr:
    tag: description_fr
    value: 'La date de fin effective d''un événement ou d''une occurrence avec durée.

      '
description: 'The actual end date of an event or occurrence with time duration.

  '
from_schema: https://ch.paf.link/schema/operations
rank: 1000
slot_uri: mcm:dateEndActual
domain_of:
- IsEventWithDuration
- IsProcessStep
range: date

```
</details></div>