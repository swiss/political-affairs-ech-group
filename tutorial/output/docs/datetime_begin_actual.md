---
search:
  boost: 5.0
---

# Slot: datetime_begin_actual 


_The actual start date and time of an event or occurrence with time duration._

__



<div data-search-exclude markdown="1">



URI: [mcm:datetimeBeginActual](https://ld.ech.ch/schema/0292/meta-common/datetimeBeginActual)
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
| Domain Of | [IsEventWithDuration](IsEventWithDuration.md) |
| Slot URI | [mcm:datetimeBeginActual](https://ld.ech.ch/schema/0292/meta-common/datetimeBeginActual) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| description_de | Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen mit Zeitdauer.
 |




### Schema Source


* from schema: https://ch.paf.link/schema/tutorial




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mcm:datetimeBeginActual |
| native | tutorial:datetime_begin_actual |




## LinkML Source

<details>
```yaml
name: datetime_begin_actual
annotations:
  description_de:
    tag: description_de
    value: 'Das tatsächliche Startdatum und die Uhrzeit eines Ereignisses oder Vorkommnissen
      mit Zeitdauer.

      '
description: 'The actual start date and time of an event or occurrence with time duration.

  '
from_schema: https://ch.paf.link/schema/tutorial
rank: 1000
slot_uri: mcm:datetimeBeginActual
domain_of:
- IsEventWithDuration
range: datetime

```
</details></div>