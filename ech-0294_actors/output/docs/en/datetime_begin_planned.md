---
search:
  boost: 5.0
---

# Slot: datetime_begin_planned 


_The planned start date and time of an event or occurrence with time duration._

__



<div data-search-exclude markdown="1">



URI: [mcm:datetimeBeginPlanned](https://ld.ech.ch/schema/0292/meta-common/datetimeBeginPlanned)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IsEventWithDuration](IsEventWithDuration.md) | A mixin class that provides slots for modeling events or occurrences with tim... |  no  |
| [IsProcessStep](IsProcessStep.md) | A mixin class for a single step in a multi-stage process (e |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [IsEventWithDuration](IsEventWithDuration.md), [IsProcessStep](IsProcessStep.md) |
| Slot URI | [mcm:datetimeBeginPlanned](https://ld.ech.ch/schema/0292/meta-common/datetimeBeginPlanned) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |












## LinkML Source

<details>
```yaml
name: datetime_begin_planned
annotations:
  description_de:
    tag: description_de
    value: 'Das geplante Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen
      mit Zeitdauer.

      '
description: 'The planned start date and time of an event or occurrence with time
  duration.

  '
from_schema: https://ld.ech.ch/schema/0294/actors
rank: 1000
slot_uri: mcm:datetimeBeginPlanned
domain_of:
- IsEventWithDuration
- IsProcessStep
range: datetime

```
</details></div>